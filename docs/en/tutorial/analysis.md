# Analyzing calculation results

RMC_UTIL provides separate readers for different RMC_POT output files. File availability and readability, successful termination, agreement with experimental data, and satisfaction of structural constraints must be assessed separately.

| Class | File | Analysis |
| --- | --- | --- |
| `RmcPotLog` | Log | Calculation blocks, generated/attempted/accepted moves, χ², Rw, and termination status |
| `RmcPotHst` | `.hst` | χ² history, move acceptance rate, and stagnation-based convergence detection |
| `RmcPotFit` | `.fit` | Calculated and experimental profiles and scattering functions |
| `RmcPotPpcf` | `.ppcf` | Radial grid and partial pair-correlation functions for atom-type pairs |
| `RmcPotSnc` | `.snc` | Per-central-atom coordination numbers and Qn distributions for Second Neighbour Constraints |

## χ² history and acceptance rate

`RmcPotHst` reads the selected `.hst` file and analyzes its history. `detect_convergence()` returns the first loop at which both the relative improvement in χ² between successive records and the move acceptance rate remain below their specified thresholds for the required number of consecutive loops. It returns `None` if no such point is detected.

```python
from rmc_util import RmcPotHst

hst = RmcPotHst(cfg_name="sample")
loop = hst.detect_convergence(
    rel_tol=1.0e-2,
    acc_tol=1.0e-3,
    min_consecutive=3,
)
```

This criterion identifies stagnation of the search; it does not establish agreement with experiment or structural validity. Also examine the χ² and Rw trends, residuals in `.fit`, and interatomic distances and coordination environments in `.ppcf`.

## Inspecting Qn distributions with SNC

Supply the `.snc` file path to the reader. `get_qn_counts()` returns a dictionary of central-atom counts by Qn for the selected constraint block. If multiple blocks record identical coordination numbers for the same central atoms, `get_common_qn_counts()` can return their common distribution. It raises `ValueError` when those records differ.

```python
from rmc_util.rmc_pot_snc import RmcPotSnc

snc = RmcPotSnc("sample.snc")
qn_counts = snc.get_qn_counts(constraint_index=0)
```

The physical interpretation of Qn depends on the network and the definition of the constraint. Interpret each distribution with reference to the central-atom and second-neighbor selections of its constraint block.

See the [API reference](../api/index.md) for class methods and the [RMC_POT output-file reference](../reference/rmcpot_output_explained.md) for file formats.
