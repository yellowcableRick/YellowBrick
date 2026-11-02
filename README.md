# YellowBrick

Parts library for the modular MTG storage rack (v3). Everything sits on a 32 mm grid (1 BU).

Open the library: https://yellowcablerick.github.io/YellowBrick/

- `index.html` — the library page: pick a part, pick a model, see it in 3D, download the STL. Modules (a block
  with its parts in place) are composed in the page from the part models: explode, parts list, one STL of the whole.
- `modules.json` — where each part of a module goes, per size.
- `models/` — one `.glb` per model, for the 3D view.
- `stl/` — one `.stl` per model, for printing.

| Part | Models |
| --- | --- |
| Wall | 81 (depth 1–9 × height 1–9 BU) |
| Bar | 9 (width 1–9 BU); also the joist and the stop |
| Back X | 72 (width 2–9 × height 1–9 BU) |
| Sled bar | 9 (width 1–9 BU) |
| Side ledge | 1 |
| Sled | 12 (width 1, 3, 5, 7 × depth 3, 5, 7 BU) |
| Seam clip | 2 (between rows, top or bottom) |
| End clip | 3 (between rows, corner A, corner B) |
| Depth clip | 1 |
| Base tile | 1 |

| Module | Sizes |
| --- | --- |
| Gridfinity drawer | 96 (width 1, 3, 5, 7 × depth 3, 5, 7 × height 2–9 BU) |
