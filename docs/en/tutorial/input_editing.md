# Editing RMC_POT input files

`RmcPotDat` provides a common Python interface for fixed-format and free-format `.dat` files. The same setters are used for parameters supported by both formats; the output format is selected during initialization.

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(cfg_name="sample", auto_write=False)
rmc_dat.init(use_free_format=True, prefer_existing=True)
rmc_dat.set_density(0.0665715652)
rmc_dat.set_cutoffs([2.40, 1.25, 2.10])
rmc_dat.set_maximum_moves([0.01, 0.01])
rmc_dat.write()
```

For a new fixed-format input, specify `use_free_format=False`. When `prefer_existing=True` and a `.dat` file already exists, its detected format takes precedence over `use_free_format`. Confirm the existing file before choosing an initialization mode.

The format-specific implementations are organized in `rmc_pot_dat_fixed` and `rmc_pot_dat_free`, but ordinary input editing should use the common `RmcPotDat` interface. FNC and topology settings are handled by the corresponding support modules. Free-format sections such as coordination and SNC constraints require the free-format functionality; they are not interchangeable with fixed-format text records.

For complete parameter examples, including different atom-type counts and structural constraints, see [Calculation parameters](configure.md) and [Structural constraints](constraints.md). The [API reference](../api/rmc_pot_dat.md) documents the Python interface, while the [RMC_POT input reference](../reference/rmcpot_input_explained.md) describes the file specification.
