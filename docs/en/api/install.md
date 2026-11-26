# `rmc_util.install`

This module deploys calculation scripts and the configuration template included in the installed Python distribution to a specified directory. See the [installation guide](../guide/installation.md) for CLI usage.

## `find_installed_scripts() -> list[Path]`

Searches `share/rmc_util/scripts` under the directory returned by `sysconfig.get_path("data")` and the installed file records provided by `importlib.metadata.distribution("rmc-util")`. Returns a name-sorted list of `Path` objects, with duplicate filenames included only once.

## `install_scripts(destination: Path, *, force: bool = False, script_name: str | None = None) -> tuple[int, int]`

Copies the bundled files to `destination`. With `script_name=None` it copies all files, and with a filename it copies one file. The `.py` and `.yml` extensions are optional. An unknown name raises `ValueError`. Existing files are skipped when `force=False` and overwritten when `force=True`. Raises `IsADirectoryError` if a target path is a directory. Returns `(number_copied, number_skipped)`. On POSIX systems, adds executable permissions to `rmc.py`. Raises `RuntimeError` if no bundled files are found.

```python
from pathlib import Path
from rmc_util.install import install_scripts

copied, skipped = install_scripts(Path.cwd(), force=False)
```

## `main() -> None`

The CLI entry point. `rmc_util list` shows filenames and descriptions. `rmc_util install [all|script|filename] [--force]` deploys files and reports the copied and skipped counts. Invalid arguments and unknown filenames exit with status 2.
