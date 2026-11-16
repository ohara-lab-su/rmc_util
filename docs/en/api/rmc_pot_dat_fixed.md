# `rmc_util.rmc_pot_dat_fixed`

Fixed-format DAT input handling.

Source: `src/rmc_util/rmc_pot_dat_fixed.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `RmcPotDatFixed`

Defined at line 67.

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, auto_write: bool=True) -> None`

Defined at line 82.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_cfg_name(self, cfg_name: str) -> None`

Defined at line 184.

Refer to the implementation for detailed semantics, side effects, and return values.

### `create_dat_file(self, basename: str) -> bool`

Defined at line 193.

Refer to the implementation for detailed semantics, side effects, and return values.

### `load(self) -> bool`

Defined at line 260.

Refer to the implementation for detailed semantics, side effects, and return values.

### `write(self, out_name: Optional[str]=None) -> None`

Defined at line 292.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_line(self, line_no_1based: int) -> str`

Defined at line 311.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_line(self, line_no_1based: int, value: Union[str, int, float, Sequence[Union[int, float]], bool], *, auto_write: Optional[bool]=None) -> None`

Defined at line 325.

Refer to the implementation for detailed semantics, side effects, and return values.

### `insert_line(self, line_no_1based: int, value: Union[str, int, float, Sequence[Union[int, float]], bool], *, comment: str='', auto_write: Optional[bool]=None) -> None`

Defined at line 355.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_line(self, line_no_1based: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 379.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_element_info(self, element_info: Sequence[str], *, auto_write: Optional[bool]=None) -> bool`

Defined at line 444.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_comment(self) -> str`

Defined at line 460.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_comment(self, comment: str, *, auto_write: Optional[bool]=True) -> None`

Defined at line 464.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_density(self) -> float`

Defined at line 475.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_density(self, rho: Union[int, float], *, auto_write: Optional[bool]=True) -> None`

Defined at line 500.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_cutoffs(self) -> List[Union[int, float]]`

Defined at line 511.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_cutoffs(self, values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=True) -> None`

Defined at line 530.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_max_moves(self) -> Tuple[float, float]`

Defined at line 613.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_maximum_moves(self, values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=True) -> None`

Defined at line 631.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_r_spacing(self) -> float`

Defined at line 660.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_r_spacing(self, dr: Union[int, float], *, auto_write: Optional[bool]=True) -> None`

Defined at line 688.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_moveout_option(self) -> bool`

Defined at line 699.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_moveout_option(self, use_moveout: bool, *, auto_write: Optional[bool]=True) -> None`

Defined at line 745.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_config_to_collect(self) -> int`

Defined at line 781.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_num_config_to_collect(self, num_config: int, *, auto_write: Optional[bool]=True) -> None`

Defined at line 822.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_print_interval(self) -> int`

Defined at line 860.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_print_interval(self, interval_step: int, *, auto_write: Optional[bool]=True) -> None`

Defined at line 896.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_time_and_save(self) -> Tuple[float, int]`

Defined at line 927.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_time_and_save(self, time_limit_min: float, save_interval_step: float, *, auto_write: Optional[bool]=True) -> None`

Defined at line 964.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_data_flags(self) -> Tuple[int, int, int, int]`

Defined at line 1010.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_data_flags(self, flags: Sequence[int], *, auto_write: Optional[bool]=True) -> None`

Defined at line 1051.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_exp_filename(self) -> str`

Defined at line 1098.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_exp_filename(self, path: Union[str, Path], *, auto_write: Optional[bool]=None) -> None`

Defined at line 1160.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_exp_range(self) -> Tuple[int, int]`

Defined at line 1193.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_exp_range(self, start: int, end: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1239.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_scale_factor(self) -> float`

Defined at line 1270.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_scale_factor(self, value: float, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1284.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_sigma_factor(self) -> float`

Defined at line 1299.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_sigma_factor(self, sigma: float, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1327.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_15(self) -> bool`

Defined at line 1343.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_15(self, value: bool, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1356.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_16(self) -> bool`

Defined at line 1365.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_16(self, value: bool, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1378.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_17(self) -> bool`

Defined at line 1387.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_17(self, value: bool, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1400.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_18(self) -> bool`

Defined at line 1409.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_18(self, value: bool, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1422.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_angle_constraint_count(self) -> int`

Defined at line 1431.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_angle_constraint_count(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1444.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_coord_constraint_count(self) -> int`

Defined at line 1453.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1466.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_avg_coord_constraint_count(self) -> int`

Defined at line 1475.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_avg_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1488.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_potential_flag(self) -> int`

Defined at line 1497.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_potential_flag(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1510.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_fnc_switch(self) -> int`

Defined at line 1519.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_fnc_options(self) -> List[str]`

Defined at line 1535.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_fnc_switch(self, value: Union[bool, int], *, opt: Optional[Union[str, Sequence[str]]]=None, keep_existing_opt: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 1580.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_fnc_distance_ranges(self, fnc_name: Optional[str]=None) -> Dict[int, Tuple[float, float]]`

Defined at line 1654.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_fnc_distance_ranges(self, ranges: Dict[int, Tuple[float, float]], fnc_name: Optional[str]=None) -> None`

Defined at line 1705.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_initial_bin_shift(self) -> int`

Defined at line 1776.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_initial_bin_shift(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1789.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_xmax_used(self) -> float`

Defined at line 1798.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_xmax_used(self, value: float, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1811.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_atoms_per_move(self) -> int`

Defined at line 1820.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_num_atoms_per_move(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1843.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_history_buffer_size(self) -> int`

Defined at line 1853.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_history_buffer_size(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1866.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_display_update_interval(self) -> int`

Defined at line 1875.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_display_update_interval(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1884.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_custom_move_flag(self) -> int`

Defined at line 1893.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_custom_move_flag(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1902.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_load_histogram_flag(self) -> int`

Defined at line 1911.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_load_histogram_flag(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1920.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_max_atoms_per_cell(self) -> int`

Defined at line 1929.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_max_atoms_per_cell(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1938.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_swap_settings(self) -> Tuple[int, int]`

Defined at line 1947.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_swap_settings(self, fraction: int, allow_flag: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1959.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_thread_count(self) -> int`

Defined at line 1969.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_thread_count(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1978.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_local_invariance(self, line_no_1based: int) -> Tuple[int, List[float], int, List[float]]`

Defined at line 1987.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_local_invariance(self, line_no_1based: int, sigma_values: Sequence[Union[int, float]], ratios: Sequence[Union[int, float]], *, mode: int=1, auto_write: Optional[bool]=None) -> None`

Defined at line 2002.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_non_periodic(self, line_no_1based: int) -> Tuple[float, bool]`

Defined at line 2026.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_non_periodic(self, line_no_1based: int, sample_radius: Union[int, float], *, recentre: bool=False, auto_write: Optional[bool]=None) -> None`

Defined at line 2040.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_vibrational_amplitudes(self, line_no_1based: int) -> List[float]`

Defined at line 2057.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_vibrational_amplitudes(self, line_no_1based: int, sigma_values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 2064.

Refer to the implementation for detailed semantics, side effects, and return values.

## `main() -> None`

Defined at line 2103.

Refer to the implementation for detailed semantics, side effects, and return values.

