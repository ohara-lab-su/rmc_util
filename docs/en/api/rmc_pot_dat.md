# `rmc_util.rmc_pot_dat`

Source: `src/rmc_util/rmc_pot_dat.py`

## Class `RmcPotDat`

A transparent wrapper class that handles fixed-format and free-format RmcPotDat through a unified interface.

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, auto_write: bool=True, use_free_format: Optional[bool]=None)`

Creates an RmcPotDat wrapper.

Args:
    config: Config instance.
    logger: XLogger instance.
    cfg_name: Filename excluding the *.dat extension.
    auto_write: Automatic save flag.
    use_free_format: Default format used when creating a new *.dat file.
        True selects free format, False selects fixed format, and None defaults to free format.

Notes:
    The constructor does not read or create a *.dat file.
    Actual initialization is performed by init().

### `set_free_format(self, use_free_format: bool)`

Sets the format to use when creating a new ``*.dat`` file.

Before initialization, updates the stored format setting. After initialization, it does not
change the format of the current ``*.dat`` file, but logs the format actually in use.

### `set_cfg_name(self, cfg_name: str)`

Changes the configuration name used for reading and writing.

Before initialization, changes only the name held by the wrapper. After initialization,
propagates the same name to the internal implementation.

### `init(self, *, use_free_format: Optional[bool]=None, prefer_existing: bool=True)`

Reads a *.dat file or creates a new one from the initial values of the respective format class.

Args:
    use_free_format: Format for new files. If None, uses the format stored by the constructor or
        set_free_format().
    prefer_existing: Prioritizes an existing *.dat file when present.
        If False, backs up the existing file and recreates it using the initial values
        of the specified format.

### `is_free_format(self)`

Returns whether the currently used underlying implementation is free-format.

If not initialized, lazily reads an existing ``*.dat`` file or creates an initial file
before determining the format.

## `main()`

Usage example that selects free-format DAT and writes basic settings.

Notes:
    If ``sample_dat.dat`` does not exist, creates a default free-format DAT file.
    SNC-related operations are delegated to ``RmcPotDatFree`` as before.


## API List Based on the Implementation

This list was created from the function definitions in the provided `rmc_pot_dat(20261116-081310).py`. The existing descriptions are retained above; argument and return types and side effects that are not explicitly specified have not been inferred.

### Methods of `RmcPotDat`

| Method | Definition line | Description (beginning of docstring) |
|---|---:|---|
| `__init__()` | 25 | Creates an RmcPotDat wrapper. |
| `set_free_format()` | 55 | Sets the format to use when creating a new \`\`*.dat\`\` file. |
| `set_cfg_name()` | 71 | Changes the configuration name used for reading and writing. |
| `init()` | 82 | Reads a *.dat file or creates a new one from the initial values of the respective format class. |
| `is_free_format()` | 155 | Returns whether the currently used underlying implementation is free-format. |

### Module Function `main()`

- Definition line: 181
- Description: Usage example that selects free-format DAT and writes basic settings.

## Argument and Return Type List Based on Source Code

This section directly checks the function declarations and type annotations in the provided implementation. Arguments and return values without type annotations are marked "Not specified". This does not mean that the runtime return value is `None`.

### `RmcPotDat.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |
| `cfg_name` | `Optional[str]` |
| `auto_write` | `bool` |
| `use_free_format` | `Optional[bool]` |

Return type annotation: `None`. Definition: `rmc_pot_dat(20261116-081310).py:25`.

### `RmcPotDat.set_free_format`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `use_free_format` | `bool` |

Return type annotation: `None`. Definition: `rmc_pot_dat(20261116-081310).py:55`.

### `RmcPotDat.set_cfg_name`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `str` |

Return type annotation: `None`. Definition: `rmc_pot_dat(20261116-081310).py:71`.

### `RmcPotDat.init`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `use_free_format` | `Optional[bool]` |
| `prefer_existing` | `bool` |

Return type annotation: `None`. Definition: `rmc_pot_dat(20261116-081310).py:82`.

### `RmcPotDat.is_free_format`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `bool`. Definition: `rmc_pot_dat(20261116-081310).py:155`.

### `main`

| Argument | Type annotation |
|---|---|
| (None) | — |

Return type annotation: `None`. Definition: `rmc_pot_dat(20261116-081310).py:181`.
