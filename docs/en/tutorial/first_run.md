# First RMC Calculation

RMC_UTIL runs RMC_POT through `rmc.py` and `rmc_init.py` placed in a calculation directory. Install the RMC_UTIL Python package and prepare the RMC_POT executable separately.

## 1. Install the package

```bash
pip install rmc-util
```

To install from a repository checkout, run `pip install .` at the repository root. The distribution name is `rmc-util`; the Python import name is `rmc_util`.

## 2. Deploy the calculation scripts

Change to the calculation directory and run:

```bash
rmc_util install
```

This places `rmc.py` (launcher) and `rmc_init.py` (editable calculation settings) in the current directory. Existing files are not overwritten by default. `rmc_util install --force` overwrites existing files; back up an edited `rmc_init.py` before using it. See the [installation guide](../guide/installation.md).

## 3. Prepare inputs and the execution environment

Prepare `config.yml`, the initial atomic configuration `.cfg`, experimental data, and the RMC_POT executable for the calculation. When structural constraints are used, also check the corresponding FNC or topology inputs.

The initial-structure preparation code in `rmc.py` is commented out. Running `python rmc.py` does not automatically create an initial configuration. See [input files](../guide/input.md) for `.cfg` and `.dat` formats and the [input-format reference](../reference/rmcpot_input_explained.md) for RMC_POT specifications.

## 4. Configure the calculation in `rmc_init.py`

The `run_rmc_init()` function in `rmc_init.py` configures `RmcPotDat`. Initialize a fixed-format or free-format `.dat` file with `rmc_dat.init()`, then set number density, cutoffs, maximum displacements, and structural constraints through the same Python API.

`prefer_existing=True` specifies that an existing `.dat` file should be preferred. Check its format and parameters when reusing it. See [configuration](configure.md), [input editing](input_editing.md), and [constraint examples](constraints.md) for material-specific examples.

## 5. Run the calculation

```bash
python rmc.py
```

The launcher reads `Config("config.yml")`, constructs `RmcPotLog` and `RmcPotDat`, applies settings through `run_rmc_init()`, and calls `run_rmc()`. The `auto_converge` and `postprocess` arguments control execution independently of the `.dat` file format. See the [execution workflow](workflow.md).

## 6. Inspect the outputs

Evaluate normal termination, attempted and accepted moves, the objective-function history, agreement with experimental data, and satisfaction of structural constraints separately. Normal termination does not establish structural convergence. See [result analysis](analysis.md) and the [output guide](../guide/output.md).
