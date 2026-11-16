# `rmc_util.install`

Source: `src/rmc_util/install.py`

## `find_installed_scripts()`

Inspect the installation destination and distribution records, and retrieve each template with the same name only once.

## `install_scripts(destination: Path, *, force: bool=False)`

Place the templates. Overwrite existing files only when `force` is true.

## `main()`

Overwrite existing templates only when `--force` is specified.


## Methods


### Module Function `find_installed_scripts()`

- Definition line: 19
- Description: Inspect the installation destination and distribution records, and retrieve each template with the same name only once.

### Module Function `install_scripts()`

- Definition line: 41
- Description: Place the templates. Overwrite existing files only when `force` is true.

### Module Function `main()`

- Definition line: 76
- Description: Overwrite existing templates only when `--force` is specified.

## Arguments and Return Values

Arguments and return values without type annotations are marked “Not specified.” This does not imply that a function returns `None`.

### `find_installed_scripts`

| Argument | Type annotation |
|---|---|
| (None) | — |

Return type annotation: `list[Path]`. Definition location: `install.py:19`.

### `install_scripts`

| Argument | Type annotation |
|---|---|
| `destination` | `Path` |
| `force` | `bool` |

Return type annotation: `tuple[int, int]`. Definition location: `install.py:41`.

### `main`

| Argument | Type annotation |
|---|---|
| (None) | — |

Return type annotation: `None`. Definition location: `install.py:76`.
