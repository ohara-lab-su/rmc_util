# `rmc_util.rmc_pot_ppcf`

Partial pair-correlation function data.

Source: `src/rmc_util/rmc_pot_ppcf.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `RmcPotPpcf`

Defined at line 16.

### `__init__(self, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Defined at line 17.

Args:
    cfg_name (str):
    config (Config):
    logger (XLogger):

### `load(self) -> None`

Defined at line 42.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_r(self) -> np.ndarray`

Defined at line 82.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_gij(self) -> np.ndarray`

Defined at line 85.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_single(self, index: int) -> np.ndarray`

Defined at line 88.

Return one partial g_ij(r) selected by its zero-based index.

### `get_labels(self) -> List[str]`

Defined at line 94.

Refer to the implementation for detailed semantics, side effects, and return values.

