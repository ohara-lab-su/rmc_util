# `rmc_util.rmc_pot_dat_top`

Topology input handling.

Source: `src/rmc_util/rmc_pot_dat_top.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `TopologySection`

Defined at line 21.

## Class `RmcPotDatTop`

Defined at line 33.

### `__init__(self, name: str, *, auto_write: bool=True, logger: Optional[XLogger]=None) -> None`

Defined at line 56.

Refer to the implementation for detailed semantics, side effects, and return values.

### `path(self) -> Path`

Defined at line 93.

Refer to the implementation for detailed semantics, side effects, and return values.

### `clear(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 101.

Refer to the implementation for detailed semantics, side effects, and return values.

### `load(self) -> None`

Defined at line 110.

Refer to the implementation for detailed semantics, side effects, and return values.

### `write(self, out_name: Optional[str]=None) -> None`

Defined at line 130.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_raw_line(self, line: str='', *, auto_write: Optional[bool]=None) -> None`

Defined at line 149.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_comment(self, comment: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 159.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_include(self, filename: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 171.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_ifdef(self, symbol: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 180.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_ifndef(self, symbol: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 189.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_else(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 198.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_endif(self, *, auto_write: Optional[bool]=None) -> None`

Defined at line 206.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_section(self, name: str, *, auto_write: Optional[bool]=None) -> TopologySection`

Defined at line 214.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_sections(self, name: Optional[str]=None) -> List[TopologySection]`

Defined at line 234.

Refer to the implementation for detailed semantics, side effects, and return values.

### `get_last_section(self, name: str) -> TopologySection`

Defined at line 249.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_section_line(self, section_name: str, line: str, *, create: bool=True, auto_write: Optional[bool]=None) -> None`

Defined at line 263.

Refer to the implementation for detailed semantics, side effects, and return values.

### `remove_sections(self, name: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 289.

Refer to the implementation for detailed semantics, side effects, and return values.

### `begin_molecule_type(self, name: str, exclusions: int, *, index_offset: Optional[int]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 303.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_atom(self, serial: int, atom_type: str, residue_number: int, residue_name: str, atom_name: str, charge_group: int, charge: float, mass: Optional[float], first_rmc_index: int, second_rmc_index: int, *, auto_write: Optional[bool]=None) -> None`

Defined at line 326.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_virtual_atom(self, serial: int, atom_type: str, residue_number: int, residue_name: str, atom_name: str, charge_group: int, charge: float, *, mass: float=0.0, auto_write: Optional[bool]=None) -> None`

Defined at line 368.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_pair(self, atom_i: int, atom_j: int, *, function_type: int=1, v_parameter: Optional[float]=None, w_parameter: Optional[float]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 399.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_bond(self, atom_i: int, atom_j: int, equilibrium_nm: float, force_constant: float, sigma: Optional[float]=None, *, function_type: int=1, rmc_parameters_after_semicolon: bool=False, auto_write: Optional[bool]=None) -> None`

Defined at line 426.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_angle(self, atom_i: int, atom_j: int, atom_k: int, equilibrium_degree: float, force_constant: float, sigma: Optional[float]=None, *, function_type: int=1, rmc_parameters_after_semicolon: bool=False, auto_write: Optional[bool]=None) -> None`

Defined at line 457.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_periodic_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, equilibrium_degree: float, force_constant: float, multiplicity: int, sigma: Optional[float]=None, *, auto_write: Optional[bool]=None) -> None`

Defined at line 490.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_harmonic_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, equilibrium_degree: float, force_constant: float, sigma: Optional[float]=None, *, auto_write: Optional[bool]=None) -> None`

Defined at line 524.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_rb_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, coefficients: Sequence[float], sigma: Optional[float]=None, *, auto_write: Optional[bool]=None) -> None`

Defined at line 556.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_exclusion(self, centre_atom: int, excluded_atoms: Sequence[int], *, auto_write: Optional[bool]=None) -> None`

Defined at line 586.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_virtual_site2(self, site: int, atom_i: int, atom_j: int, a: float, *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 608.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_virtual_site3(self, site: int, atom_i: int, atom_j: int, atom_k: int, function_type: int, parameters: Sequence[float], *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 634.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_virtual_site4(self, site: int, atom_i: int, atom_j: int, atom_k: int, atom_l: int, a: float, b: float, c_nm: float, *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None) -> None`

Defined at line 669.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_system(self, name: str, *, auto_write: Optional[bool]=None) -> None`

Defined at line 702.

Refer to the implementation for detailed semantics, side effects, and return values.

### `set_molecules(self, molecules: Sequence[Tuple[str, int]], *, auto_write: Optional[bool]=None) -> None`

Defined at line 714.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_molecule_template(self, molecule_name: str, atoms: Sequence[Mapping[str, object]], first_instance_indices: Mapping[int, int], second_instance_indices: Mapping[int, int], *, exclusions: int=3, index_offset: Optional[int]=None, bonds: Sequence[Mapping[str, object]]=(), angles: Sequence[Mapping[str, object]]=(), periodic_dihedrals: Sequence[Mapping[str, object]]=(), harmonic_dihedrals: Sequence[Mapping[str, object]]=(), rb_dihedrals: Sequence[Mapping[str, object]]=(), pairs: Sequence[Mapping[str, object]]=(), explicit_exclusions: Sequence[Tuple[int, Sequence[int]]]=(), auto_write: Optional[bool]=None) -> None`

Defined at line 734.

Refer to the implementation for detailed semantics, side effects, and return values.

### `add_explicit_network_molecule(self, molecule_name: str, atoms: Sequence[Mapping[str, object]], *, exclusions: int=2, bonds: Sequence[Mapping[str, object]]=(), angles: Sequence[Mapping[str, object]]=(), periodic_dihedrals: Sequence[Mapping[str, object]]=(), harmonic_dihedrals: Sequence[Mapping[str, object]]=(), rb_dihedrals: Sequence[Mapping[str, object]]=(), auto_write: Optional[bool]=None) -> None`

Defined at line 807.

Refer to the implementation for detailed semantics, side effects, and return values.

### `validate_rmc_index_progression(first_instance: Mapping[int, int], second_instance: Mapping[int, int], all_instances: Sequence[Mapping[int, int]]) -> None`

Defined at line 848.

Check that later instances follow the first/second index progression.

### `validate(self) -> None`

Defined at line 871.

Refer to the implementation for detailed semantics, side effects, and return values.

## Class `RmcPotDatItp`

Defined at line 1073.

Explicit class name for include-topology files.

## `main() -> None`

Defined at line 1077.

Refer to the implementation for detailed semantics, side effects, and return values.

