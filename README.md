# rmc_util

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/README.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/README.ja.md)

`rmc_util` is a Python library for working with `RMC_POT` calculations.
It was originally developed as a subpackage of `RMC_DFT` and was later separated into an independent package.

The library provides a programmatic interface for preparing and editing RMC_POT input files, defining structural
constraints, working with FNC and topology data, running and validating RMC_POT calculations, collecting calculation
results, and reading output files such as `.log`, `.hst`, `.fit`, and `.ppcf`.

It can be used on its own for preparing, running, and analyzing RMC_POT calculations. It is particularly useful as a
building block in larger automated workflows, such as RMC-DFT workflows, where RMC parameters need to be changed
programmatically, RMC calculations need to be executed repeatedly, and the resulting structures and convergence
information need to be passed to subsequent calculations.

## Installation

Install the released package from PyPI:

```bash
pip install rmc-util
```

The PyPI project name is `rmc-util`, while the Python package is imported as `rmc_util`.

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst
```

To install a local development checkout, run from the repository root:

```bash
pip install .
```

## What rmc_util handles

### RMC_POT input and execution

`RmcPotDat` is the main interface for RMC_POT `.dat` files. Calculation parameters such as number density, cutoffs,
maximum atomic moves, radial spacing, experimental data range, and calculation/save time can be configured from Python.

Parameters common to the fixed and free formats are handled through the same API. With `prefer_existing=True`, an
existing `.dat` file is detected and loaded in its existing format; the format can be selected when creating a new file.
Free-format-specific structural constraints can also be configured through `RmcPotDat`.

`RmcPot` handles the RMC_POT calculation itself. Its current workflow includes preprocessing, input validation, RMC_POT
execution, result collection/postprocessing, and checks for consistency between FNC constraints and interatomic cutoffs.

### Free-format constraints

The free-format implementation supports programmatic construction and editing of constraints and potential-related
sections, including:

- angular constraints
- coordination constraints
- SNC/Qn constraints
- BVS constraints
- pair potentials
- AENET potential settings

This makes it possible to construct or modify RMC conditions directly from a Python workflow instead of manually
rewriting `.dat` files for each run.

### FNC and topology

`RmcPotDatFnc` provides operations for creating, loading, editing, validating, and writing FNC data, including distance
ranges and atom-neighbour definitions.

`RmcPotDatTop` provides a programmatic interface to RMC_POT topology files, including molecule definitions, atoms,
bonds, angles, dihedrals, exclusions, virtual sites, and topology validation.

### Results and analysis

The output readers can be used independently of the RMC execution layer.

- `RmcPotLog` reads RMC_POT logs and exposes generated/tried/accepted moves, chi-square values, Rw values, and
  calculation blocks/loops. It also provides result collection and backup operations.
- `RmcPotHst` reads `.hst` histories, exposes acceptance and chi-square histories, and provides convergence detection.
- `RmcPotFit` reads `.fit` files and provides calculated and experimental F (Q), background data, and corresponding S
  (Q) values.
- `RmcPotPpcf` reads `.ppcf` files and provides partial pair correlation functions `g_ij(r)`.

## Basic example: preparing an RMC_POT `.dat` file

`RmcPotDat` delays initialization until the file is actually accessed, or it can be initialized explicitly.

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(
    cfg_name="sample",
    auto_write=False,
    use_free_format=True,
)

rmc_dat.init(
    use_free_format=True,
    prefer_existing=True,
)

rmc_dat.set_comment("SiO2 sample", auto_write=False)
rmc_dat.set_density(0.0665715652, auto_write=False)
rmc_dat.set_cutoffs([1.9, 1.1, 1.9], auto_write=False)
rmc_dat.set_maximum_moves([0.01, 0.01], auto_write=False)
rmc_dat.set_r_spacing(0.025, auto_write=False)
rmc_dat.write()
```

If `sample.dat` already exists and `prefer_existing=True`, its fixed/free format is detected and the existing file is
used.

## Example: free-format coordination and Qn constraints

The free-format interface can be used to build structural constraints from Python.

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(
    cfg_name="sample",
    use_free_format=True,
)

rmc_dat.init(
    use_free_format=True,
    prefer_existing=True,
)

rmc_dat.set_element_info(["Si", "O"])

rmc_dat.set_coord_constraint(
    central_type=1,
    neighbors=[
        (2, 1.40, 1.90),
    ],
    subconstraints=[
        (4, 1.0, 0.01),
    ],
    index=0,
)

rmc_dat.set_qn_constraint(
    central_type=1,
    first_neighbor_type=2,
    first_neighbor_minimum=1.45,
    first_neighbor_maximum=1.80,
    second_neighbors=[
        (1, 1.45, 1.80),
    ],
    coordination_number=4,
    fraction=1.0,
    sigma=0.04,
    index=0,
)
```

The same interface is suitable for larger systems with several atom types and multiple coordination or Qn constraints.

## Example: using rmc_util in an automated RMC workflow

A typical higher-level workflow can keep the RMC settings and RMC execution objects alive and use the output readers to
decide what happens next.

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst, RmcPotLog

rmc_dat = RmcPotDat(
    cfg_name="sample",
    use_free_format=True,
)
rmc_dat.init(prefer_existing=True)

rmc_log = RmcPotLog(cfg_name="sample")

rmc = RmcPot(
    rmc_dat=rmc_dat,
    rmc_log=rmc_log,
    cfg_name="sample",
)

if not rmc.preprocess():
    raise RuntimeError("RMC_POT input validation failed.")

if not rmc.check_fnc_cutoff_consistency(cfg_name="sample"):
    raise RuntimeError("FNC and cutoff settings are inconsistent.")

try:
    run_ok = rmc.run()
finally:
    rmc.postprocess(
        cfg_name="sample",
    )

if not run_ok:
    raise RuntimeError("RMC_POT execution failed.")

hst = RmcPotHst(cfg_name="sample")
loop = hst.detect_convergence(
    rel_tol=1.0e-2,
    acc_tol=1.0e-3,
    min_consecutive=2,
)
```

This type of use is useful when RMC_POT is one stage of a larger calculation rather than a standalone calculation. For
example, an RMC-DFT workflow can modify RMC conditions, execute RMC_POT, inspect convergence, archive the results, and
then pass the resulting structure to a DFT stage.

`rmc_util` itself does not provide the DFT calculation layer; it provides the RMC_POT handling required by such
workflows.

## Main modules

| Area              | Module              | Purpose                                                                        |
|-------------------|---------------------|--------------------------------------------------------------------------------|
| RMC execution     | `rmc_pot`           | Preprocess, run, validate, and postprocess RMC_POT calculations                |
| DAT interface     | `rmc_pot_dat`       | Unified API that hides fixed/free-format differences for common RMC parameters |
| Fixed-format DAT  | `rmc_pot_dat_fixed` | Read and edit fixed-format RMC_POT parameters                                  |
| Free-format DAT   | `rmc_pot_dat_free`  | Read/edit free-format parameters, constraints, and potential settings          |
| FNC               | `rmc_pot_dat_fnc`   | Create, edit, and validate FNC files                                           |
| Topology          | `rmc_pot_dat_top`   | Create, edit, and validate topology/ITP-style data                             |
| RMC log           | `rmc_pot_log`       | Parse RMC logs and collect/backup results                                      |
| History           | `rmc_pot_hst`       | Read `.hst` histories and evaluate convergence                                 |
| Fit results       | `rmc_pot_fit`       | Read `.fit` data and obtain F(Q)/S(Q)                                          |
| Pair correlations | `rmc_pot_ppcf`      | Read partial pair correlation functions                                        |

Structure conversion utilities such as CFG/POSCAR conversion are also provided under `rmc_util.util`.

## Documentation

- [Documentation home](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/index.md)
- [RMC and RMC_POT](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/overview.md)
- [Input files](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/input.md)
- [Structural constraints](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/constraints.md)
- [Output and analysis](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/output.md)
- [File format reference](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/reference/index.md)
- [API reference](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/api/index.md)

To build the HTML documentation locally:

```bash
docs/build.sh
```

The generated HTML is written to `docs/_build/html/`.

## Source code

Source code and development history are available on [GitHub](https://github.com/ohara-lab-su/rmc_util).

## Reference

Orsolya Gereben, *RMC_POT user guide for version 2023.1* (2023).
