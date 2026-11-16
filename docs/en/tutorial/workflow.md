# 4. RMC_POT Execution Workflow

The standard execution path is to edit the calculation settings in `rmc_init.py`, deployed by `rmc_util install`, and launch the calculation with `python rmc.py`. The package-level `run_rmc()` requires `config` and receives `rmc_dat` from its caller.

```python
from rmc_util.runners.run_rmc import run_rmc

ok = run_rmc(
    config=config,
    rmc_log=rmc_log,
    rmc_dat=rmc_dat,
    rmc_pot=None,
    auto_converge=False,
    postprocess=True,
)
```

Here, `config`, `rmc_log`, and `rmc_dat` represent objects already initialized by the caller. Creating these objects and configuring the calculation are responsibilities of the distributed scripts. `run_rmc()` performs preprocessing, FNC/cutoff consistency checks, RMC execution, and postprocessing. When `postprocess=True`, postprocessing is also attempted from the `finally` block if execution is interrupted. When `auto_converge=True`, convergence is evaluated using the `.hst` file, and execution continues with another iteration if convergence has not been reached.

[API: runner](../api/runners_run_rmc.md) / [RmcPot](../api/rmc_pot.md) / [RmcPotHst](../api/rmc_pot_hst.md)

## Execution sequence of the installed scripts

`rmc.py` reads settings with `Config("config.yml")` and uses `config.cfg_name` to construct `RmcPotLog` and `RmcPotDat`. It then calls `run_rmc_init(config=config, rmc_dat=rmc_dat, logger=logger)` from `rmc_init.py` to configure the `.dat` input before passing the objects to `run_rmc()`.

The `auto_converge=False` and `postprocess=True` arguments in `rmc.py` control execution. In contrast, `rmc_dat.init(use_free_format=True, prefer_existing=True)` in `rmc_init.py` initializes the input-file format. These settings operate at different stages.

The initial-structure preparation commands in `rmc.py` are commented out. Running `python rmc.py` alone therefore does not generate an initial configuration. Prepare the required `.cfg` file and experimental data before starting the calculation.

`rmc.py` catches `KeyboardInterrupt` and exits with status code 130. This does not indicate convergence.
