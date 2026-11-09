"""Slices the library's print jobs with Bambu Studio's command line, for one printer, nozzle, filament and plate.
Runs on GitHub Actions (see .github/workflows/slice.yml). Usage: slice.py <bambu-studio> <profiles dir> <jobs.json> <out dir>
Every job is a list of print-oriented STLs (print/stl, made by the library's generator) that Bambu Studio arranges on
the plate(s) and slices into one .gcode.3mf. The system presets are flattened (their 'inherits' chains resolved), so
the command line gets complete settings."""
import json, os, subprocess, sys, time

PRINTER = "Bambu Lab H2D 0.4 nozzle"
PROCESS = "0.20mm Standard @BBL H2D"
FILAMENT = "Bambu PETG Basic @BBL H2D 0.4 nozzle"
BED = {"curr_bed_type": "Textured PEI Plate"}


def index(prof):
    """preset name -> file, from the vendor index (BBL.json next to the BBL folder)."""
    idx = json.load(open(prof.rstrip("/") + ".json")); P = {}
    for k in ("machine_model_list", "filament_list", "machine_list", "process_list"):
        for x in idx.get(k, []): P[x["name"]] = os.path.join(prof, x["sub_path"])
    return P


def flat(P, name):
    """a system preset with its 'inherits' chain and 'include' templates resolved."""
    d = json.load(open(P[name])); base = {}
    if d.get("inherits"): base = flat(P, d["inherits"])
    for inc in d.get("include", []): base.update(flat(P, inc))
    base.update({k: v for k, v in d.items() if k not in ("inherits", "include")})
    return base


def write_flat(P, kind, name, out, extra=None):
    d = flat(P, name); d.update(extra or {})
    d["from"] = "User"; d["is_custom_defined"] = "1"; d["name"] = name
    path = os.path.join(out, f"_{kind}.json"); json.dump(d, open(path, "w"), indent=1)
    return path


def main(studio, prof, jobs_file, out):
    os.makedirs(out, exist_ok=True)
    log = open(os.path.join(out, "log.txt"), "a")
    def say(*a):
        s = " ".join(str(x) for x in a); print(s); log.write(s + "\n"); log.flush()
    P = index(prof)
    m = write_flat(P, "machine", PRINTER, out)
    f = write_flat(P, "filament", FILAMENT, out)
    jobs = json.load(open(jobs_file)); done = {}
    for job in jobs:
        p = write_flat(P, "process", PROCESS, out, dict(BED, **job.get("process", {})))
        target = os.path.join(out, job["id"] + ".gcode.3mf")
        cmd = [studio, "--arrange", "1", "--load-settings", f"{m};{p}", "--load-filaments", f,
               "--slice", "0", "--allow-newer-file", "--export-3mf", target] + job["files"]
        t = time.time(); r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        ok = r.returncode == 0 and os.path.exists(target)
        say(f"{job['id']}: {'ok' if ok else 'FAILED rc=' + str(r.returncode)} in {time.time() - t:.0f}s")
        if not ok: say(r.stdout[-3000:]); say(r.stderr[-3000:])
        done[job["id"]] = {"ok": ok, "file": os.path.basename(target) if ok else None}
    json.dump(done, open(os.path.join(out, "sliced.json"), "w"), indent=1)


if __name__ == "__main__":
    main(*sys.argv[1:5])
