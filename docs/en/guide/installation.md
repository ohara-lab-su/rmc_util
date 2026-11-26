# Installation and Calculation Directory Setup

## Python package and calculation executable

The Python distribution is named `rmc-util`; its import package is `rmc_util`.

```bash
pip install rmc-util
```

To install from a source checkout, run `pip install .` at the repository root. RMC_UTIL is a Python library for preparing RMC_POT inputs, running calculations, and analyzing results. **This command does not install the RMC_POT calculation executable.** The RMC_POT executable, experimental data, and initial atomic configuration must be prepared separately.

## What `rmc_util install` does

`rmc_util install`, `rmc_util install all`, and `rmc_util install script` all deploy `rmc.py`, `rmc_init.py`, `config.yml`, and the four plotting scripts to the current directory.

```bash
rmc_util install
rmc_util list
rmc_util install plot_fit.py
rmc_util install config
```

`rmc_util list` shows the available filenames and their purpose. For an individual file, the `.py` and `.yml` extensions are optional. For example, `plot_fit` and `plot_fit.py` select the same file, as do `config` and `config.yml`.

To plot a result, run a command such as `python plot_fit.py aaa` in the directory containing the result file. The argument `aaa` is the result file basename.

Before launching a calculation, set the RMC_POT executable, experimental data, and input file basename in `config.yml`, and edit calculation parameters in `rmc_init.py`.

By default, an existing file with the same name is skipped. To overwrite existing files, run:

```bash
rmc_util install --force
```

`--force` works with both bulk and individual installs and overwrites existing files selected for deployment. Updating the Python package does not automatically update files already copied into calculation directories.

## Script discovery and copying

`rmc_util.install.find_installed_scripts()` searches `share/rmc_util/scripts` under the Python installation data directory and the installed distribution's file records. Files with duplicate names are copied only once. An error is raised when no bundled scripts are found.

`rmc_util.install.install_scripts(destination, force=False, script_name=None)` returns the numbers of copied and skipped files. On POSIX systems, it also adds executable permissions to `rmc.py`.

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

This API deploys the scripts and configuration template. See the [installation API](../api/install.md) for details.
