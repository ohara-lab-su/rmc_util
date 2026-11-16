# `rmc_util.rmc_pot_fit`

Source: `src/rmc_util/rmc_pot_fit.py`

## Class `RmcPotFit`

A class that reads RMC_POT .fit files and stores Q, F(Q), renormalized F(Q)_exp, and related data.

### `__init__(self, *, fit_name: Optional[str]=None, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Args:
    fit_name (str): Name including aaa.fit
    cfg_name (str): cfg_name.fit (full filename including .fit)
    config (Config):
    logger (XLogger):

### `read_fit(self, filename: Optional[str]=None)`

Reads the .fit file and stores the main data columns.
self.filename: fullname

Args:
    filename:

Returns:

### `get_S_calc(self)`

S_calc(Q) = F_calc + 1
RMC_POT uses this form of F(Q).

### `get_S_exp(self)`

S_exp(Q) = renormalized F_exp + 1

### `get_S_exp_original(self)`

S_exp_original(Q) = original F_exp + 1

### `as_dict(self)`

Used to return the data in dictionary form.


## API List Based on the Implementation

This list was created from the function definitions in the provided `rmc_pot_fit(7).py`. The existing descriptions are retained above; argument and return types and side effects that are not explicitly specified have not been inferred.

### Methods of `RmcPotFit`

| Method | Definition line | Description (beginning of docstring) |
|---|---:|---|
| `__init__()` | 20 | Args: |
| `read_fit()` | 59 | Reads the .fit file and stores the main data columns. |
| `get_S_calc()` | 114 | S_calc(Q) = F_calc + 1 |
| `get_S_exp()` | 136 | S_exp(Q) = renormalized F_exp + 1 |
| `get_S_exp_original()` | 140 | S_exp_original(Q) = original F_exp + 1 |
| `as_dict()` | 144 | Used to return the data in dictionary form. |

## Argument and Return Type List Based on Source Code

This section directly checks the function declarations and type annotations in the provided implementation. Arguments and return values without type annotations are marked "Not specified". This does not mean that the runtime return value is `None`.

### `RmcPotFit.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `fit_name` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |

Return type annotation: `Not specified`. Definition: `rmc_pot_fit(7).py:20`.

### `RmcPotFit.read_fit`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `filename` | `Optional[str]` |

Return type annotation: `Optional[bool]`. Definition: `rmc_pot_fit(7).py:59`.

### `RmcPotFit.get_S_calc`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `List[float]`. Definition: `rmc_pot_fit(7).py:114`.

### `RmcPotFit.get_S_exp`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `List[float]`. Definition: `rmc_pot_fit(7).py:136`.

### `RmcPotFit.get_S_exp_original`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `List[float]`. Definition: `rmc_pot_fit(7).py:140`.

### `RmcPotFit.as_dict`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `Dict[str, List[float]]`. Definition: `rmc_pot_fit(7).py:144`.
