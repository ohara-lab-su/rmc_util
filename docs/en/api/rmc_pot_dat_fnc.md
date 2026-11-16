# `rmc_util.rmc_pot_dat_fnc`

FNC constraint input handling.

Source: `src/rmc_util/rmc_pot_dat_fnc.py`.

## Class `FncNeighbour`

Represents one neighboring atom recorded in an FNC file.

Attributes:
    atom_index: One-based RMC index of the neighboring atom.
    constraint_type: Constraint type number referring to the distance-range table.

## Class `RmcPotDatFnc`

An independent class for creating and editing RMC_POT `*.fnc` files.

Low-level methods operate directly on one-based RMC atom indices in the final structure. Template methods explicitly expand mappings from local atom numbers to RMC indices; they do not infer bonds from element names or interatomic distances.

### `__init__(self, name: str, *, atom_count: Optional[int]=None, auto_write: bool=True, logger: Optional[XLogger]=None) -> None`

Defined at line 39.



### `path(self) -> Path`

Defined at line 84.



### `initialize(self, atom_count: int, *, title: Optional[str]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 92.



### `load(self) -> None`

Defined at line 116.



### `write(self, out_name: Optional[str]=None) -> None`

Defined at line 186.



### `set_title(self, title: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 228.



### `get_title(self) -> str`

Defined at line 238.



### `get_atom_count(self) -> int`

Defined at line 246.



### `set_distance_range(self, constraint_type: int, rmin: float, rmax: float, *, auto_write: Optional[bool]=None) -> None`

Defined at line 254.



### `set_distance_ranges(self, ranges: Union[Mapping[int, Tuple[float, float]], Sequence[Tuple[float, float]]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 282.



### `get_distance_ranges(self) -> Dict[int, Tuple[float, float]]`

Defined at line 309.



### `set_atom_neighbours(self, atom_index: int, neighbours: Iterable[Union[FncNeighbour, Tuple[int, int]]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 317.



### `get_atom_neighbours(self, atom_index: int) -> List[FncNeighbour]`

Defined at line 341.



### `add_neighbour(self, atom_index: int, neighbour_index: int, constraint_type: int, *, reciprocal: bool=False, auto_write: Optional[bool]=None) -> None`

Defined at line 353.



### `add_pair(self, atom_index1: int, atom_index2: int, constraint_type: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 381.



### `add_pairs(self, pairs: Iterable[Tuple[int, int, int]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 405.



### `remove_pair(self, atom_index1: int, atom_index2: int, *, reciprocal: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 421.



### `clear_atom_neighbours(self, atom_index: int, *, reciprocal: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 444.



### `add_template_instance(self, local_pairs: Iterable[Tuple[int, int, int]], local_to_rmc: Mapping[int, int], *, auto_write: Optional[bool]=None) -> None`

Defined at line 469.

Expand one local molecular template to final RMC atom indices.

### `add_template_instances(self, local_pairs: Iterable[Tuple[int, int, int]], instances: Iterable[Mapping[int, int]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 488.



### `add_group_complete_graph(self, atom_indices: Sequence[int], constraint_type: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 507.

Constrain every pair within an explicitly supplied atom group.

### `validate(self, *, require_reciprocal: bool=True) -> None`

Defined at line 521.



### `as_pairs(self, *, unique: bool=True) -> List[Tuple[int, int, int]]`

Defined at line 550.



## `main() -> None`

Defined at line 644.



