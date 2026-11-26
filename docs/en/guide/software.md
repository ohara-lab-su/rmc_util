# Software architecture

`rmc_util` is an open-source Python library for RMC_POT input generation, calculation execution, and output analysis. It can be used independently or as part of an RMC–DFT workflow. It was separated from the `RMC_DFT` project.

The package distinguishes **maintained execution logic** from **per-calculation editable parameters**:

- `rmc_util.runners.run_rmc`: packaged execution logic.
- `scripts/rmc.py`: thin entry script calling the packaged runner.
- `scripts/rmc_init.py`: user-edited calculation settings.
- `scripts/config.yml` provides the settings read by `rmc.py`.
- `rmc_util.install` copies the launcher, calculation script, configuration template, and plotting scripts. Use `rmc_util list` to see the available files.
- `rmc_util.util.find_next_log_index`: selects the next available log directory by scanning existing directories, starting numbering at zero.

The `RmcPot` class coordinates execution and pre-/post-processing; `RmcPotDat` and related classes manage inputs; `RmcPotLog`, `RmcPotHst`, `RmcPotFit`, and `RmcPotPpcf` handle result files. See the [API reference](../api/index.md) for the source-derived declarations.

The separate [packmol_util](https://github.com/ohara-lab-su/packmol_util) project can be used to generate initial structures and FNC files; it is not a required component of this package.
