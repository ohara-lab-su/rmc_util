# `rmc_util.rmc_pot`

Source: `src/rmc_util/rmc_pot.py`

## Class `RmcPot`

Utility class for managing and running local RMC commands.
And parsing configuration files.

### `__init__(self, *, rmc_log: Optional[RmcPotLog]=None, rmc_dat: Optional[RmcPotDat]=None, config: Optional[Config]=None, cfg_name: Optional[str]=None, use_free_format: bool=False, logger: Optional[XLogger]=None)`

When a config instance is supplied, cfg_name is not required.

Args:
    rmc_log: Instance for processing RMC_POT logs
    rmc_dat: Instance for processing RMC_POT DAT files
    config (Config): All instances share the same Config()
    logger (XLogger): All instances share the same XLogger()
    cfg_name (str): cfg-filename

### `rmc_dat(self)`

This method has no docstring. Refer to the implementation for details.

### `set_cfg_name(self, cfg_name: str)`

This method has no docstring. Refer to the implementation for details.

### `set_tag(self, tag_name: str, *args)`

Compatibility interface for calling set_xxx methods of RmcPotData.

Args:
    tag_name (str): Tag name (e.g., 'cutoffs', 'potential'）
    *args: set_xxx Arguments passed to

### `get_tag(self, tag_name: str, *args)`

Compatibility interface for calling get_xxx methods of RmcPotData.

Args:
    tag_name (str): Tag name (e.g., 'cutoffs', 'potential'）
    *args: get_xxx Arguments passed to get_xxx (if necessary)

Returns:
    Any: Return value of the corresponding get_xxx method

### `init(self, cfg_name: str)`

RMC-DFT begins with RMC. However, because the structural file starts from a VASP-based format, this routine does not explicitly initialize it on the rmc_pot side. This is a dummy compatibility interface.

Args:
    cfg_name:

Returns:

### `preprocess(self)`

 Check the input files required before running RMC_POT.

This code assumes that the RMC_POT inputs are prepared.
 1. Stop if the experimental profile (e.g., fesi04_smbt-rmc.txt) does not exist in the current working directory.
 2. Stop if label.txt does not exist.

 *) Because initial structure conversion can easily lead to misunderstandings, the RmcPot class does not perform it automatically in Preprocess().


 Returns:
     bool:
         ``True`` if all required input files exist and the experimental data filename was retrieved successfully. ``False`` if inputs are missing or configuration is invalid.

### `postprocess(self, log_dir: Optional[str]=None, cfg_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None)`

Postprocessing

For running DFT after RMC:
1) DATA-collect
2) BACKUP
3) xxx.CFG --> POSCAR (VASP4) conversion(xxx.vasp) --> VASP5 conversion(xxx.vasp)

The basic assumption is to go through POSCAR even when using other codes. Having postprocess produce POSCAR therefore avoids inconsistencies when using other libraries.

Args:
    log_dir (str): log_dir for RMC
    cfg_name (str): cfg_name and vasp_name are assumed equal (the default is the cfg_name argument to the constructor)
    element_info (str | list): Element information

Returns:
    bool:

### `check_fnc_cutoff_consistency(self, cfg_name: Optional[str]=None)`

Before running RMC_POT, check consistency between rmin in *.fnc and the hard-sphere cutoff in *.dat.

Rather than fixing a mapping between FNC constraint type numbers and pairs of atomic species, determine the corresponding RMC atom types from the actual atom-index pairs recorded in *.fnc and the atomic-species blocks in *.cfg.

### `run(self, cfg_name: Optional[str]=None, blocking: Optional[bool]=True, save_stdout: Optional[bool]=True)`

Run RMC

Args:
    cfg_name (str):
    blocking (bool)_:  Launch subprocess in blocking mode (default: True)
    save_stdout (bool): If True, save the log to a file

Returns:
    bool: Whether execution completed successfully

### `ensure_vasp5_format(poscar_name: str, element_info: Optional[str]=None, logger: XLogger=XLogger())`

RMC_POT has no information on elemental species, so conversion can only produce an equivalent of a VASP4 POSCAR. This utility method adds elemental-species information to the VASP4-format POSCAR.

Args:
    poscar_name:
    element_info:
    logger:

Returns:

### `cfg2poscar(self, cfg_name: Optional[str]=None, vasp_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None)`

Convert CFG to POSCAR

Because it is generated directly from CFG, it lacks elemental-species information and is therefore a VASP4-format POSCAR.

Args:
    cfg_name (str):  xxx.cfg（base name without extension expected）
    vasp_name (str): xxx.vasp（base name without extension expected）
    element_info (str or Sequence[str]): ["Fe","Si",,,]


## API list based on the implementation

This list was compiled from the function definitions in the provided `rmc_pot.py`. The existing descriptions are preserved above; types of arguments and return values and side effects not explicitly stated have not been inferred.

### Methods of `RmcPot`

| Method | Definition line | Description (beginning of docstring) |
|---|---:|---|
| `__init__()` | 34 | When a config instance is supplied, cfg_name is not required. |
| `rmc_dat()` | 114 | No description in source |
| `set_cfg_name()` | 117 | No description in source |
| `set_tag()` | 132 | Compatibility interface for calling set_xxx methods of RmcPotData. |
| `get_tag()` | 148 | Compatibility interface for calling get_xxx methods of RmcPotData. |
| `init()` | 167 | RMC-DFT begins with RMC, but the structural file starts from a VASP-based format |
| `preprocess()` | 181 | Check the input files required before running RMC_POT. |
| `postprocess()` | 261 | Postprocessing |
| `check_fnc_cutoff_consistency()` | 342 | Before running RMC_POT, check the rmin in *.fnc against the hard-sphere cutoff in *.dat |
| `run()` | 729 | Run RMC |
| `ensure_vasp5_format()` | 839 | RMC_POT lacks elemental-species information and can only generate the equivalent of a VASP4 POSCAR |
| `cfg2poscar()` | 863 | Convert CFG to POSCAR |

## Argument and return-value list based on source code

This section directly checks the function declarations and type annotations in the provided implementation. Arguments and return values without type annotations are marked “Not specified”; this does not mean their runtime return value is `None`.

### `RmcPot.__init__`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `rmc_log` | `Optional[RmcPotLog]` |
| `rmc_dat` | `Optional[RmcPotDat]` |
| `config` | `Optional[Config]` |
| `cfg_name` | `Optional[str]` |
| `use_free_format` | `bool` |
| `logger` | `Optional[XLogger]` |

Return type annotation: `None`。Definition location: `rmc_pot.py:34`。

### `RmcPot.rmc_dat`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `Not specified`。Definition location: `rmc_pot.py:114`。

### `RmcPot.set_cfg_name`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `str` |

Return type annotation: `Not specified`。Definition location: `rmc_pot.py:117`。

### `RmcPot.set_tag`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `tag_name` | `str` |
| `args` | `Not specified` |

Return type annotation: `None`。Definition location: `rmc_pot.py:132`。

### `RmcPot.get_tag`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `tag_name` | `str` |
| `args` | `Not specified` |

Return type annotation: `Not specified`。Definition location: `rmc_pot.py:148`。

### `RmcPot.init`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `str` |

Return type annotation: `Not specified`。Definition location: `rmc_pot.py:167`。

### `RmcPot.preprocess`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |

Return type annotation: `bool`。Definition location: `rmc_pot.py:181`。

### `RmcPot.postprocess`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `log_dir` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |

Return type annotation: `bool`。Definition location: `rmc_pot.py:261`。

### `RmcPot.check_fnc_cutoff_consistency`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `Optional[str]` |

Return type annotation: `bool`。Definition location: `rmc_pot.py:342`。

### `RmcPot.run`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `Optional[str]` |
| `blocking` | `Optional[bool]` |
| `save_stdout` | `Optional[bool]` |

Return type annotation: `bool`。Definition location: `rmc_pot.py:729`。

### `RmcPot.ensure_vasp5_format`

| Argument | Type annotation |
|---|---|
| `poscar_name` | `str` |
| `element_info` | `Optional[str]` |
| `logger` | `XLogger` |

Return type annotation: `bool`。Definition location: `rmc_pot.py:839`。

### `RmcPot.cfg2poscar`

| Argument | Type annotation |
|---|---|
| `self` | `Not specified` |
| `cfg_name` | `Optional[str]` |
| `vasp_name` | `Optional[str]` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |

Return type annotation: `bool`。Definition location: `rmc_pot.py:863`。

