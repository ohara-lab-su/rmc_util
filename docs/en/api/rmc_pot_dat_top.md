# `rmc_util.rmc_pot_dat_top`

Source: `src/rmc_util/rmc_pot_dat_top.py`

## Class `TopologySection`

Represents one section in a TOP/ITP file.

Attributes:
    name: Section name without brackets.
    lines: Data lines within the section.

## Class `RmcPotDatTop`

A standalone class for generating and editing RMC_POT TOP/ITP files.

In addition to low-level section operations, methods explicitly add atoms, bonds, angles, and dihedrals. Both regular molecular templates and irregular networks represented as a single molecule spanning the cell are supported.

### `__init__(self, name: str, *, auto_write: bool=True, logger: Optional[XLogger]=None)`

Initialize the instance.

Args:
    name: Value supplied for name.
    auto_write: Value supplied for auto_write.
    logger: Value supplied for logger.

### `path(self)`

Return the current input/output path.

Returns:
    Result of the operation.

### `clear(self, *, auto_write: Optional[bool]=None)`

Clear the stored contents.

Args:
    auto_write: Value supplied for auto_write.

### `load(self)`

Load an existing file.
        

### `write(self, out_name: Optional[str]=None)`

Write the current state to a file.

Args:
    out_name: Value supplied for out_name.

### `add_raw_line(self, line: str='', *, auto_write: Optional[bool]=None)`

Add raw line.

Args:
    line: Value supplied for line.
    auto_write: Value supplied for auto_write.

### `add_comment(self, comment: str, *, auto_write: Optional[bool]=None)`

Add comment.

Args:
    comment: Value supplied for comment.
    auto_write: Value supplied for auto_write.

### `add_include(self, filename: str, *, auto_write: Optional[bool]=None)`

Add include.

Args:
    filename: Value supplied for filename.
    auto_write: Value supplied for auto_write.

### `add_ifdef(self, symbol: str, *, auto_write: Optional[bool]=None)`

Add ifdef.

Args:
    symbol: Value supplied for symbol.
    auto_write: Value supplied for auto_write.

### `add_ifndef(self, symbol: str, *, auto_write: Optional[bool]=None)`

Add ifndef.

Args:
    symbol: Value supplied for symbol.
    auto_write: Value supplied for auto_write.

### `add_else(self, *, auto_write: Optional[bool]=None)`

Add else.

Args:
    auto_write: Value supplied for auto_write.

### `add_endif(self, *, auto_write: Optional[bool]=None)`

Add endif.

Args:
    auto_write: Value supplied for auto_write.

### `add_section(self, name: str, *, auto_write: Optional[bool]=None)`

Add section.

Args:
    name: Value supplied for name.
    auto_write: Value supplied for auto_write.

Returns:
    Result of the operation.

### `get_sections(self, name: Optional[str]=None)`

Get sections.

Args:
    name: Value supplied for name.

Returns:
    Result of the operation.

### `get_last_section(self, name: str)`

Get last section.

Args:
    name: Value supplied for name.

Returns:
    Result of the operation.

### `add_section_line(self, section_name: str, line: str, *, create: bool=True, auto_write: Optional[bool]=None)`

Add section line.

Args:
    section_name: Value supplied for section_name.
    line: Value supplied for line.
    create: Value supplied for create.
    auto_write: Value supplied for auto_write.

### `remove_sections(self, name: str, *, auto_write: Optional[bool]=None)`

Remove sections.

Args:
    name: Value supplied for name.
    auto_write: Value supplied for auto_write.

### `begin_molecule_type(self, name: str, exclusions: int, *, index_offset: Optional[int]=None, auto_write: Optional[bool]=None)`

Execute begin molecule type.

Args:
    name: Value supplied for name.
    exclusions: Value supplied for exclusions.
    index_offset: Value supplied for index_offset.
    auto_write: Value supplied for auto_write.

### `add_atom(self, serial: int, atom_type: str, residue_number: int, residue_name: str, atom_name: str, charge_group: int, charge: float, mass: Optional[float], first_rmc_index: int, second_rmc_index: int, *, auto_write: Optional[bool]=None)`

Add atom.

Args:
    serial: Value supplied for serial.
    atom_type: Value supplied for atom_type.
    residue_number: Value supplied for residue_number.
    residue_name: Value supplied for residue_name.
    atom_name: Value supplied for atom_name.
    charge_group: Value supplied for charge_group.
    charge: Value supplied for charge.
    mass: Value supplied for mass.
    first_rmc_index: Value supplied for first_rmc_index.
    second_rmc_index: Value supplied for second_rmc_index.
    auto_write: Value supplied for auto_write.

### `add_virtual_atom(self, serial: int, atom_type: str, residue_number: int, residue_name: str, atom_name: str, charge_group: int, charge: float, *, mass: float=0.0, auto_write: Optional[bool]=None)`

Add virtual atom.

Args:
    serial: Value supplied for serial.
    atom_type: Value supplied for atom_type.
    residue_number: Value supplied for residue_number.
    residue_name: Value supplied for residue_name.
    atom_name: Value supplied for atom_name.
    charge_group: Value supplied for charge_group.
    charge: Value supplied for charge.
    mass: Value supplied for mass.
    auto_write: Value supplied for auto_write.

### `add_pair(self, atom_i: int, atom_j: int, *, function_type: int=1, v_parameter: Optional[float]=None, w_parameter: Optional[float]=None, auto_write: Optional[bool]=None)`

Add pair.

Args:
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    function_type: Value supplied for function_type.
    v_parameter: Value supplied for v_parameter.
    w_parameter: Value supplied for w_parameter.
    auto_write: Value supplied for auto_write.

### `add_bond(self, atom_i: int, atom_j: int, equilibrium_nm: float, force_constant: float, sigma: Optional[float]=None, *, function_type: int=1, rmc_parameters_after_semicolon: bool=False, auto_write: Optional[bool]=None)`

Add bond.

Args:
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    equilibrium_nm: Value supplied for equilibrium_nm.
    force_constant: Value supplied for force_constant.
    sigma: Value supplied for sigma.
    function_type: Value supplied for function_type.
    rmc_parameters_after_semicolon: Value supplied for rmc_parameters_after_semicolon.
    auto_write: Value supplied for auto_write.

### `add_angle(self, atom_i: int, atom_j: int, atom_k: int, equilibrium_degree: float, force_constant: float, sigma: Optional[float]=None, *, function_type: int=1, rmc_parameters_after_semicolon: bool=False, auto_write: Optional[bool]=None)`

Add angle.

Args:
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    atom_k: Value supplied for atom_k.
    equilibrium_degree: Value supplied for equilibrium_degree.
    force_constant: Value supplied for force_constant.
    sigma: Value supplied for sigma.
    function_type: Value supplied for function_type.
    rmc_parameters_after_semicolon: Value supplied for rmc_parameters_after_semicolon.
    auto_write: Value supplied for auto_write.

### `add_periodic_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, equilibrium_degree: float, force_constant: float, multiplicity: int, sigma: Optional[float]=None, *, auto_write: Optional[bool]=None)`

Add periodic dihedral.

Args:
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    atom_k: Value supplied for atom_k.
    atom_l: Value supplied for atom_l.
    equilibrium_degree: Value supplied for equilibrium_degree.
    force_constant: Value supplied for force_constant.
    multiplicity: Value supplied for multiplicity.
    sigma: Value supplied for sigma.
    auto_write: Value supplied for auto_write.

### `add_harmonic_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, equilibrium_degree: float, force_constant: float, sigma: Optional[float]=None, *, auto_write: Optional[bool]=None)`

Add harmonic dihedral.

Args:
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    atom_k: Value supplied for atom_k.
    atom_l: Value supplied for atom_l.
    equilibrium_degree: Value supplied for equilibrium_degree.
    force_constant: Value supplied for force_constant.
    sigma: Value supplied for sigma.
    auto_write: Value supplied for auto_write.

### `add_rb_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, coefficients: Sequence[float], sigma: Optional[float]=None, *, auto_write: Optional[bool]=None)`

Add rb dihedral.

Args:
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    atom_k: Value supplied for atom_k.
    atom_l: Value supplied for atom_l.
    coefficients: Value supplied for coefficients.
    sigma: Value supplied for sigma.
    auto_write: Value supplied for auto_write.

### `add_exclusion(self, centre_atom: int, excluded_atoms: Sequence[int], *, auto_write: Optional[bool]=None)`

Add exclusion.

Args:
    centre_atom: Value supplied for centre_atom.
    excluded_atoms: Value supplied for excluded_atoms.
    auto_write: Value supplied for auto_write.

### `add_virtual_site2(self, site: int, atom_i: int, atom_j: int, a: float, *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None)`

Add virtual site2.

Args:
    site: Value supplied for site.
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    a: Value supplied for a.
    host_atom: Value supplied for host_atom.
    auto_write: Value supplied for auto_write.

### `add_virtual_site3(self, site: int, atom_i: int, atom_j: int, atom_k: int, function_type: int, parameters: Sequence[float], *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None)`

Add virtual site3.

Args:
    site: Value supplied for site.
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    atom_k: Value supplied for atom_k.
    function_type: Value supplied for function_type.
    parameters: Value supplied for parameters.
    host_atom: Value supplied for host_atom.
    auto_write: Value supplied for auto_write.

### `add_virtual_site4(self, site: int, atom_i: int, atom_j: int, atom_k: int, atom_l: int, a: float, b: float, c_nm: float, *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None)`

Add virtual site4.

Args:
    site: Value supplied for site.
    atom_i: Value supplied for atom_i.
    atom_j: Value supplied for atom_j.
    atom_k: Value supplied for atom_k.
    atom_l: Value supplied for atom_l.
    a: Value supplied for a.
    b: Value supplied for b.
    c_nm: Value supplied for c_nm.
    host_atom: Value supplied for host_atom.
    auto_write: Value supplied for auto_write.

### `set_system(self, name: str, *, auto_write: Optional[bool]=None)`

Set the system.

Args:
    name: Value supplied for name.
    auto_write: Value supplied for auto_write.

### `set_molecules(self, molecules: Sequence[Tuple[str, int]], *, auto_write: Optional[bool]=None)`

Set the molecules.

Args:
    molecules: Value supplied for molecules.
    auto_write: Value supplied for auto_write.

### `add_molecule_template(self, molecule_name: str, atoms: Sequence[Mapping[str, object]], first_instance_indices: Mapping[int, int], second_instance_indices: Mapping[int, int], *, exclusions: int=3, index_offset: Optional[int]=None, bonds: Sequence[Mapping[str, object]]=(), angles: Sequence[Mapping[str, object]]=(), periodic_dihedrals: Sequence[Mapping[str, object]]=(), harmonic_dihedrals: Sequence[Mapping[str, object]]=(), rb_dihedrals: Sequence[Mapping[str, object]]=(), pairs: Sequence[Mapping[str, object]]=(), explicit_exclusions: Sequence[Tuple[int, Sequence[int]]]=(), auto_write: Optional[bool]=None)`

Add a reusable molecule type.

Args:
    molecule_name: Molecule name written in ``[ moleculetype ]``.
    atoms: Sequence of atom dictionaries within the molecule.``serial`` and ``atom_type`` are required.
    first_instance_indices: Local serial and RMC index for the first molecule.
    second_instance_indices: Local serial and RMC index for the second molecule.
    exclusions: GROMACS nrexcl.
    index_offset: Explicit index offset for RMC_POT.
    bonds: Sequence of dictionaries passed to ``add_bond()``.
    angles: Sequence of dictionaries passed to ``add_angle()``.
    periodic_dihedrals: Sequence of periodic-dihedral dictionaries.
    harmonic_dihedrals: Sequence of harmonic-dihedral dictionaries.
    rb_dihedrals: Sequence of Ryckaert--Bellemans-dihedral dictionaries.
    pairs: Sequence of dictionaries passed to ``add_pair()``.
    explicit_exclusions: Pairs of central atoms and lists of excluded atoms.
    auto_write: Whether to save automatically after adding.

### `add_explicit_network_molecule(self, molecule_name: str, atoms: Sequence[Mapping[str, object]], *, exclusions: int=2, bonds: Sequence[Mapping[str, object]]=(), angles: Sequence[Mapping[str, object]]=(), periodic_dihedrals: Sequence[Mapping[str, object]]=(), harmonic_dihedrals: Sequence[Mapping[str, object]]=(), rb_dihedrals: Sequence[Mapping[str, object]]=(), auto_write: Optional[bool]=None)`

Add an arbitrary cell-spanning network as one large molecule.

Map each local serial directly to its final RMC index. Because there is only one molecule instance, the first and second RMC indices recorded in ``[ atoms ]`` are identical. This representation supports Qn networks that cannot be expressed as regular repetitions.

### `validate_rmc_index_progression(first_instance: Mapping[int, int], second_instance: Mapping[int, int], all_instances: Sequence[Mapping[int, int]])`

Check that later instances follow the first/second index progression.

### `validate(self)`

Validate the current configuration.
        

## Class `RmcPotDatItp`

Explicit class name for include-topology files.

## `main()`

Generate ``sample.top`` from the SnI4 indexing example in the RMC_POT manual.

The example illustrates the correspondence between the ``first index`` and ``second index`` fields at the end of ``[ atoms ]``. Bond-potential parameters cannot be inferred from the indexing example, so sections such as ``[ bonds ]`` are not generated.

In the first representation in the manual, the Sn atoms of 1000 SnI4 molecules occupy RMC indices 1--1000. The four iodine positions occupy blocks 1001--2000, 2001--3000, 3001--4000, and 4001--5000. Thus, the first two molecule instances map as follows.

* Sn: 1, 2
* I1: 1001, 1005
* I2: 1002, 1006
* I3: 1003, 1007
* I4: 1004, 1008

This rule determines each atom’s RMC index for any molecule number.


## API inventory


### `TopologySection` methods

| Method | Definition line | Description |
|---|---:|---|
| (No public methods) | — | — |

### `RmcPotDatTop` methods

| Method | Definition line | Description |
|---|---:|---|
| `__init__()` | 56 | Initialize the instance. |
| `path()` | 93 | Return the current input/output path. |
| `clear()` | 101 | Clear the stored contents. |
| `load()` | 110 | Load an existing file. |
| `write()` | 130 | Write the current state to a file. |
| `add_raw_line()` | 149 |Add raw line. |
| `add_comment()` | 159 |Add comment. |
| `add_include()` | 171 |Add include. |
| `add_ifdef()` | 180 |Add ifdef. |
| `add_ifndef()` | 189 |Add ifndef. |
| `add_else()` | 198 |Add else. |
| `add_endif()` | 206 |Add endif. |
| `add_section()` | 214 |Add section. |
| `get_sections()` | 234 |Get sections. |
| `get_last_section()` | 249 |Get last section. |
| `add_section_line()` | 263 |Add section line. |
| `remove_sections()` | 289 |Remove sections. |
| `begin_molecule_type()` | 303 |Execute begin molecule type. |
| `add_atom()` | 326 |Add atom. |
| `add_virtual_atom()` | 368 |Add virtual atom. |
| `add_pair()` | 399 |Add pair. |
| `add_bond()` | 426 |Add bond. |
| `add_angle()` | 457 |Add angle. |
| `add_periodic_dihedral()` | 490 |Add periodic dihedral. |
| `add_harmonic_dihedral()` | 524 |Add harmonic dihedral. |
| `add_rb_dihedral()` | 556 |Add rb dihedral. |
| `add_exclusion()` | 586 |Add exclusion. |
| `add_virtual_site2()` | 608 |Add virtual site2. |
| `add_virtual_site3()` | 634 |Add virtual site3. |
| `add_virtual_site4()` | 669 |Add virtual site4. |
| `set_system()` | 702 | Set the system. |
| `set_molecules()` | 714 | Set the molecules. |
| `add_molecule_template()` | 734 | Add a reusable molecule type. |
| `add_explicit_network_molecule()` | 807 | Add an arbitrary cell-spanning network as one large molecule. |
| `validate_rmc_index_progression()` | 848 | Check that later instances follow the first/second index progression. |
| `validate()` | 871 | Validate the current configuration. |

### `RmcPotDatItp` methods

| Method | Definition line | Description |
|---|---:|---|
| (No public methods) | — | — |

### Module function `main()`

- Definition line: 1077 line
- Description: Generate ``sample.top`` from the SnI4 indexing example in the RMC_POT manual.

## Parameters and return types


### `RmcPotDatTop.__init__`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `str` |
| `auto_write` | `bool` |
| `logger` | `Optional[XLogger]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:56`。

### `RmcPotDatTop.path`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |

Return type annotation: `Path`。Definition: `src/rmc_util/rmc_pot_dat_top.py:93`。

### `RmcPotDatTop.clear`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:101`。

### `RmcPotDatTop.load`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:110`。

### `RmcPotDatTop.write`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `out_name` | `Optional[str]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:130`。

### `RmcPotDatTop.add_raw_line`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `line` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:149`。

### `RmcPotDatTop.add_comment`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `comment` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:159`。

### `RmcPotDatTop.add_include`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `filename` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:171`。

### `RmcPotDatTop.add_ifdef`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `symbol` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:180`。

### `RmcPotDatTop.add_ifndef`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `symbol` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:189`。

### `RmcPotDatTop.add_else`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:198`。

### `RmcPotDatTop.add_endif`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:206`。

### `RmcPotDatTop.add_section`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `TopologySection`。Definition: `src/rmc_util/rmc_pot_dat_top.py:214`。

### `RmcPotDatTop.get_sections`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `Optional[str]` |

Return type annotation: `List[TopologySection]`。Definition: `src/rmc_util/rmc_pot_dat_top.py:234`。

### `RmcPotDatTop.get_last_section`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `str` |

Return type annotation: `TopologySection`。Definition: `src/rmc_util/rmc_pot_dat_top.py:249`。

### `RmcPotDatTop.add_section_line`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `section_name` | `str` |
| `line` | `str` |
| `create` | `bool` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:263`。

### `RmcPotDatTop.remove_sections`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:289`。

### `RmcPotDatTop.begin_molecule_type`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `str` |
| `exclusions` | `int` |
| `index_offset` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:303`。

### `RmcPotDatTop.add_atom`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `serial` | `int` |
| `atom_type` | `str` |
| `residue_number` | `int` |
| `residue_name` | `str` |
| `atom_name` | `str` |
| `charge_group` | `int` |
| `charge` | `float` |
| `mass` | `Optional[float]` |
| `first_rmc_index` | `int` |
| `second_rmc_index` | `int` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:326`。

### `RmcPotDatTop.add_virtual_atom`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `serial` | `int` |
| `atom_type` | `str` |
| `residue_number` | `int` |
| `residue_name` | `str` |
| `atom_name` | `str` |
| `charge_group` | `int` |
| `charge` | `float` |
| `mass` | `float` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:368`。

### `RmcPotDatTop.add_pair`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `function_type` | `int` |
| `v_parameter` | `Optional[float]` |
| `w_parameter` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:399`。

### `RmcPotDatTop.add_bond`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `equilibrium_nm` | `float` |
| `force_constant` | `float` |
| `sigma` | `Optional[float]` |
| `function_type` | `int` |
| `rmc_parameters_after_semicolon` | `bool` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:426`。

### `RmcPotDatTop.add_angle`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `equilibrium_degree` | `float` |
| `force_constant` | `float` |
| `sigma` | `Optional[float]` |
| `function_type` | `int` |
| `rmc_parameters_after_semicolon` | `bool` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:457`。

### `RmcPotDatTop.add_periodic_dihedral`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `equilibrium_degree` | `float` |
| `force_constant` | `float` |
| `multiplicity` | `int` |
| `sigma` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:490`。

### `RmcPotDatTop.add_harmonic_dihedral`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `equilibrium_degree` | `float` |
| `force_constant` | `float` |
| `sigma` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:524`。

### `RmcPotDatTop.add_rb_dihedral`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `coefficients` | `Sequence[float]` |
| `sigma` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:556`。

### `RmcPotDatTop.add_exclusion`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `centre_atom` | `int` |
| `excluded_atoms` | `Sequence[int]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:586`。

### `RmcPotDatTop.add_virtual_site2`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `site` | `int` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `a` | `float` |
| `host_atom` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:608`。

### `RmcPotDatTop.add_virtual_site3`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `site` | `int` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `function_type` | `int` |
| `parameters` | `Sequence[float]` |
| `host_atom` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:634`。

### `RmcPotDatTop.add_virtual_site4`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `site` | `int` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `a` | `float` |
| `b` | `float` |
| `c_nm` | `float` |
| `host_atom` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:669`。

### `RmcPotDatTop.set_system`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `name` | `str` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:702`。

### `RmcPotDatTop.set_molecules`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `molecules` | `Sequence[Tuple[str, int]]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:714`。

### `RmcPotDatTop.add_molecule_template`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `molecule_name` | `str` |
| `atoms` | `Sequence[Mapping[str, object]]` |
| `first_instance_indices` | `Mapping[int, int]` |
| `second_instance_indices` | `Mapping[int, int]` |
| `exclusions` | `int` |
| `index_offset` | `Optional[int]` |
| `bonds` | `Sequence[Mapping[str, object]]` |
| `angles` | `Sequence[Mapping[str, object]]` |
| `periodic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `harmonic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `rb_dihedrals` | `Sequence[Mapping[str, object]]` |
| `pairs` | `Sequence[Mapping[str, object]]` |
| `explicit_exclusions` | `Sequence[Tuple[int, Sequence[int]]]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:734`。

### `RmcPotDatTop.add_explicit_network_molecule`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |
| `molecule_name` | `str` |
| `atoms` | `Sequence[Mapping[str, object]]` |
| `exclusions` | `int` |
| `bonds` | `Sequence[Mapping[str, object]]` |
| `angles` | `Sequence[Mapping[str, object]]` |
| `periodic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `harmonic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `rb_dihedrals` | `Sequence[Mapping[str, object]]` |
| `auto_write` | `Optional[bool]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:807`。

### `RmcPotDatTop.validate_rmc_index_progression`

| Parameter | Type annotation |
|---|---|
| `first_instance` | `Mapping[int, int]` |
| `second_instance` | `Mapping[int, int]` |
| `all_instances` | `Sequence[Mapping[int, int]]` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:848`。

### `RmcPotDatTop.validate`

| Parameter | Type annotation |
|---|---|
| `self` | `unspecified` |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:871`。

### `main`

| Parameter | Type annotation |
|---|---|
| (None) | — |

Return type annotation: `None`。Definition: `src/rmc_util/rmc_pot_dat_top.py:1077`。

