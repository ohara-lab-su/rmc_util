# Calculation workflow

1. Install `rmc-util` and deploy the working scripts with `rmc_util install`.
2. Edit `rmc_init.py` for the intended material and calculation.
3. Prepare the structure (`.cfg`), RMC_POT settings (`.dat`), experimental profiles, and any required FNC or topology files.
4. Run `python rmc.py` in the calculation directory.
5. Inspect the logs and output files. Use the result-analysis classes when integrating into Python workflows.

`RmcPot.preprocess()` checks required inputs; it does not generate an initial structure automatically. `RmcPot.postprocess()` includes collection/backup and CFG-to-POSCAR conversion for subsequent calculations.

See [the first-run tutorial](../tutorial/first_run.md).
