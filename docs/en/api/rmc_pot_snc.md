# `rmc_util.rmc_pot_snc`

Source: `src/rmc_util/rmc_pot_snc.py`

## Class `RmcPotSnc`

Reads the Second Neighbour Constraint output from RMC_POT.

### `__init__(self, path: str)`

Reads ``*.snc``.

Args:
    path: The ``*.snc`` file to analyze.

### `load(self)`

Reloads the file and stores constraint information and coordination numbers for each central atom.

Raises:
    FileNotFoundError: If the specified file does not exist.
    ValueError: If a required section of ``*.snc`` cannot be interpreted.

### `get_qn_counts(self, constraint_index: int=0)`

Returns the Qn distribution of central atoms recorded in the specified constraint block.

Args:
    constraint_index: Zero-based constraint index.

Returns:
    A dictionary mapping Qn values to counts of central atoms.

### `get_common_qn_counts(self)`

Checks that all constraints contain the same coordination-number sequence and returns the distribution.

Returns:
    A dictionary mapping Qn values to counts of central atoms.

Raises:
    ValueError: If the coordination numbers of central atoms differ between constraints.


## Methods


### Methods of `RmcPotSnc`

| Method | Definition line | Description (start of docstring) |
|---|---:|---|
| `__init__()` | 17 | Reads \`\`*.snc\`\`. |
| `load()` | 27 | Reloads the file and stores constraint information and coordination numbers for each central atom. |
| `get_qn_counts()` | 69 | Returns the Qn distribution of central atoms recorded in the specified constraint block. |
| `get_common_qn_counts()` | 82 | Checks that all constraints contain the same coordination-number sequence and returns the distribution. |

## Argument and Return-Type List Based on Source Code

This section directly checks the function declarations and type annotations in the provided implementation. Arguments and return values without type annotations are marked “Not specified.” This does not mean that their runtime return value is `None`.

### `RmcPotSnc.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `path` | `str` |

Return type annotation: `None`. Definition: `rmc_pot_snc.py:17`.

### `RmcPotSnc.load`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `None`. Definition: `rmc_pot_snc.py:27`.

### `RmcPotSnc.get_qn_counts`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `constraint_index` | `int` |

Return type annotation: `Dict[int, int]`. Definition: `rmc_pot_snc.py:69`.

### `RmcPotSnc.get_common_qn_counts`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `Dict[int, int]`. Definition: `rmc_pot_snc.py:82`.
