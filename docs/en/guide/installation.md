# Installation and Calculation Directory Setup

## Python package and calculation executable

The Python distribution is named `rmc-util`; its import package is `rmc_util`.

```bash
pip install rmc-util
```

To install from a source checkout, run `pip install .` at the repository root. RMC_UTIL is a Python library for preparing RMC_POT inputs, running calculations, and analyzing results. **This command does not install the RMC_POT calculation executable.** The RMC_POT executable, experimental data, and initial atomic configuration must be prepared separately.

## What `rmc_util install` does

Change to the calculation directory and run:

```bash
rmc_util install
```

This copies the `rmc.py` and `rmc_init.py` scripts bundled with the installed distribution into the **current working directory**. The former launches calculations; the latter is used to edit calculation parameters. `rmc_util install` does not create a virtual environment or install the RMC_POT executable.

By default, an existing file with the same name is skipped. To replace existing scripts explicitly, run:

```bash
rmc_util install --force
```

Because `--force` can overwrite modified copies of `rmc.py` and `rmc_init.py`, do not use it when you need to preserve local settings. Updating the Python package does not automatically update scripts already copied into calculation directories.

## Script discovery and copying

`rmc_util.install.find_installed_scripts()` searches `share/rmc_util/scripts` under the Python installation data directory and the installed distribution's file records. Files with duplicate names are copied only once. An error is raised when no bundled scripts are found.

`rmc_util.install.install_scripts(destination, force=False)` returns the numbers of copied and skipped files. On POSIX systems, it also adds executable permissions to `rmc.py`. The command accepts only `install` or `install --force`.

## Starting a calculation and separating configuration

```bash
python rmc.py
```

The `rmc.py` launcher reads `config.yml`, prepares the log and input objects, applies calculation settings through `run_rmc_init()` in the working directory's `rmc_init.py`, and calls `rmc_util.runners.run_rmc.run_rmc()`. The package contains the iterative execution logic, while `rmc_init.py` holds system-specific parameters.

Both fixed-format and free-format `.dat` files can be edited using the common `RmcPotDat` methods. See [editing input parameters](../tutorial/configure.md), [structural constraints](../tutorial/constraints.md), and [RMC_POT input formats](../reference/rmcpot_input_explained.md).

## Using the Python API

```python
from pathlib import Path
from rmc_util.install import install_scripts

copied, skipped = install_scripts(Path.cwd(), force=False)
```

This API deploys scripts; editing calculation settings and starting an RMC calculation are separate operations. See the [installation API](../api/install.md) for details.
