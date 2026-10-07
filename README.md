# rmc_util

`rmc_util` is a Python library for preparing RMC_POT input files, converting atomic configurations, and reading and analyzing simulation results.

It provides modules for simulation parameters (`.dat`), atomic configurations (`.cfg`), structural constraints, fitting results, histories, and partial pair correlation functions.

## Installation

Run from the repository root:

```bash
pip install .
```

## Modules

| Area | Modules |
| --- | --- |
| RMC_POT operations | `rmc_pot` |
| Parameter files | `rmc_pot_dat`, `rmc_pot_dat_fixed`, `rmc_pot_dat_free` |
| Constraints and topology | `rmc_pot_dat_fnc`, `rmc_pot_dat_top`, `rmc_pot_snc` |
| Results and analysis | `rmc_pot_fit`, `rmc_pot_hst`, `rmc_pot_log`, `rmc_pot_ppcf` |
| Conversions and utilities | `util` |

## Documentation

See the [documentation home](docs/index.md) for RMC concepts, input and output formats, structural constraints, and the Python API. Build HTML with `docs/build.sh`.

## Reference

Orsolya Gereben, *RMC_POT user guide for version 2023.1* (2023).

[日本語](README.ja.md)
