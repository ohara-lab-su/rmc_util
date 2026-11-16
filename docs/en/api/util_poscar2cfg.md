# `rmc_util.util.poscar2cfg`

Source: `src/rmc_util/util/poscar2cfg.py`

## `contcar2cfg(cfg_name: str, logger: Optional[Any]=None)`

2025.10.29 update: Added support for the CONTCAR type.
Separated the core functionality.

Args:
    cfg_name (str): Name used to save the CFG file
    logger (str):

Returns:

## `poscar2cfg(cfg_name: str, poscar_name: Optional[str]=None, logger: Optional[Any]=None)`

2025.10.29 update: Added support for the CONTCAR type.
Separated the core functionality.

Args:
    cfg_name (str): Name used to save the CFG file
    poscar_name (str):
    logger (Any):

Returns:

## `vasp2cfg(vasp_name: str, cfg_name: str=None, logger: Optional[Any]=None)`

2025.10.29 update: Added support for the CONTCAR type.

*) The function is named vasp2cfg rather than poscar2cfg because
   it is intended to convert xxx.vasp --> xxx.cfg,
   rather than poscar --> xxx.cfg.

Args:
    cfg_name (str): Reads the cfg_name.vasp file (equivalent to POSCAR).
                    If the cfg_name.vasp file does not exist,
                    reads CONTCAR.
    vasp_name (str):
    logger:

Returns:

## `convert_to_cfg(poscar_name: str='POSCAR', cfg_name: str='aaa', logger: Optional[Any]=None)`

Treats the contents of the file named `name` as POSCAR/CONTCAR and converts that file to CFG format.

Args:
    poscar_name (str): Reads the file with this name as-is
    cfg_name (str): Writes the output as cfg_name.cfg
    logger (XLogger):

Returns:


## API List Based on the Implementation

This list was created from the function definitions in the supplied `poscar2cfg(8).py`. The existing descriptions are retained above; argument and return types and side effects that are not explicitly stated have not been inferred.

### Module Function `contcar2cfg()`

- Definition location: Line 42
- Description: 2025.10.29 update: Added support for the CONTCAR type

### Module Function `poscar2cfg()`

- Definition location: Line 67
- Description: 2025.10.29 update: Added support for the CONTCAR type

### Module Function `vasp2cfg()`

- Definition location: Line 98
- Description: 2025.10.29 update: Added support for the CONTCAR type

### Module Function `convert_to_cfg()`

- Definition location: Line 137
- Description: Treats the contents of the file named `name` as POSCAR/CONTCAR and converts that file to CFG format

## Argument and Return Type List Based on the Source Code

This section lists the function declarations and type annotations verified directly against the supplied implementation. Arguments and return values without type annotations are marked "Not specified." This does not mean that the runtime return value is `None`.

### `contcar2cfg`

| Argument | Type annotation |
|---|---|
| `cfg_name` | `str` |
| `logger` | `Optional[Any]` |

Return type annotation: `Not specified`. Definition location: `poscar2cfg(8).py:42`.

### `poscar2cfg`

| Argument | Type annotation |
|---|---|
| `cfg_name` | `str` |
| `poscar_name` | `Optional[str]` |
| `logger` | `Optional[Any]` |

Return type annotation: `bool`. Definition location: `poscar2cfg(8).py:67`.

### `vasp2cfg`

| Argument | Type annotation |
|---|---|
| `vasp_name` | `str` |
| `cfg_name` | `str` |
| `logger` | `Optional[Any]` |

Return type annotation: `Not specified`. Definition location: `poscar2cfg(8).py:98`.

### `convert_to_cfg`

| Argument | Type annotation |
|---|---|
| `poscar_name` | `str` |
| `cfg_name` | `str` |
| `logger` | `Optional[Any]` |

Return type annotation: `bool`. Definition location: `poscar2cfg(8).py:137`.
