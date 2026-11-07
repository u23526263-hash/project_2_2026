# BFB321 classwork: EPQ and ABC classification

Two Python 3 scripts for the BFB321 classwork on Economic Production Quantity (EPQ) and ABC inventory classification. They use the standard library only (`math`). No packages to install.

Filenames follow the brief for David Plumb, u23526263: `david_plumb_epq.py` and `david_plumb_abc.py`.

## Files

| File | Role |
| --- | --- |
| `david_plumb_epq.py` | EPQ calculation, worked example, and the two production-rate checks |
| `david_plumb_abc.py` | ABC classification, worked example, two added SKUs, and 70/90 thresholds |
| `test_wa2.py` | Six unit tests for the formulas, thresholds, sort order, and tier counts |
| `output_epq.txt` | Console output from `david_plumb_epq.py` |
| `output_abc.txt` | Console output from `david_plumb_abc.py` |
| `test_results.txt` | Console output from `python3 test_wa2.py` |

## Run

From this directory:

```bash
python3 david_plumb_epq.py
python3 david_plumb_abc.py
python3 test_wa2.py
```

## Values from the classwork

EPQ inputs: annual demand `D = 12000`, setup cost `S = 50` (Rand per run), holding cost `H = 2` (Rand per unit per year), daily demand `d = 40`, daily production `p = 100`.

```text
EPQ = sqrt(2 * D * S / (H * (1 - d / p)))
```

`p` must be greater than `d`. Runs per year are `D / EPQ`. Run length in days is `EPQ / p`. Maximum inventory is `EPQ * (1 - d / p)`.

Worked-example output:

- Optimal production quantity: 1000.0
- Production runs per year: 12.0
- Length of each run (days): 10.0
- Maximum inventory level: 600.0

With `p = 150`, EPQ is below 1000. With `p = 100000`, EPQ is within 0.2 of plain EOQ `sqrt(2 * D * S / H)` for the same `D`, `S`, and `H`.

ABC annual usage value is `demand * unit cost`. Items are sorted from highest value to lowest. Cumulative percent is `running total / total value * 100`. A tier is A when that percent is `<= 80`, B when it is `<= 95`, and C otherwise. On the eight SKUs in the brief, the counts are 3 A, 3 B, and 2 C. At 70/90 the counts are 3 A, 2 B, and 3 C.

`classify_inventory` returns a new list. The list passed in is not modified. Equal usage values keep their original relative order (`WSH-050` before `CBL-900`).
