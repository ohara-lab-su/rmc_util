# `rmc_util.rmc_pot_log`

Source: `src/rmc_util/rmc_pot_log.py`

## Class `RmcPotLog`

Reads RMC_POT log files and provides calculation status and statistics.

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, log_filename: Optional[str]=None)`

When a config instance is supplied, cfg_name is not required.

Args:
    config (Config): The shared Config() instance.
    logger (XLogger): The shared XLogger() instance.
    cfg_name (str):
    log_filename (str): Specify the log filename when RMC output is redirected to a job log.
                        Otherwise, the log filename is cfg_name.log.

### `load_log(self, log_filename: str=None)`

Read the log file if it exists and
store its contents in self._log_lines.
(The complete file contents are retained.)

### `set_cfg_name(self, cfg_name: str)`



### `get_cfg_name(self)`



### `is_finished(self)`

Determine whether the final RMC section of the log completed successfully.

- No RMC section appears       → False
- The final RMC section has only a start marker   → False
- The final RMC section has start and end markers   → True

Here, “final” refers to the last
RMC_POT++ program ... start block in the log.

### `get_num_rmc_block(self)`

Return the number of RMC sections (start blocks) in the log.
An incomplete block is also counted.

### `get_num_rmc_loop(self, block_index: int)`

Count the loops in an RMC block.
Args:
    block_index:

Returns:

### `get_generated(self, block: int, loop: int)`



### `get_tried(self, block: int, loop: int)`



### `get_accepted(self, block: int, loop: int)`



### `get_chi2_tot(self, block: int, loop: int)`

The name uses tot to align with Hst terminology (formerly global).
(Take care when comparing the meaning of the values.)

Possibly
log side (global)
hst side (total)
refer to the same quantity.

Args:
    block:
    loop:

Returns:

### `get_chi2_dataset(self, block: int, loop: int)`

dataset refers to an individual dataset rather than the global value.

Previously,
Hst uses set1 (specific set)
The log uses dataset (individual set)
The statistical populations may differ.

Args:
    block:
    loop:

Returns:

### `get_rw(self, block: int, loop: int)`



### `get_tried_per_generated(self, block: int, loop: int)`



### `get_accepted_per_tried(self, block: int, loop: int)`



### `clear(self, cfg_name: str)`

Remove RMC_POT output files.

Args:
    cfg_name (str):

Returns:

### `remove_file(self, filename: str)`

Remove the specified file from the current working directory.

Args:
    filename (str): Filename to remove (relative or absolute path).

### `collect_result(self)`



### `backup_result(self, log_dir: Optional[str]=None, cfg_name: Optional[str]=None)`

Copy RMC log files to the specified directory.

Args:
    log_dir (str): Directory to copy the log files to.
    cfg_name (str): Name of the configuration file.


## API listing

### `RmcPotLog` methods

| Method | Definition line | Description (first line of docstring) |
|---|---:|---|
| `__init__()` | 21 | When a config instance is supplied, cfg_name is not required. |
| `load_log()` | 65 | Read the log file if it exists and |
| `set_cfg_name()` | 99 | — |
| `get_cfg_name()` | 109 | — |
| `is_finished()` | 521 | Determine whether the final RMC section of the log completed successfully. |
| `get_num_rmc_block()` | 552 | Return the number of RMC sections (start blocks) in the log. |
| `get_num_rmc_loop()` | 560 | Count the loops in an RMC block. |
| `get_generated()` | 584 | — |
| `get_tried()` | 594 | — |
| `get_accepted()` | 604 | — |
| `get_chi2_tot()` | 614 | The name uses tot to align with Hst terminology (formerly global). |
| `get_chi2_dataset()` | 636 | dataset refers to an individual dataset rather than the global value. |
| `get_rw()` | 657 | — |
| `get_tried_per_generated()` | 663 | — |
| `get_accepted_per_tried()` | 677 | — |
| `clear()` | 695 | Remove RMC_POT output files. |
| `remove_file()` | 740 | Remove the specified file from the current working directory. |
| `collect_result()` | 759 | — |
| `backup_result()` | 762 | Copy RMC log files to the specified directory. |

## Argument and return type annotations

### `RmcPotLog.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |
| `cfg_name` | `Optional[str]` |
| `log_filename` | `Optional[str]` |

Return type annotation: `None`。Defined at: `src/rmc_util/rmc_pot_log.py:21`。

### `RmcPotLog.load_log`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `log_filename` | `str` |

Return type annotation: `None`。Defined at: `src/rmc_util/rmc_pot_log.py:65`。

### `RmcPotLog.set_cfg_name`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `cfg_name` | `str` |

Return type annotation: `None`。Defined at: `src/rmc_util/rmc_pot_log.py:99`。

### `RmcPotLog.get_cfg_name`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |

Return type annotation: `str`。Defined at: `src/rmc_util/rmc_pot_log.py:109`。

### `RmcPotLog.is_finished`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |

Return type annotation: `bool`。Defined at: `src/rmc_util/rmc_pot_log.py:521`。

### `RmcPotLog.get_num_rmc_block`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |

Return type annotation: `int`。Defined at: `src/rmc_util/rmc_pot_log.py:552`。

### `RmcPotLog.get_num_rmc_loop`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block_index` | `int` |

Return type annotation: `int`。Defined at: `src/rmc_util/rmc_pot_log.py:560`。

### `RmcPotLog.get_generated`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[int]`。Defined at: `src/rmc_util/rmc_pot_log.py:584`。

### `RmcPotLog.get_tried`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[int]`。Defined at: `src/rmc_util/rmc_pot_log.py:594`。

### `RmcPotLog.get_accepted`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[int]`。Defined at: `src/rmc_util/rmc_pot_log.py:604`。

### `RmcPotLog.get_chi2_tot`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[float]`。Defined at: `src/rmc_util/rmc_pot_log.py:614`。

### `RmcPotLog.get_chi2_dataset`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[float]`。Defined at: `src/rmc_util/rmc_pot_log.py:636`。

### `RmcPotLog.get_rw`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[float]`。Defined at: `src/rmc_util/rmc_pot_log.py:657`。

### `RmcPotLog.get_tried_per_generated`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[float]`。Defined at: `src/rmc_util/rmc_pot_log.py:663`。

### `RmcPotLog.get_accepted_per_tried`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `block` | `int` |
| `loop` | `int` |

Return type annotation: `Optional[float]`。Defined at: `src/rmc_util/rmc_pot_log.py:677`。

### `RmcPotLog.clear`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `cfg_name` | `str` |

Return type annotation: `None`。Defined at: `src/rmc_util/rmc_pot_log.py:695`。

### `RmcPotLog.remove_file`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `filename` | `str` |

Return type annotation: `bool`。Defined at: `src/rmc_util/rmc_pot_log.py:740`。

### `RmcPotLog.collect_result`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |

Return type annotation: `Not annotated`。Defined at: `src/rmc_util/rmc_pot_log.py:759`。

### `RmcPotLog.backup_result`

| Argument | Type annotation |
|---|---|
| `self` | `Not annotated` |
| `log_dir` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |

Return type annotation: `Not annotated`。Defined at: `src/rmc_util/rmc_pot_log.py:762`。

