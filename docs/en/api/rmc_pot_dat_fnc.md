# `rmc_util.rmc_pot_dat_fnc`

FNC constraint input handling.

Source: `src/rmc_util/rmc_pot_dat_fnc.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `FncNeighbour`

Defined at line 19.

## Class `RmcPotDatFnc`

Defined at line 31.

### `__init__(self, name: str, *, atom_count: Optional[int]=None, auto_write: bool=True, logger: Optional[XLogger]=None) -> None`

Defined at line 39.

Refer to the implementation for detailed semantics, side effects, and return values.

### `path(self) -> Path`

Defined at line 84.

Refer to the implementation for detailed semantics, side effects, and return values.

### `initialize(self, atom_count: int, *, title: Optional[str]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 92.

Refer to the implementation for detailed semantics, side effects, and return values.

### `load(self) -> None`

Defined at line 116.

Refer to the implementation for detailed semantics, side effects, and return values.

### `write(self, out_name: Optional[str]=None) -> None`

Defined at line 186.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_title(self, title: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 228.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_title(self) -> str`

Defined at line 238.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_atom_count(self) -> int`

Defined at line 246.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_distance_range(self, constraint_type: int, rmin: float, rmax: float, *, auto_write: Optional[bool]=None) -> None`

Defined at line 254.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_distance_ranges(self, ranges: Union[Mapping[int, Tuple[float, float]], Sequence[Tuple[float, float]]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 282.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_distance_ranges(self) -> Dict[int, Tuple[float, float]]`

Defined at line 309.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_atom_neighbours(self, atom_index: int, neighbours: Iterable[Union[FncNeighbour, Tuple[int, int]]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 317.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_atom_neighbours(self, atom_index: int) -> List[FncNeighbour]`

Defined at line 341.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_neighbour(self, atom_index: int, neighbour_index: int, constraint_type: int, *, reciprocal: bool=False, auto_write: Optional[bool]=None) -> None`

Defined at line 353.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_pair(self, atom_index1: int, atom_index2: int, constraint_type: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 381.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_pairs(self, pairs: Iterable[Tuple[int, int, int]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 405.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_pair(self, atom_index1: int, atom_index2: int, *, reciprocal: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 421.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear_atom_neighbours(self, atom_index: int, *, reciprocal: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 444.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_template_instance(self, local_pairs: Iterable[Tuple[int, int, int]], local_to_rmc: Mapping[int, int], *, auto_write: Optional[bool]=None) -> None`

Defined at line 469.

Expand one local molecular template to final RMC atom indices.

### `add_template_instances(self, local_pairs: Iterable[Tuple[int, int, int]], instances: Iterable[Mapping[int, int]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 488.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_group_complete_graph(self, atom_indices: Sequence[int], constraint_type: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 507.

Constrain every pair within an explicitly supplied atom group.

### `validate(self, *, require_reciprocal: bool=True) -> None`

Defined at line 521.

Refer to the implementation for detailed semantics, side effects, and return values.

### `as_pairs(self, *, unique: bool=True) -> List[Tuple[int, int, int]]`

Defined at line 550.

Refer to the implementation for detailed semantics, side effects, and return values.

## `main() -> None`

Defined at line 644.

Refer to the implementation for detailed semantics, side effects, and return values.

