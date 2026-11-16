# `rmc_util.util.zeolite`

Zeolite structure utilities.

Source: `src/rmc_util/util/zeolite.py`.

This reference is generated from the supplied Python source. Signatures and declaration lines are taken from that source; implementation-specific behavior must be checked against the code.

## Class `ZeoliteCutoffs`

Defined at line 48.

### `range_for_t(self, symbol: str) -> BondRange`

Defined at line 60.

Refer to the implementation for detailed semantics, side effects, and return values.

## Class `ZeoliteRmcConfig`

Defined at line 70.

## `load_zeolite_rmc_config_from_dat(path: str | Path) -> ZeoliteRmcConfig`

Defined at line 137.

Refer to the implementation for detailed semantics, side effects, and return values.

## `load_zeolite_rmc_config_from_init(path: str | Path) -> ZeoliteRmcConfig`

Defined at line 259.

Refer to the implementation for detailed semantics, side effects, and return values.

## `rmc_config_to_cutoffs(config: ZeoliteRmcConfig) -> ZeoliteCutoffs`

Defined at line 330.

Refer to the implementation for detailed semantics, side effects, and return values.

## `find_rmc_parameter_source(directory: str | Path='.') -> Optional[Path]`

Defined at line 343.

Refer to the implementation for detailed semantics, side effects, and return values.

## `load_zeolite_rmc_config(source: str | Path) -> ZeoliteRmcConfig`

Defined at line 376.

Refer to the implementation for detailed semantics, side effects, and return values.

## Class `ZeoliteCriteria`

Defined at line 395.

## Class `PeriodicEdge`

Defined at line 413.

## `validate_framework_elements(structure: Structure) -> None`

Defined at line 452.

Refer to the implementation for detailed semantics, side effects, and return values.

## `build_to_bonds(structure: Structure, cutoffs: ZeoliteCutoffs=ZeoliteCutoffs()) -> List[PeriodicEdge]`

Defined at line 482.

Refer to the implementation for detailed semantics, side effects, and return values.

## `coordination_distributions(structure: Structure, edges: Sequence[PeriodicEdge]) -> Dict[str, object]`

Defined at line 542.

Refer to the implementation for detailed semantics, side effects, and return values.

## `bond_length_statistics(structure: Structure, edges: Sequence[PeriodicEdge]) -> Dict[str, object]`

Defined at line 652.

Refer to the implementation for detailed semantics, side effects, and return values.

## `angle_statistics(structure: Structure, edges: Sequence[PeriodicEdge]) -> Dict[str, object]`

Defined at line 679.

Refer to the implementation for detailed semantics, side effects, and return values.

## `periodic_network_statistics(structure: Structure, edges: Sequence[PeriodicEdge]) -> Dict[str, object]`

Defined at line 753.

Refer to the implementation for detailed semantics, side effects, and return values.

## `build_tt_graph(structure: Structure, edges: Sequence[PeriodicEdge]) -> Dict[int, Set[int]]`

Defined at line 834.

Refer to the implementation for detailed semantics, side effects, and return values.

## `shortest_ring_statistics(structure: Structure, edges: Sequence[PeriodicEdge], max_ring_size: int=16) -> Dict[str, object]`

Defined at line 901.

Refer to the implementation for detailed semantics, side effects, and return values.

## `loewenstein_statistics(structure: Structure, edges: Sequence[PeriodicEdge]) -> Dict[str, object]`

Defined at line 955.

Refer to the implementation for detailed semantics, side effects, and return values.

## `framework_density(structure: Structure) -> float`

Defined at line 992.

Refer to the implementation for detailed semantics, side effects, and return values.

## `evaluate_zeolite_like(coordination: Mapping[str, object], network: Mapping[str, object], criteria: ZeoliteCriteria=ZeoliteCriteria()) -> Dict[str, object]`

Defined at line 998.

Refer to the implementation for detailed semantics, side effects, and return values.

## `analyze_zeolite(structure: Structure, *, cutoffs: ZeoliteCutoffs=ZeoliteCutoffs(), criteria: ZeoliteCriteria=ZeoliteCriteria(), max_ring_size: int=16, calculate_rings: bool=True) -> Dict[str, object]`

Defined at line 1031.

Refer to the implementation for detailed semantics, side effects, and return values.

