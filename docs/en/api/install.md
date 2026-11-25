# `rmc_util.install`

This module deploys calculation scripts and the configuration template included in the installed Python distribution to a specified directory. See the [installation guide](../guide/installation.md) for CLI usage.

## `find_installed_scripts() -> list[Path]`

Searches `share/rmc_util/scripts` under the directory returned by `sysconfig.get_path("data")` and the installed file records provided by `importlib.metadata.distribution("rmc-util")`. Returns a name-sorted list of `Path` objects, with duplicate filenames included only once.

## `install_scripts(destination: Path, *, force: bool = False) -> tuple[int, int]`

Copies the bundled scripts and configuration template to `destination`. Existing files are skipped when `force=False` and overwritten when `force=True`. Raises `IsADirectoryError` if a target path is a directory. Returns `(number_copied, number_skipped)`. On POSIX systems, adds executable permissions to `rmc.py`. Raises `RuntimeError` if no bundled files are found.

```python
from pathlib import Path
from rmc_util.install import install_scripts

copied, skipped = install_scripts(Path.cwd(), force=False)
```

## `main() -> None`

The CLI entry point. Handles `rmc_util install` and `rmc_util install --force`, printing the copied and skipped counts. Other arguments print usage to standard error and exit with status 2.
