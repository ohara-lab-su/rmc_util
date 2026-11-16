# `rmc_util.rmc_pot_log`

RMC_POT log analysis.

Source: `src/rmc_util/rmc_pot_log.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `RmcPotLog`

Defined at line 19.

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, log_filename: Optional[str]=None) -> None`

Defined at line 21.

Refer to the implementation for detailed semantics, side effects, and return values.

### `load_log(self, log_filename: str=None) -> None`

Defined at line 65.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_cfg_name(self, cfg_name: str) -> None`

Defined at line 99.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_cfg_name(self) -> str`

Defined at line 109.

Refer to the implementation for detailed semantics, side effects, and return values.

### `is_finished(self) -> bool`

Defined at line 521.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_rmc_block(self) -> int`

Defined at line 552.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_rmc_loop(self, block_index: int) -> int`

Defined at line 560.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_generated(self, block: int, loop: int) -> Optional[int]`

Defined at line 584.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_tried(self, block: int, loop: int) -> Optional[int]`

Defined at line 594.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_accepted(self, block: int, loop: int) -> Optional[int]`

Defined at line 604.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_chi2_tot(self, block: int, loop: int) -> Optional[float]`

Defined at line 614.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_chi2_dataset(self, block: int, loop: int) -> Optional[float]`

Defined at line 636.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_rw(self, block: int, loop: int) -> Optional[float]`

Defined at line 657.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_tried_per_generated(self, block: int, loop: int) -> Optional[float]`

Defined at line 663.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_accepted_per_tried(self, block: int, loop: int) -> Optional[float]`

Defined at line 677.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear(self, cfg_name: str) -> None`

Defined at line 695.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_file(self, filename: str) -> bool`

Defined at line 740.

Refer to the implementation for detailed semantics, side effects, and return values.

### `collect_result(self)`

Defined at line 759.

Refer to the implementation for detailed semantics, side effects, and return values.

### `backup_result(self, log_dir: Optional[str]=None, cfg_name: Optional[str]=None)`

Defined at line 762.

Copy RMC log files to the specified directory.

Args:
    log_dir (str): Directory to copy the log files to.
    cfg_name (str): Name of the configuration file.

