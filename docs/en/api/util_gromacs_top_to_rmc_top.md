# `rmc_util.util.gromacs_top_to_rmc_top`

GROMACS topology conversion.

Source: `src/rmc_util/util/gromacs_top_to_rmc_top.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `TopologyConvertError`

Defined at line 47.

## Class `GroAtom`

Defined at line 51.

### `__init__(self, index: int, residue_name: str, atom_name: str) -> None`

Defined at line 54.

Refer to the implementation for detailed semantics, side effects, and return values.

## Class `MoleculeType`

Defined at line 60.

### `__init__(self, name: str, nrexcl: str) -> None`

Defined at line 63.

Refer to the implementation for detailed semantics, side effects, and return values.

## Class `TopologyInfo`

Defined at line 69.

### `__init__(self) -> None`

Defined at line 72.

Refer to the implementation for detailed semantics, side effects, and return values.

## `read_text_lines(path: str) -> List[str]`

Defined at line 109.

Refer to the implementation for detailed semantics, side effects, and return values.

## `write_text_lines(path: str, lines: Sequence[str]) -> None`

Defined at line 115.

Refer to the implementation for detailed semantics, side effects, and return values.

## `read_gro(path: str) -> List[GroAtom]`

Defined at line 125.

Refer to the implementation for detailed semantics, side effects, and return values.

## `expand_local_includes(top_path: str, lines: Sequence[str], include_dirs: Optional[Sequence[str]]=None, expand_local_itp: bool=False, _seen: Optional[set]=None) -> List[str]`

Defined at line 176.

Refer to the implementation for detailed semantics, side effects, and return values.

## `parse_topology_info(lines: Sequence[str]) -> TopologyInfo`

Defined at line 239.

Refer to the implementation for detailed semantics, side effects, and return values.

## `build_rmc_index_map(info: TopologyInfo) -> Tuple[Dict[str, int], Dict[Tuple[str, int], List[int]], int]`

Defined at line 310.

Refer to the implementation for detailed semantics, side effects, and return values.

## `replace_force_field_include(lines: Sequence[str], force_field_include: Optional[str]) -> List[str]`

Defined at line 378.

Refer to the implementation for detailed semantics, side effects, and return values.

## `convert_topology_lines(top_lines: Sequence[str], gro_atoms: Sequence[GroAtom], force_field_include: Optional[str]=None) -> Tuple[List[str], TopologyInfo]`

Defined at line 430.

Refer to the implementation for detailed semantics, side effects, and return values.

## `convert_gromacs_top_to_rmc_top(top_path: str, gro_path: str, output_path: str, force_field_include: Optional[str]=None, include_dirs: Optional[Sequence[str]]=None, expand_local_itp: bool=False) -> TopologyInfo`

Defined at line 489.

Refer to the implementation for detailed semantics, side effects, and return values.

## `build_arg_parser() -> argparse.ArgumentParser`

Defined at line 515.

Refer to the implementation for detailed semantics, side effects, and return values.

## `main(argv: Optional[Sequence[str]]=None) -> int`

Defined at line 544.

CLI entry point。

