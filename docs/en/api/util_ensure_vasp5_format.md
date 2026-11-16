# `rmc_util.util.ensure_vasp5_format`

Source: `src/rmc_util/util/ensure_vasp5_format.py`

## `ensure_vasp5_format(poscar_name: str, element_info: Optional[Union[str, Sequence[str]]]=None, logger: Optional[XLogger]=XLogger())`

Set element labels on line 6 of a VASP file.
Convert a VASP4-type POSCAR to a VASP5-type POSCAR.
Repeated execution has no side effects.

Because the RMC_POT cfg format does not contain element names, conversion to POSCAR can be problematic.
This function converts it to VASP5 format (`cfg2poscar` produces VASP4 format without element information).

Args:
    poscar_name (str): POSCAR
    element_info (str): Filename containing element information or a list of elements
    logger (XLogger):

Returns:
    bool: True/False


## Methods


### Module Function `ensure_vasp5_format()`

- Definition location: line 10
- Description: Set element labels on line 6 of a VASP file.

## Arguments and Return Values Based on the Source Code


### `ensure_vasp5_format`

| Argument | Type annotation |
|---|---|
| `poscar_name` | `str` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |
| `logger` | `Optional[XLogger]` |

Return type annotation: `bool`. Definition location: `ensure_vasp5_format.py:10`.
