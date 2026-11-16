# `rmc_util.rmc_pot_hst`

Histogram output analysis.

Source: `src/rmc_util/rmc_pot_hst.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `RmcPotHst`

Defined at line 39.

### `__init__(self, hst_name: Optional[str]=None, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None) -> None`

Defined at line 41.

Refer to the implementation for detailed semantics, side effects, and return values.

### `read_chi2(self) -> Tuple[List[int], List[float]]`

Defined at line 202.

Refer to the implementation for detailed semantics, side effects, and return values.

### `detect_convergence(self, rel_tol: float=0.01, acc_tol: float=0.001, min_consecutive: int=3) -> Optional[int]`

Defined at line 231.

Refer to the implementation for detailed semantics, side effects, and return values.

### `detect_convergence_set1(self, rel_tol: float=0.01, acc_tol: float=0.001, min_consecutive: int=2) -> Optional[int]`

Defined at line 327.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_rmc_loops(self) -> int`

Defined at line 368.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_generated(self, loop_index: Optional[int]=None) -> Union[int, List[int]]`

Defined at line 382.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_tried(self, loop_index: Optional[int]=None) -> Union[int, List[int]]`

Defined at line 413.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_accepted(self, loop_index: Optional[int]=None) -> Union[int, List[int]]`

Defined at line 441.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_time(self, loop_index: Optional[int]=None) -> Union[int, List[int]]`

Defined at line 469.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_tried_per_generated(self, loop_index: Optional[int]=None) -> Union[float, List[float]]`

Defined at line 497.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_accepted_per_tried(self, loop_index: Optional[int]=None) -> Union[float, List[float]]`

Defined at line 525.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_chi2_tot(self, loop_index: Optional[int]=None) -> Union[float, List[float]]`

Defined at line 553.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_chi2_set1(self, loop_index: Optional[int]=None) -> Union[float, List[float]]`

Defined at line 575.

Refer to the implementation for detailed semantics, side effects, and return values.

