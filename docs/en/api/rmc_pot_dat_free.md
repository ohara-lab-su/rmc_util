# `rmc_util.rmc_pot_dat_free`

Free-format DAT input handling.

Source: `src/rmc_util/rmc_pot_dat_free.py`.

This module provides section- and keyword-based access to free-format RMC_POT DAT files.

## Class `RmcPotDatFree`

`RmcPotDatFree` reads and writes free-format RMC_POT `*.dat` files using `[ SECTION ]` and `KEY = VALUE` entries. Settings can be changed through the standard getters and setters or through the free-format-specific `get()`, `set()`, and `add()` operations.

The RMC_POT executable must support the required advanced geometric constraints when those constraints are used; the corresponding build options are described in the RMC_POT manual.

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, auto_write: bool=True, version: str='#003')`

Initialize the free-format input editor.

- `config`: Overall configuration; a new `Config` is used when omitted.
- `logger`: `XLogger` instance; a new logger is created when omitted.
- `cfg_name`: File basename without `.dat`; defaults to `config.cfg_name`.
- `auto_write`: Save the DAT file after each setter by default.
- `version`: Format marker for newly created files, normally `#002` or `#003`.

If `<cfg_name>.dat` already exists, its format marker is preserved. The `version` argument applies when creating a new file. Set `auto_write=False` to apply multiple changes before writing the result.

### `create_dat_file(self, basename: str)`

Create a free-format DAT file with initial settings in `[ GENERAL ]`. The argument is the basename without `.dat`. Returns `True` when a new file is created and `False` when the file already exists; existing files are not overwritten. The initial configuration uses `FNC-TYPE = NONE` and does not create a `[ BPOT ]` section.

### `load(self)`

Read the DAT file selected by `cfg_name`. Returns `True` when the file is loaded and `False` when it does not exist. Raises `ValueError` for an empty file, invalid format marker, or a key/value entry outside a section. Repeated keys are retained as ordered lists; continuation lines are joined to the preceding value.

### `write(self, out_name: Optional[str]=None)`

Write the current free-format data to `<out_name>.dat`, or to the current `cfg_name` when omitted. Section order, key order, and the order of repeated values are preserved.

### `set(self, section: str, key: str, value: Any, index: int=0)`

Replace the value of `key` in the zero-based occurrence `index` of `section`. Missing section occurrences are created as needed. Existing values for the key are replaced.

### `add(self, section: str, key: str, value: Any, index: int=0)`

Append a value to `key` in the selected occurrence of `section`, retaining existing values and their order.

### `get(self, section: str, key: str, index: int=0, default: Optional[str]=None)`

Return the first value for the specified key and section occurrence. Return `default` when the section or key does not exist.

### `get_all(self, section: str, key: str, index: int=0)`

Return all values for the key in insertion order. Return an empty list when no matching entry exists.

### `initialize_sections(self, section: str, *, auto_write: Optional[bool]=None)`

Remove all occurrences of the named section without creating an empty replacement. This is useful before rebuilding repeated `[ SNC ]`, `[ EXP ]`, or `[ COS ]` sections. `auto_write=None` uses the instance-level setting.

### `initialize_qn_constraints(self, *, auto_write: Optional[bool]=None)`

Compatibility method for older Qn/SNC initialization code. Delegates removal to `clear_qn_constraints()`; new code can call that method directly.

### `add_section(self, section: str)`

Append an empty section and return its zero-based occurrence index. This low-level operation does not write the file automatically. For normal constraint definitions, use the corresponding high-level constraint setter.

### `remove_section(self, section: str, index: int=0)`

Remove the selected occurrence of a section. Raises `IndexError` if the specified occurrence does not exist.

### `remove(self, section: str, key: str, index: int=0)`

Remove a key and all its values from the selected section. Does nothing if the section or key does not exist.

### `section_count(self, section: str)`

Return the number of occurrences of the specified section.

### `set_cfg_name(self, cfg_name: str)`

Change the DAT file basename (without `.dat`) and update the corresponding `Config.cfg_name` value.

### `set_element_info(self, element_info: Sequence[str], *, auto_write: Optional[bool]=None) -> None`

Defined at line 728.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_comment(self) -> str`

Defined at line 827.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_comment(self, comment: str, *, auto_write: Optional[bool]=True) -> None`

Defined at line 831.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_density(self) -> Union[float, bool]`

Defined at line 844.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_density(self, rho: Union[int, float], *, auto_write: Optional[bool]=True) -> None`

Defined at line 858.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_cutoffs(self) -> List[Union[int, float, str]]`

Defined at line 871.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_cutoffs(self, values: Union[str, Sequence[Union[int, float]]], *, auto_write: Optional[bool]=True) -> None`

Defined at line 893.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_max_moves(self) -> List[float]`

Defined at line 914.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_maximum_moves(self, values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=True) -> None`

Defined at line 925.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_r_spacing(self) -> float`

Defined at line 938.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_r_spacing(self, dr: Union[int, float], *, auto_write: Optional[bool]=True) -> None`

Defined at line 943.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_moveout_option(self) -> bool`

Defined at line 952.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_moveout_option(self, use_moveout: bool, *, auto_write: Optional[bool]=True) -> None`

Defined at line 957.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_config_to_collect(self) -> int`

Defined at line 966.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_num_config_to_collect(self, num_config: int, *, auto_write: Optional[bool]=True) -> None`

Defined at line 971.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_print_interval(self) -> int`

Defined at line 982.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_print_interval(self, interval_step: int, *, auto_write: Optional[bool]=True) -> None`

Defined at line 987.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_time_and_save(self) -> Tuple[float, int]`

Defined at line 998.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_time_and_save(self, time_limit_min: float, save_interval_step: float, *, auto_write: Optional[bool]=True) -> None`

Defined at line 1004.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_data_flags(self) -> Tuple[int, int, int, int]`

Defined at line 1021.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_data_flags(self, flags: Sequence[int], *, auto_write: Optional[bool]=True) -> bool`

Defined at line 1028.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_exp_filename(self) -> Union[str, bool]`

Defined at line 1071.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_exp_filename(self, path: Union[str, Path], *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1112.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_exp_range(self) -> Union[Tuple[int, int], bool]`

Defined at line 1127.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_exp_range(self, start: int, end: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1151.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_scale_factor(self) -> Union[float, bool]`

Defined at line 1170.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_scale_factor(self, value: float, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1184.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_sigma_factor(self) -> Union[float, bool]`

Defined at line 1197.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_sigma_factor(self, sigma: float, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1211.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_15(self) -> bool`

Defined at line 1261.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_15(self, value: bool, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1269.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_16(self) -> bool`

Defined at line 1280.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_16(self, value: bool, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1284.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_17(self) -> bool`

Defined at line 1288.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_17(self, value: bool, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1292.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_flag_18(self) -> bool`

Defined at line 1296.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_flag_18(self, value: bool, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1300.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_angle_constraint_count(self) -> int`

Defined at line 1304.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_angle_constraint_count(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1308.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_coord_constraint_count(self) -> int`

Defined at line 1335.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1339.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_avg_coord_constraint_count(self) -> int`

Defined at line 1366.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_avg_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1370.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_potential_flag(self) -> int`

Defined at line 1399.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_potential_flag(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1406.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_fnc_switch(self) -> int`

Defined at line 1435.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_fnc_options(self) -> List[str]`

Defined at line 1471.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_fnc_switch(self, value: Union[bool, int], *, opt: Optional[Union[str, Sequence[str]]]=None, keep_existing_opt: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 1534.

Refer to the implementation for detailed semantics, side effects, and return values.

### `validate_mode_configuration(self, *, check_input_files: bool=False) -> None`

Defined at line 1614.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_fnc_distance_ranges(self, fnc_name: Optional[str]=None) -> Dict[int, Tuple[float, float]]`

Defined at line 1714.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_fnc_distance_ranges(self, ranges: Dict[int, Tuple[float, float]], fnc_name: Optional[str]=None) -> None`

Defined at line 1765.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_initial_bin_shift(self) -> int`

Defined at line 1836.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_initial_bin_shift(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1841.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_xmax_used(self) -> float`

Defined at line 1849.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_xmax_used(self, value: float, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1854.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_num_atoms_per_move(self) -> int`

Defined at line 1860.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_num_atoms_per_move(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1872.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_history_buffer_size(self) -> int`

Defined at line 1896.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_history_buffer_size(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1901.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_display_update_interval(self) -> int`

Defined at line 1909.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_display_update_interval(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1914.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_custom_move_flag(self) -> int`

Defined at line 1922.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_custom_move_flag(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1928.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_load_histogram_flag(self) -> int`

Defined at line 1956.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_load_histogram_flag(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1961.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_max_atoms_per_cell(self) -> int`

Defined at line 1969.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_max_atoms_per_cell(self, value: int, *, auto_write: Optional[bool]=None) -> bool`

Defined at line 1974.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_swap_settings(self) -> Tuple[float, int]`

Defined at line 1986.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_swap_settings(self, fraction: float, allow_flag: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 1999.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_thread_count(self) -> int`

Defined at line 2028.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_thread_count(self, value: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 2033.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_angle_constraints(self) -> List[Dict[str, Any]]`

Defined at line 2169.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_angle_constraint(self, central_type: int, neighbor1: Tuple[int, Union[int, float], Union[int, float]], neighbor2: Tuple[int, Union[int, float], Union[int, float]], *, distribution_type: str='GAUSSIAN', angle_degrees: Optional[Union[int, float]]=None, distribution_width: Optional[Union[int, float]]=None, dcosth: Optional[Union[int, float]]=None, sigma: Union[int, float], sigma_mode: str='normal', index: int=0, auto_write: Optional[bool]=None) -> int`

Defined at line 2282.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_angle_constraint(self, index: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 2415.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_angle_constraints(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 2427.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_coord_constraints(self) -> List[Dict[str, Any]]`

Defined at line 2440.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_coord_constraint(self, central_type: int, neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], subconstraints: Sequence[Tuple[int, Union[int, float], Union[int, float]]], *, sigma_mode: str='normal', write_cnc_detail: bool=False, auto_write: Optional[bool]=None) -> int`

Defined at line 2530.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_coord_constraint(self, central_type: int, neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], subconstraints: Sequence[Tuple[int, Union[int, float], Union[int, float]]], *, index: int=0, sigma_mode: str='normal', write_cnc_detail: bool=False, auto_write: Optional[bool]=None) -> int`

Defined at line 2566.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_coord_constraint(self, index: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 2680.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_coord_constraints(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 2692.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_qn_constraints(self) -> List[Dict[str, Any]]`

Defined at line 2705.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_qn_constraint(self, index: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 2823.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_qn_constraint(self, central_type: int, first_neighbor_type: int, first_neighbor_minimum: Union[int, float], first_neighbor_maximum: Union[int, float], second_neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], coordination_number: int, fraction: Union[int, float], sigma: Union[int, float], *, sigma_mode: str='normal', auto_write: Optional[bool]=None) -> int`

Defined at line 2840.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_qn_constraint(self, central_type: int, first_neighbor_type: int, first_neighbor_minimum: Union[int, float], first_neighbor_maximum: Union[int, float], second_neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], coordination_number: int, fraction: Union[int, float], sigma: Union[int, float], *, index: int=0, sigma_mode: str='normal', auto_write: Optional[bool]=None) -> int`

Defined at line 2884.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_qn_constraints(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 3003.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_bvs_constraints(self) -> List[Dict[str, Any]]`

Defined at line 3018.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_bvs_constraint(self, central_type: int, neighbors: Sequence[Tuple[int, Union[int, float], Optional[Union[int, float]], Optional[Union[int, float]], Optional[int]]], valence: Union[int, float], sigma: Union[int, float], *, central_charge: Optional[int]=None, sigma_mode: str='normal', index: int=0, auto_write: Optional[bool]=None) -> int`

Defined at line 3109.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_bvs_constraint(self, index: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 3252.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_bvs_constraints(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 3263.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_pair_potential_settings(self) -> Optional[Dict[str, Any]]`

Defined at line 3271.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_pair_potential(self, partials: Sequence[Tuple[int, str, Union[int, float, str], str]], *, cutoff: Optional[Union[int, float]]=None, temperature: Union[int, float]=298.0, auto_write: Optional[bool]=None) -> None`

Defined at line 3338.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_pair_potential(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 3449.

Refer to the implementation for detailed semantics, side effects, and return values.

### `write_pair_potential_file(cls, filename: Union[str, Path], points: Sequence[Tuple[Union[int, float], Union[int, float]]], *, comment: str='') -> None`

Defined at line 3470.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_cos_constraints(self) -> List[Dict[str, Any]]`

Defined at line 3505.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_cos_constraint(self, *args: Any, **kwargs: Any) -> int`

Defined at line 3509.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_snc_constraints(self) -> List[Dict[str, Any]]`

Defined at line 3513.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_snc_constraint(self, *args: Any, **kwargs: Any) -> int`

Defined at line 3517.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_lj_potential(self) -> Optional[Dict[str, Any]]`

Defined at line 3521.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_lj_potential(self, ngr_types: int, lj_sigma: Sequence[Union[int, float]], lj_epsilon: Sequence[Union[int, float]], *, cutoff_vdw: Union[int, float]=1.0, cutoff_coul: Optional[Union[int, float]]=None, vdw_sigma: Union[int, float, str]=1.0, coul_sigma: Optional[Union[int, float, str]]=None, lj_power: int=12, scale_14_vdw: Union[int, float]=1.0, scale_14_coul: Optional[Union[int, float]]=None, chi_lowlimit_ratio: Optional[Union[int, float]]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 3535.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_custom_move(self) -> Optional[Dict[str, Any]]`

Defined at line 3593.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_custom_move(self, nmoved_atoms: int, custom_lines: Sequence[Union[str, int, float]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 3603.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_local_invariance(self) -> Optional[Dict[str, Any]]`

Defined at line 3625.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_local_invariance(self, mode: str, intervals: Sequence[Tuple[Union[int, float], Union[int, float, str], str]], *, r_spacing: Optional[Union[int, float]]=None, end: Optional[Union[int, float]]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 3646.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_non_periodic(self) -> Optional[Tuple[float, bool]]`

Defined at line 3685.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_non_periodic(self, sample_radius: Union[int, float], *, recentre: bool=False, auto_write: Optional[bool]=None) -> None`

Defined at line 3695.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_vibrational_amplitudes(self) -> List[float]`

Defined at line 3714.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_vibrational_amplitudes(self, sigma_values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 3724.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_common_neighbor_constraints(self) -> List[Dict[str, Any]]`

Defined at line 3740.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_common_neighbor_constraint(self, index: int, primary_type1: int, primary_type2: int, primary_minimum: Union[int, float], primary_maximum: Union[int, float], secondary: Sequence[Tuple[int, Union[int, float], Union[int, float], Union[int, float], Union[int, float]]], coordination_number: int, fraction: Union[int, float], sigma: Union[int, float, str], *, sigma_mode: str='normal', auto_write: Optional[bool]=None) -> None`

Defined at line 3750.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_ann_potential_settings(self) -> Optional[Dict[str, Any]]`

Defined at line 3798.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_ann_potential(self, *args: Any, **kwargs: Any) -> None`

Defined at line 3802.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_aenet_settings(self) -> Optional[Dict[str, Any]]`

Defined at line 3835.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_aenet_potential(self, potentials: Sequence[Tuple[int, str, Optional[str]]], sigma: Union[int, float], *, sigma_mode: str='normal', cutoff: Optional[Union[int, float]]=None, write_atomic_energy: bool=False, aenet_step: int=5, auto_write: Optional[bool]=None) -> None`

Defined at line 3923.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_aenet_potential_file(self, atom_type: int, filename: str, type_name: Optional[str]=None, *, auto_write: Optional[bool]=None) -> None`

Defined at line 4038.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_aenet_potential_file(self, atom_type: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 4100.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_aenet_potential(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 4150.

Refer to the implementation for detailed semantics, side effects, and return values.

## `main() -> None`

Defined at line 4172.

Refer to the implementation for detailed semantics, side effects, and return values.

