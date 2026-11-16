# Editing RMC_POT inputs

The input classes are split by format and purpose:

- `rmc_pot_dat`: main DAT interface.
- `rmc_pot_dat_fixed`: fixed-format DAT support.
- `rmc_pot_dat_free`: free-format DAT support.
- `rmc_pot_dat_fnc`: FNC constraints.
- `rmc_pot_dat_top`: topology information.

Select the class and methods supported by the actual file format. Use the signatures in the [API reference](../api/index.md), and the detailed [RMC_POT input format explanation](../reference/rmcpot_input_explained.md). Do not mix fixed- and free-format syntax without checking the implementation.
