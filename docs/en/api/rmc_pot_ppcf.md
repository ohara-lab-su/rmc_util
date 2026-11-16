# `rmc_util.rmc_pot_ppcf`

Source: `src/rmc_util/rmc_pot_ppcf.py`

## Class `RmcPotPpcf`

The source contains no class-level explanatory docstring.

### `__init__(self, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Args:
    cfg_name (str):
    config (Config):
    logger (XLogger):

### `load(self)`

This method has no docstring. Refer to the implementation for details of its behavior.

### `get_r(self)`

This method has no docstring. Refer to the implementation for details of its behavior.

### `get_gij(self)`

This method has no docstring. Refer to the implementation for details of its behavior.

### `get_single(self, index: int)`

Return one partial g_ij(r) selected by its zero-based index.

### `get_labels(self)`

This method has no docstring. Refer to the implementation for details of its behavior.


## API List Based on the Implementation

This list was created from the function definitions in the provided `rmc_pot_ppcf(9).py`. The existing descriptions are retained above; argument types, return types, and side effects not explicitly stated are not inferred.

### Methods of `RmcPotPpcf`

| Method | Definition line | Description (start of docstring) |
|---|---:|---|
| `__init__()` | 17 | Args: |
| `load()` | 42 | No description in source |
| `get_r()` | 82 | No description in source |
| `get_gij()` | 85 | No description in source |
| `get_single()` | 88 | Return one partial g_ij(r) selected by its zero-based index. |
| `get_labels()` | 94 | No description in source |

## Argument and Return-Type List Based on Source Code

This section directly checks the function declarations and type annotations in the provided implementation. Arguments and return values without type annotations are marked “Not specified.” This does not mean that their runtime return value is `None`.

### `RmcPotPpcf.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `Optional[str]` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |

Return type annotation: `Not specified`. Definition: `rmc_pot_ppcf(9).py:17`.

### `RmcPotPpcf.load`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `None`. Definition: `rmc_pot_ppcf(9).py:42`.

### `RmcPotPpcf.get_r`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `np.ndarray`. Definition: `rmc_pot_ppcf(9).py:82`.

### `RmcPotPpcf.get_gij`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `np.ndarray`. Definition: `rmc_pot_ppcf(9).py:85`.

### `RmcPotPpcf.get_single`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `index` | `int` |

Return type annotation: `np.ndarray`. Definition: `rmc_pot_ppcf(9).py:88`.

### `RmcPotPpcf.get_labels`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `List[str]`. Definition: `rmc_pot_ppcf(9).py:94`.
