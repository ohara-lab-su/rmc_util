# `rmc_util.util.gromacs_top_to_rmc_top`

Source: `src/rmc_util/util/gromacs_top_to_rmc_top.py`

## Class `TopologyConvertError`

Exception raised when conversion from a GROMACS topology to an RMC_POT topology fails.

## Class `GroAtom`

Information for one atom in a GROMACS gro file.

### `__init__(self, index: int, residue_name: str, atom_name: str)`

This method has no docstring. Consult the implementation for its behavior.

## Class `MoleculeType`

A molecule-type definition in the topology.

### `__init__(self, name: str, nrexcl: str)`

This method has no docstring. Consult the implementation for its behavior.

## Class `TopologyInfo`

Minimal information required for topology conversion.

### `__init__(self)`

This method has no docstring. Consult the implementation for its behavior.

## `read_text_lines(path: str)`

Read a text file, preserving line endings.

## `write_text_lines(path: str, lines: Sequence[str])`

Write a text file.

## `read_gro(path: str)`

Read a GROMACS gro file and return atoms in file order.

Because atom serial numbers in a gro file may wrap at 99999, the order of appearance in the file is used as a one-based index.

## `expand_local_includes(top_path: str, lines: Sequence[str], include_dirs: Optional[Sequence[str]]=None, expand_local_itp: bool=False, _seen: Optional[set]=None)`

Expand local itp files containing molecule definitions when requested.

Preserve apparent force-field includes matching ``ff*.itp`` without expansion.

## `parse_topology_info(lines: Sequence[str])`

Read molecule types and molecule counts from a topology.

## `build_rmc_index_map(info: TopologyInfo)`

Construct offsets for each molecule type and RMC indices for each local atom.

Returns:
    offsets: molecule type -> number of atoms preceding the first RMC index of that type.
    index_map: (molecule type, local atom index) -> list of RMC indices for each occurrence.
    total_atoms: total atom count expected from the topology.

## `replace_force_field_include(lines: Sequence[str], force_field_include: Optional[str])`

Replace a force-field include when requested.

If ``force_field_include`` is None, leave the input unchanged.
If an existing ``#include "ff*.itp"`` is present, replace its first occurrence.
Otherwise insert it immediately after the ``[ defaults ]`` block.

## `convert_topology_lines(top_lines: Sequence[str], gro_atoms: Sequence[GroAtom], force_field_include: Optional[str]=None)`

Convert GROMACS topology lines into topology lines for RMC_POT.

## `convert_gromacs_top_to_rmc_top(top_path: str, gro_path: str, output_path: str, force_field_include: Optional[str]=None, include_dirs: Optional[Sequence[str]]=None, expand_local_itp: bool=False)`

Generate an RMC_POT ``*.top`` file from GROMACS ``*.top`` and ``*.gro`` files.

## `build_arg_parser()`

Create the argument parser for the CLI.

## `main(argv: Optional[Sequence[str]]=None)`

CLI entry point.


## API reference

The classes and functions defined in this module are listed below.

### Methods of `TopologyConvertError`

| Method | Definition line | Description (first line of docstring) |
|---|---:|---|
| (No public methods) | — | — |

### Methods of `GroAtom`

| Method | Definition line | Description (first line of docstring) |
|---|---:|---|
| `__init__()` | 54 | No description in source |

### Methods of `MoleculeType`

| Method | Definition line | Description (first line of docstring) |
|---|---:|---|
| `__init__()` | 63 | No description in source |

### Methods of `TopologyInfo`

| Method | Definition line | Description (first line of docstring) |
|---|---:|---|
| `__init__()` | 72 | No description in source |

### Module function `read_text_lines()`

- Defined at line 109
- Description:Read a text file, preserving line endings.

### Module function `write_text_lines()`

- Defined at line 115
- Description:Write a text file.

### Module function `read_gro()`

- Defined at line 125
- Description:Read a GROMACS gro file and return atoms in file order.

### Module function `expand_local_includes()`

- Defined at line 176
- Description:Expand local itp files containing molecule definitions when requested.

### Module function `parse_topology_info()`

- Defined at line 239
- Description:Read molecule types and molecule counts from a topology.

### Module function `build_rmc_index_map()`

- Defined at line 310
- Description:Construct offsets for each molecule type and RMC indices for each local atom.

### Module function `replace_force_field_include()`

- Defined at line 378
- Description:Replace a force-field include when requested.

### Module function `convert_topology_lines()`

- Defined at line 430
- Description:Convert GROMACS topology lines into topology lines for RMC_POT.

### Module function `convert_gromacs_top_to_rmc_top()`

- Defined at line 489
- Description:Generate an RMC_POT ``*.top`` file from GROMACS ``*.top`` and ``*.gro`` files.

### Module function `build_arg_parser()`

- Defined at line 515
- Description:Create the argument parser for the CLI.

### Module function `main()`

- Defined at line 544
- Description:CLI entry point.

## Argument and return type annotations

The tables show argument and return type annotations from function declarations. “Not specified” indicates the absence of a type annotation.

### `GroAtom.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `index` | `int` |
| `residue_name` | `str` |
| `atom_name` | `str` |

Return type annotation: `None`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:54`.

### `MoleculeType.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `name` | `str` |
| `nrexcl` | `str` |

Return type annotation: `None`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:63`.

### `TopologyInfo.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `None`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:72`.

### `read_text_lines`

| Argument | Type annotation |
|---|---|
| `path` | `str` |

Return type annotation: `List[str]`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:109`.

### `write_text_lines`

| Argument | Type annotation |
|---|---|
| `path` | `str` |
| `lines` | `Sequence[str]` |

Return type annotation: `None`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:115`.

### `read_gro`

| Argument | Type annotation |
|---|---|
| `path` | `str` |

Return type annotation: `List[GroAtom]`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:125`.

### `expand_local_includes`

| Argument | Type annotation |
|---|---|
| `top_path` | `str` |
| `lines` | `Sequence[str]` |
| `include_dirs` | `Optional[Sequence[str]]` |
| `expand_local_itp` | `bool` |
| `_seen` | `Optional[set]` |

Return type annotation: `List[str]`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:176`.

### `parse_topology_info`

| Argument | Type annotation |
|---|---|
| `lines` | `Sequence[str]` |

Return type annotation: `TopologyInfo`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:239`.

### `build_rmc_index_map`

| Argument | Type annotation |
|---|---|
| `info` | `TopologyInfo` |

Return type annotation: `Tuple[Dict[str, int], Dict[Tuple[str, int], List[int]], int]`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:310`.

### `replace_force_field_include`

| Argument | Type annotation |
|---|---|
| `lines` | `Sequence[str]` |
| `force_field_include` | `Optional[str]` |

Return type annotation: `List[str]`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:378`.

### `convert_topology_lines`

| Argument | Type annotation |
|---|---|
| `top_lines` | `Sequence[str]` |
| `gro_atoms` | `Sequence[GroAtom]` |
| `force_field_include` | `Optional[str]` |

Return type annotation: `Tuple[List[str], TopologyInfo]`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:430`.

### `convert_gromacs_top_to_rmc_top`

| Argument | Type annotation |
|---|---|
| `top_path` | `str` |
| `gro_path` | `str` |
| `output_path` | `str` |
| `force_field_include` | `Optional[str]` |
| `include_dirs` | `Optional[Sequence[str]]` |
| `expand_local_itp` | `bool` |

Return type annotation: `TopologyInfo`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:489`.

### `build_arg_parser`

| Argument | Type annotation |
|---|---|
| (None) | — |

Return type annotation: `argparse.ArgumentParser`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:515`.

### `main`

| Argument | Type annotation |
|---|---|
| `argv` | `Optional[Sequence[str]]` |

Return type annotation: `int`. Defined at: `src/rmc_util/util/gromacs_top_to_rmc_top.py:544`.

