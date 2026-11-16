# `rmc_util.util.cfg2poscar`

Source: `src/rmc_util/util/cfg2poscar.py`

## `parse_elements(element_info: Optional[Union[str, Sequence[str]]]=None)`

This function has no docstring. Consult the implementation for details of its behavior.

## `make_vasp_elements_line(elements: List[str])`

This function has no docstring. Consult the implementation for details of its behavior.

## `cfg2poscar(cfg_name: str, vasp_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None, logger: Optional[Any]=None)`

Convert RMCPOT cfg format to POSCAR format.
Standalone version without SAE (noLIB).

Args:
    cfg_name (str):
    vasp_name (str):
    element_info (str or Sequence[str]):
    logger (Any):
Returns:
    bool:


## Methods


### Module Function `parse_elements()`

- Definition location: line 42
- Description: No description in the source code.

### Module Function `make_vasp_elements_line()`

- Definition location: line 87
- Description: No description in the source code.

### Module Function `cfg2poscar()`

- Definition location: line 99
- Description: Convert RMCPOT cfg format to POSCAR format.

## Arguments and Return Values Based on the Source Code


### `parse_elements`

| Argument | Type annotation |
|---|---|
| `element_info` | `Optional[Union[str, Sequence[str]]]` |

Return type annotation: `Optional[List[str]]`. Definition location: `cfg2poscar.py:42`.

### `make_vasp_elements_line`

| Argument | Type annotation |
|---|---|
| `elements` | `List[str]` |

Return type annotation: `str`. Definition location: `cfg2poscar.py:87`.

### `cfg2poscar`

| Argument | Type annotation |
|---|---|
| `cfg_name` | `str` |
| `vasp_name` | `Optional[str]` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |
| `logger` | `Optional[Any]` |

Return type annotation: `bool`. Definition location: `cfg2poscar.py:99`.
