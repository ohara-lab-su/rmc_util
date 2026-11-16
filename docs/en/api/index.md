# API Reference

The following public classes, functions, and methods were extracted from the provided Python source code. Default argument values follow the declarations in the source code. Internal methods whose names begin with `_` are generally excluded.

```{toctree}
:maxdepth: 2

implementation_index

config
install
rmc_pot
rmc_pot_dat
rmc_pot_dat_fixed
rmc_pot_dat_free
rmc_pot_dat_fnc
rmc_pot_dat_top
rmc_pot_fit
rmc_pot_hst
rmc_pot_log
rmc_pot_ppcf
rmc_pot_snc
runners_run_rmc
util_zeolite
util_poscar2cfg
util_cfg2poscar
util_ensure_vasp5_format
util_find_next_log_index
util_gromacs_top_to_rmc_top
```

## How to Read the API Reference

Each module page includes signatures and docstrings from the source code, together with lists of public methods for each class and their definition line numbers. The line numbers refer to the source files provided for this documentation and may change in future releases.

Start with the initialization and input operations of `RmcPotDat`, then consult `RmcPot` for execution and pre-/post-processing, and `run_rmc()` for iterative processing. For result analysis, see the pages for `RmcPotLog`, `RmcPotHst`, `RmcPotFit`, and `RmcPotPpcf`.

**Note:** Because `scripts/rmc.py`, `scripts/rmc_init.py`, and the package's `__init__.py` were not provided, their function specifications are not included in this reference.
