# API Reference


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

## API Organization


Start with the initialization and input operations of `RmcPotDat`, then consult `RmcPot` for execution and pre-/post-processing, and `run_rmc()` for iterative processing. For result analysis, see the pages for `RmcPotLog`, `RmcPotHst`, `RmcPotFit`, and `RmcPotPpcf`.

