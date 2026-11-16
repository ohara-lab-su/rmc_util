# Software Architecture and Responsibilities

RMC_UTIL is a Python library for editing RMC_POT input files, controlling execution, and analyzing output. It does not replace the RMC_POT calculation engine.

| Layer | Modules | Responsibility |
|---|---|---|
| Calculation parameters | `rmc_pot_dat.py` | Common API for fixed-format and free-format `.dat` files |
| Format-specific input | `rmc_pot_dat_fixed.py`, `rmc_pot_dat_free.py` | Reading and writing each `.dat` format |
| Additional input | `rmc_pot_dat_fnc.py`, `rmc_pot_dat_top.py`, `rmc_pot_snc.py` | FNC, topology, and structural-constraint operations |
| Execution | `rmc_pot.py`, `runners/run_rmc.py` | Pre-run checks, RMC_POT invocation, result processing, and iterative execution |
| Output analysis | `rmc_pot_log.py`, `rmc_pot_hst.py`, `rmc_pot_fit.py`, `rmc_pot_ppcf.py` | Log, history, fit, and partial-correlation data |
| File conversion | `util/` | CFG, POSCAR, topology conversion, and supporting operations |
| Distributed scripts | `install.py`, `scripts/rmc.py`, `scripts/rmc_init.py` | Deployment of working scripts and execution |

## Separation of the calculation directory and the package

The `rmc.py` file deployed by `rmc_util install` is the launcher, while `rmc_init.py` contains editable calculation settings. The execution implementation resides in the installed `rmc_util.runners.run_rmc` module. Updating the package does not automatically modify a previously deployed `rmc_init.py`.

## `.dat` formats and initialization

Constructing `RmcPotDat` alone does not read a `.dat` file. Use `init(prefer_existing=True)` to prioritize an existing file; for new files, select the format using `use_free_format`. Distinguish the format of an existing file from the format requested for a new file.

## Related pages

[Basic usage](software.md) / [Tutorial](../tutorial/index.md) / [API reference](../api/index.md)
