# Manual by Task

This page organizes the features described in `README.ja.md` according to user tasks. For concrete usage examples, see [README Code Examples](../tutorial/readme_examples.md); for method names, see the [Implementation-Based API Index](../api/implementation_index.md).

| Purpose | Main modules | Related page |
| --- | --- | --- |
| Installation and placement of editable scripts | `install` | [Installation](installation.md) |
| Running RMC_POT | `RmcPot`, `runners.run_rmc` | [Execution Workflow](../tutorial/workflow.md) |
| Reading/writing `.dat` files and selecting formats | `RmcPotDat`, `RmcPotDatFixed`, `RmcPotDatFree` | [Configuration](../tutorial/configure.md) |
| Editing FNC constraints | `RmcPotDatFnc` | [Structural Constraints](../tutorial/constraints.md) |
| Editing topology | `RmcPotDatTop` | [Input](input.md) |
| SNC / Qn constraints | `RmcPotSnc` | [Structural Constraints](../tutorial/constraints.md) |
| Logs and convergence history | `RmcPotLog`, `RmcPotHst` | [Result Analysis](../tutorial/analysis.md) |
| Fits and partial pair distribution functions | `RmcPotFit`, `RmcPotPpcf` | [Result Analysis](../tutorial/analysis.md) |
| Structure format conversion | `util.cfg2poscar`, `util.poscar2cfg`, etc. | [API Reference](../api/index.md) |

## Distinctions in Usage

`rmc-util` is the PyPI distribution name, whereas `rmc_util` is the Python import name. The editable scripts placed in the working directory by `rmc_util install` are distinct from the execution code within the package. Previously installed scripts are not automatically updated when the package is updated. For details, see the [README-Based Manual](readme_manual.md).

The existing explanations of RMC theory and RMC_POT file formats are retained in [RMC Method and RMC_POT Explanations](../reference/index.md).
