# `rmc_util.rmc_pot_hst`

Reads RMC_POT `.hst` history files and provides per-loop statistics and convergence diagnostics.

Source: `src/rmc_util/rmc_pot_hst.py`

## `RmcPotHst`

Parses the eight history columns `generated`, `tried`, `accepted`, `time`, `tried_per_gen`, `acc_per_tried`, `chi2_tot`, and `chi2_set1`. Numeric rows following the table header form the history records.

### `__init__(self, hst_name=None, cfg_name=None, config=None, logger=None)`

File selection priority is `hst_name`, then `cfg_name`, then `config`. `hst_name` is used as supplied; `cfg_name` receives the `.hst` suffix.

**Implementation note:** When only `config` is supplied, the implementation constructs `Config("config.yaml")` instead of using the supplied object.

```python
RmcPotHst(hst_name="sample.hst")
RmcPotHst(cfg_name="sample")
```

### `read_chi2(self)`

Returns `(steps, chi2)`. Because `.hst` does not provide a separate step column, `steps` are zero-based record indices.

### `detect_convergence(self, rel_tol=0.01, acc_tol=0.001, min_consecutive=3)`

Checks both the relative improvement in `chi2_tot` between consecutive loops and the `accepted/tried` ratio.

```text
delta = (chi2[i - 1] - chi2[i]) / chi2[i - 1]
delta < rel_tol
accepted / tried < acc_tol
```

If the conditions hold for `min_consecutive` consecutive loops, returns the first loop index in that sequence; otherwise returns `None`.

### `detect_convergence_set1(self, rel_tol=0.01, acc_tol=0.001, min_consecutive=2)`

Applies the same convergence criteria to `chi2_set1` (`chi2/F(Q)_set#1` in `.hst`) instead of `chi2_tot`.

### `get_num_rmc_loops(self)`

Returns the number of parsed history records as an integer.

## History value accessors

### `get_generated(self, loop_index=None)`

Retrieves history column `generated` (number of generated moves).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[int, List[int]]`.

### `get_tried(self, loop_index=None)`

Retrieves history column `tried` (number of attempted moves).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[int, List[int]]`.

### `get_accepted(self, loop_index=None)`

Retrieves history column `accepted` (number of accepted moves).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[int, List[int]]`.

### `get_time(self, loop_index=None)`

Retrieves history column `time` (time recorded in the history).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[int, List[int]]`.

### `get_tried_per_generated(self, loop_index=None)`

Retrieves history column `tried_per_gen` (ratio of attempted to generated moves).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[float, List[float]]`.

### `get_accepted_per_tried(self, loop_index=None)`

Retrieves history column `acc_per_tried` (ratio of accepted to attempted moves).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[float, List[float]]`.

### `get_chi2_tot(self, loop_index=None)`

Retrieves history column `chi2_tot` (chi-squared measure for all data sets).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[float, List[float]]`.

### `get_chi2_set1(self, loop_index=None)`

Retrieves history column `chi2_set1` (chi-squared measure for data set 1).
 
With `loop_index=None`, returns a list for all records; an integer index selects one record.

Returns: `Union[float, List[float]]`.

## Implementation mapping

| Method | Source line |
|---|---:|
| `__init__` | 41 |
| `read_chi2` | 202 |
| `detect_convergence` | 231 |
| `detect_convergence_set1` | 327 |
| `get_num_rmc_loops` | 368 |
| `get_generated` | 382 |
| `get_tried` | 413 |
| `get_accepted` | 441 |
| `get_time` | 469 |
| `get_tried_per_generated` | 497 |
| `get_accepted_per_tried` | 525 |
| `get_chi2_tot` | 553 |
| `get_chi2_set1` | 575 |
