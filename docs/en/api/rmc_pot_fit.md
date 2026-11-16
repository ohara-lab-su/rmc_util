# `rmc_util.rmc_pot_fit`

Fitted scattering-profile data.

Source: `src/rmc_util/rmc_pot_fit.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `RmcPotFit`

Defined at line 14.

### `__init__(self, *, fit_name: Optional[str]=None, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Defined at line 20.

Refer to the implementation for detailed semantics, side effects, and return values.

### `read_fit(self, filename: Optional[str]=None) -> Optional[bool]`

Defined at line 59.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_S_calc(self) -> List[float]`

Defined at line 114.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_S_exp(self) -> List[float]`

Defined at line 136.

S_exp(Q) = renormalized F_exp + 1

### `get_S_exp_original(self) -> List[float]`

Defined at line 140.

S_exp_original(Q) = original F_exp + 1

### `as_dict(self) -> Dict[str, List[float]]`

Defined at line 144.

Refer to the implementation for detailed semantics, side effects, and return values.

