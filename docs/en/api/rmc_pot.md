# `rmc_util.rmc_pot`

RMC_POT execution and preprocessing/postprocessing.

Source: `src/rmc_util/rmc_pot.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `RmcPot`

Defined at line 28.

Utility class for managing and running local RMC commands.
And parsing configuration files.

### `__init__(self, *, rmc_log: Optional[RmcPotLog]=None, rmc_dat: Optional[RmcPotDat]=None, config: Optional[Config]=None, cfg_name: Optional[str]=None, use_free_format: bool=False, logger: Optional[XLogger]=None) -> None`

Defined at line 34.

Refer to the implementation for detailed semantics, side effects, and return values.

### `rmc_dat(self)`

Defined at line 114.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_cfg_name(self, cfg_name: str)`

Defined at line 117.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_tag(self, tag_name: str, *args) -> None`

Defined at line 132.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_tag(self, tag_name: str, *args)`

Defined at line 148.

Refer to the implementation for detailed semantics, side effects, and return values.

### `init(self, cfg_name: str)`

Defined at line 167.

Refer to the implementation for detailed semantics, side effects, and return values.

### `preprocess(self) -> bool`

Defined at line 181.

Refer to the implementation for detailed semantics, side effects, and return values.

### `postprocess(self, log_dir: Optional[str]=None, cfg_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None) -> bool`

Defined at line 261.

Refer to the implementation for detailed semantics, side effects, and return values.

### `check_fnc_cutoff_consistency(self, cfg_name: Optional[str]=None) -> bool`

Defined at line 342.

Refer to the implementation for detailed semantics, side effects, and return values.

### `run(self, cfg_name: Optional[str]=None, blocking: Optional[bool]=True, save_stdout: Optional[bool]=True) -> bool`

Defined at line 729.

Refer to the implementation for detailed semantics, side effects, and return values.

### `ensure_vasp5_format(poscar_name: str, element_info: Optional[str]=None, logger: XLogger=XLogger()) -> bool`

Defined at line 839.

Refer to the implementation for detailed semantics, side effects, and return values.

### `cfg2poscar(self, cfg_name: Optional[str]=None, vasp_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None) -> bool`

Defined at line 863.

Refer to the implementation for detailed semantics, side effects, and return values.

