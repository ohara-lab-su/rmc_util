# rmc_util

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/README.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/README.ja.md)

[![GitHub](https://img.shields.io/badge/GitHub-ohara--lab--su%2Frmc_util-181717?logo=github)](https://github.com/ohara-lab-su/rmc_util/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Documentation-222222?logo=githubpages&logoColor=white)](https://ohara-lab-su.github.io/rmc_util/en/)
[![Ohara Lab](https://img.shields.io/badge/Ohara%20Lab-Home-4B5563?logo=homeassistant&logoColor=white)](https://ohara-lab-su.github.io/)

`rmc_util` is an **open-source library for preparing RMC_POT input, running calculations, and analyzing results from Python**. While using the existing RMC_POT calculation engine, it enables programmatic automation of input conditions, editing structural constraints, iterative calculations, and convergence evaluation.

Its scope extends from handling `.dat`, FNC, and topology files to analyzing `.log`, `.hst`, `.fit`, and `.ppcf` files. It can be used both for research employing RMC_POT alone and for computational workflows such as RMC-DFT. The package was originally separated from `RMC_DFT`.

**For generating initial structures, the separately published [`packmol_util`](https://github.com/ohara-lab-su/packmol_util) can also be used.** In addition to generating amorphous structures from composition, density, and atom count, it supports generating FNC files for RMC_POT. Both packages can be used independently.

### Installation

Install the package published on PyPI with the following command:

```bash
pip install rmc-util
```

The project name on PyPI is `rmc-util`, whereas the package name used from Python is `rmc_util`.

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst
```

To use a development version cloned locally, run the following in the repository root:

```bash
pip install .
```

### Installing the Launcher and Configuration Files

After installing `rmc-util`, copy the bundled `rmc.py`, `rmc_init.py`, and `config.yml` into the current directory.

```bash
rmc_util install
```

Existing files with the same names are skipped rather than overwritten. To explicitly overwrite them, run:

```bash
rmc_util install --force
```

Set the executable and experimental data in `config.yml` and edit calculation parameters in `rmc_init.py`. Updating the package does not automatically update files already installed in working directories.

### Separation of Execution Processing and Calculation Conditions

The RMC execution system separates **execution processing maintained by the package** from **parameters edited for each calculation**. The execution logic remains in the package, while working directories contain the launcher and calculation settings.

- `src/rmc_util/runners/run_rmc.py`: RMC execution processing maintained within the package. It is not copied into individual working directories.
- `scripts/rmc.py`: A script that only launches `rmc_util.runners.run_rmc`. It can be executed with `python rmc.py`.
- `scripts/rmc_init.py`: Initialization and parameter script for editing calculation conditions. It is deployed to working directories with `rmc_util install` and calls the package-side runner.
- `scripts/config.yml` is the configuration template that `rmc.py` reads at startup.
- `src/rmc_util/install.py` copies the bundled files into the working directory.
- `next_log_dir_name()` in `find_next_log_index.py`: Searches existing log directories each time to determine the next name. Numbering **starts at 0**, and there is no centrally managed counter. This naming convention associates calculation conditions and execution scripts with their saved results.

The repository-root `scripts/` directory holds editable files for distribution and has a different role from `runners/` inside the Python package. Changes to the runner take effect when the package is updated.

Integration workflows such as `rmc_dft` can call the execution functionality maintained by the package. Standalone RMC execution is also supported.

### Scope of rmc_util

#### RMC_POT Input Conditions and Execution

`RmcPotDat` is the central interface for handling RMC_POT `.dat` files. It allows calculation conditions such as number density, cutoff, maximum atomic displacement, r spacing, experimental data range, calculation time, and save interval to be configured from Python.

Conditions shared by fixed and free formats are handled through the same API. When using an existing `.dat` file with `prefer_existing=True`, its format is detected and the file is read; when creating a new file, the format can be specified. Structural constraints specific to the free format can also be configured through `RmcPotDat`.

`RmcPot` handles RMC_POT execution. The current implementation supports preprocessing, input validation, running RMC_POT, collecting and archiving results after calculation, and checking consistency between FNC distance constraints and interspecies cutoffs.

#### Free-Format Structural Constraints

In free-format `.dat` files, the following constraints and potential-related settings can be created and edited from Python:

- angle constraint
- coordination constraint
- SNC / Qn constraint
- BVS constraint
- pair potential
- AENET potential

This allows calculation conditions to be assembled or changed by higher-level scripts instead of manually rewriting `.dat` files for each RMC run.

#### FNC and Topology

`RmcPotDatFnc` handles creating, reading, editing, validating, and writing FNC data. Distance ranges for each constraint type, neighbors of each atom, and atom pairs can be manipulated from Python.

`RmcPotDatTop` provides functionality for constructing and editing RMC_POT topology from Python. It handles molecules, atoms, bonds, angles, dihedrals, exclusions, virtual sites, and other data, and can validate topology.

#### Calculation Results and Analysis

Output files can also be read independently of the RMC_POT execution functionality.

- `RmcPotLog`: Reads RMC_POT logs and obtains generated / tried / accepted counts, χ², Rw, RMC blocks / loops, and other information. It also handles collecting and backing up calculation results.
- `RmcPotHst`: Reads `.hst` histories, retrieves acceptance and χ² histories, and determines convergence.
- `RmcPotFit`: Reads `.fit` files and obtains calculated and experimental F(Q), background, and corresponding S(Q).
- `RmcPotPpcf`: Reads `.ppcf` files and obtains partial pair distribution functions `g_ij(r)`.

### Basic Example: Configuring an RMC_POT `.dat` File

`RmcPotDat` can defer initialization until necessary, but it can also be initialized explicitly with `init()`.

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

If `sample.dat` already exists and `prefer_existing=True`, its fixed or free format is detected automatically and the existing file is used.

### Example: Free-Format Coordination / Qn Constraints

In the free format, structural constraints can be configured directly from Python.

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

Multiple coordination constraints and Qn constraints can also be specified for systems containing multiple atomic species.

### Example: Using It from an RMC Workflow

A higher-level workflow can retain RMC configuration and execution objects, read output, and determine subsequent processing.

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

This approach allows RMC_POT to be treated not only as an independent calculation but also as one stage of a larger computational workflow. For example, in RMC-DFT, it can be used to change RMC conditions, execute RMC_POT, check convergence, archive results, and pass the resulting structure to the DFT stage.

`rmc_util` itself does not provide DFT calculations; it handles the RMC_POT side required by such workflows.

### Main Modules

| Area | Module | Description |
|---|---|---|
| RMC execution | `rmc_pot` | RMC_POT preprocessing, execution, validation, and postprocessing |
| Common DAT | `rmc_pot_dat` | Abstracts fixed/free differences and handles common RMC conditions through one API |
| Fixed-format DAT | `rmc_pot_dat_fixed` | Reads and writes fixed-format RMC_POT parameters |
| Free-format DAT | `rmc_pot_dat_free` | Reads and writes free-format parameters, structural constraints, and potential settings |
| FNC | `rmc_pot_dat_fnc` | Creates, edits, and validates FNC |
| topology | `rmc_pot_dat_top` | Creates, edits, and validates topology / ITP-format data |
| RMC log | `rmc_pot_log` | Analyzes RMC logs and collects and backs up results |
| history | `rmc_pot_hst` | Analyzes `.hst` and determines convergence |
| fit | `rmc_pot_fit` | Reads `.fit` and obtains F(Q) / S(Q) |
| PPCF | `rmc_pot_ppcf` | Reads partial pair distribution functions |

Structural conversion and auxiliary functionality, including CFG / POSCAR conversion, are included in `rmc_util.util`.

### Documentation

- [Documentation Home](https://ohara-lab-su.github.io/rmc_util/en/)
- [RMC Method and RMC_POT](https://ohara-lab-su.github.io/rmc_util/en/guide/overview.html)
- [Input Files](https://ohara-lab-su.github.io/rmc_util/en/guide/input.html)
- [Structural Constraints](https://ohara-lab-su.github.io/rmc_util/en/guide/constraints.html)
- [Output and Analysis](https://ohara-lab-su.github.io/rmc_util/en/guide/output.html)
- [Detailed File Formats](https://ohara-lab-su.github.io/rmc_util/en/reference/index.html)
- [API Reference](https://ohara-lab-su.github.io/rmc_util/en/api/index.html)

To build the documentation as HTML locally, run:

```bash
docs/build.sh
```

HTML is output to `docs/_build/html/`.

### Source Code

The source code and development history are published on [GitHub](https://github.com/ohara-lab-su/rmc_util).

### References

Orsolya Gereben, *RMC_POT user guide for version 2023.1* (2023).

#### Running RMC

Use `rmc_util install` to deploy all three files, edit `config.yml` and `rmc_init.py` for the calculation, and then execute in the same working directory.

```bash
rmc_util install
python rmc.py
```

`rmc.py` only executes `rmc_util.runners.run_rmc` and does not duplicate the execution processing. This assumes that the runner is executable as `__main__`.

`run_rmc()` requires `config` as an argument and receives the objects needed for execution, including `rmc_dat`, from the caller. In `scripts/rmc.py`, `Config("config.yml")`, `RmcPotLog`, and `RmcPotDat` are created; after configuring conditions using `rmc_init.py`, it calls `run_rmc(config=..., rmc_log=..., rmc_dat=..., rmc_pot=None, auto_converge=False, postprocess=True, msg=None, logger=...)`. The runner does not retain the old standalone script's `if __name__ == "__main__":` block.

If this software is useful as a reference for research or contributes to research results, we would appreciate an acknowledgment of “Ohara Lab, Shimane University” in publications or other research outputs.
