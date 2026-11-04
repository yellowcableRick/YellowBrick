# YellowBrick

Parts library for the modular MTG storage rack (v3). Everything sits on a 32 mm grid (1 BU).

Open the library: https://yellowcablerick.github.io/YellowBrick/

- `index.html` — the library page: pick a part, pick a model, see it in 3D, download the STL. Modules (a block
  with its parts in place) are composed in the page from the part models: explode, parts list, one STL of the whole.
- `modules.json` — where each part of a module goes, per size.
- `models/` — one `.glb` per model, for the 3D view.
- `stl/` — one `.stl` per model, for printing.

| Group | Part | Models |
| --- | --- | --- |
| Frame | Wall | 81 (depth 1–9 × height 1–9 BU) |
| Frame | Bar | 9 (width 1–9 BU); also the joist and the stop |
| Frame | Back X | 72 (width 2–9 × height 1–9 BU) |
| Joints | Seam clip | 2 (between rows, top or bottom) |
| Joints | End clip | 3 (between rows, corner A, corner B) |
| Joints | Staple | 1 (optional, flush across a joint of stacked walls) |
| Joints | Depth clip | 1 |
| Base | Base tile | 1 |
| Drawer | Sled bar | 9 (width 1–9 BU) |
| Drawer | Side ledge | 1 |
| Drawer | Strongbox sled | 84: lengthwise (width 3–9 × depth 4–9 BU) and crosswise (width 4–9 × depth 3–9 BU) |
| Drawer | 100+ Deck Box sled | 49 (width 3–9 × depth 3–9 BU) |
| Drawer | Pull rod | 4 (single; double 9, 10, 11–12 deep) |
| Drawer | Rod knob | 1 |
| Drawer | Gridfinity sled | 72 (width 1–9 × depth 2–9 BU) |

| Module | Sizes |
| --- | --- |
| Gridfinity drawer | 576 (width 1–9 × depth 2–9 × height 2–9 BU); the block and its contents, no clips or tiles |
| Strongbox drawer | 588: Dragon Shield Strongbox deck boxes, lengthwise (width 3–9 × depth 4–9) or crosswise (width 4–9 × depth 3–9), height 3–9 BU |
| 100+ Deck Box drawer | 294: Ultra Pro 100+ Deck Boxes, art to the front (width 3–9 × depth 3–9 × height 4–9 BU) |
| Bundle drawer | 336: MTG bundles on the frame, single or double deep (width 3–9 × depth 5–12 × height 4–9 BU) |
