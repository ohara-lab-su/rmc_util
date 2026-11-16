# Manual by Task

RMC_UTIL is not the RMC_POT calculation engine itself. It is a Python library for manipulating input files, assisting execution, and reading and analyzing output data. This page maps practical tasks to the relevant classes and documentation. For RMC_POT input specifications, see [Input Files](input.md); for output types, see [Output Files](output.md); and for theoretical background, see [RMC and RMC_POT](overview.md).

## Mapping Tasks to Modules

| Task | Main modules | Documentation and API |
| --- | --- | --- |
| Place editable scripts | `install` | [Installation API](../api/install.md), [README-Based Manual](readme_manual.md) |
| Run RMC_POT | `RmcPot`, `runners.run_rmc` | [RmcPot](../api/rmc_pot.md), [Execution API](../api/runners_run_rmc.md) |
| Read and write `.dat` files | `RmcPotDat`, `RmcPotDatFixed`, `RmcPotDatFree` | [Common API](../api/rmc_pot_dat.md), [Fixed Format](../api/rmc_pot_dat_fixed.md), [Free Format](../api/rmc_pot_dat_free.md) |
| Manipulate FNC constraints | `RmcPotDatFnc` | [FNC API](../api/rmc_pot_dat_fnc.md), [Structural Constraints](constraints.md) |
| Manipulate topology files | `RmcPotDatTop` | [Topology API](../api/rmc_pot_dat_top.md), [Input Files](input.md) |
| Manipulate SNC constraints | `RmcPotSnc` | [SNC API](../api/rmc_pot_snc.md), [Structural Constraints](constraints.md) |
| Read execution logs | `RmcPotLog` | [Log API](../api/rmc_pot_log.md), [Output Files](output.md) |
| Read history files | `RmcPotHst` | [History API](../api/rmc_pot_hst.md), [Output Files](output.md) |
| Read fitting results | `RmcPotFit` | [Fit API](../api/rmc_pot_fit.md), [Output Files](output.md) |
| Read partial pair correlation functions | `RmcPotPpcf` | [PPCF API](../api/rmc_pot_ppcf.md), [Output Files](output.md) |
| Convert atomic configuration formats | `util.cfg2poscar`, `util.poscar2cfg` | [CFG→POSCAR](../api/util_cfg2poscar.md), [POSCAR→CFG](../api/util_poscar2cfg.md) |

## Preparing Inputs

First prepare the atomic configuration `*.cfg`, the simulation parameters `*.dat`, and the experimental data to be fitted. In RMC_POT, the order of atom types in `*.cfg` determines the order of partial correlations; it must therefore agree with the partial-specific cutoffs and scattering coefficients in `*.dat`. Fixed-format and free-format `.dat` files have different syntax. In particular, free-format `#002` and `#003` use different default handling of X-ray scattering coefficients, so changing only the first line does not make them equivalent.

FNC is relevant when molecular connectivity must be preserved, while `*.top` is relevant to topology-based interactions. These input files serve different purposes; structural constraints must not be conflated with potentials. See [RMC_POT Input Files Explained](../reference/rmcpot_input_explained.md) and [Structural Constraints](constraints.md) for their formats.

## Running a Calculation

`RmcPot` and `runners.run_rmc` are entry points for locating execution-related functionality. During RMC_POT iterations, trial atomic moves are evaluated against experimental residuals and the specified structural constraints. A successful launch must therefore be distinguished from convergence to a useful structure. For actual arguments and invocation procedures, consult the [RmcPot API](../api/rmc_pot.md) and [Execution API](../api/runners_run_rmc.md).

## Examining Results

After a run, use logs, history, fitting results, and partial pair correlation functions for different purposes. Logs help inspect execution status and objective values; history records changes during iterations; fitting results allow comparison of calculated and experimental data; and PPCFs support analysis of local structure by atom-type pair. Agreement with experimental data alone does not guarantee a unique structure, so interpret it together with distance, coordination, and bond-angle constraints. See [RMC_POT Output Files Explained](../reference/rmcpot_output_explained.md) for output formats.

## Distinguishing Distribution Names and Execution Environments

`rmc-util` is the distribution package name, while `rmc_util` is the Python import name. Editable scripts placed in a working directory by `rmc_util install` are distinct from the implementation in the installed package. Updating the package does not automatically update scripts already placed in the working directory. See the [README-Based Manual](readme_manual.md) for operational procedures and the [Implementation-Based API Index](../api/implementation_index.md) for the available methods.

*References: RMC_POT user guide 2023.1, I.A, I.K–I.Q, II.C–II.I. Feature names follow the existing RMC_UTIL API documentation.*
