# Changelog

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/CHANGELOG.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/CHANGELOG.ja.md)


- Corrected the runner separation: removed legacy standalone initialization from `runners/run_rmc.py`; `scripts/rmc.py` initializes configuration and calls the runner with explicit arguments.

## v0.1.6
- Added `scripts/rmc.py` as a thin launcher for `rmc_util.runners.run_rmc`, installed alongside editable `rmc_init.py` via `rmc_util install`. The runner implementation is not copied.


### Separation of runners and editable calculation parameters

- Moved the RMC execution workflow to package-managed `rmc_util.runners.run_rmc`, separating execution logic from user-editable initialization parameters.
- `rmc_init.py` remains the editable per-calculation script, installed into the working directory using `rmc_util install`; it calls the packaged runner.
- Updated the packaged script list to include **only** `scripts/rmc_init.py`. `rmc.py` is no longer copied to each working directory.
- Added the log-directory naming/backup helper for standalone RMC runs and combined workflows. Log numbering starts at 0 and the next directory name is determined from existing directories, without a centralized counter.
- Retained the existing `install.py` implementation and CLI (`rmc_util install [--force]`); existing files are skipped unless `--force` is supplied.
- This structure aligns with `vasp_util` and lets `rmc_dft` orchestrate the independently maintained runners, reducing duplicated scripts and version drift.

## v0.1.5

- Renamed `install_scripts.py` to `install.py` and changed the CLI entry point from `rmc_util-install` to `rmc_util`.
- Added `rmc_util install` to copy bundled, editable example scripts into the current directory.
- Added `rmc_util install --force` to overwrite existing files; without `--force`, existing files are skipped.
- Kept the existing bundled-script discovery and copying behavior.

Usage:

```bash
rmc_util install
rmc_util install --force
```

## v0.1.0

### DAT free/fixed format support expansion

Extended `.dat` handling for both free and fixed formats in accordance with the RMC_POT manual and reference samples.
The existing implementation model is preserved: free-format files are handled through their section/key structure, while
fixed-format files remain based on physical line positions.

### Free format

- Added read/write support for Lennard-Jones non-bonded potential settings in `[ NBPOT ]`.
- Added read/write support for `NMOVED-ATOMS` and multiple `CUSTOM-LINE` entries in `[ CUSTMOVE ]`.
- Added support for local invariance settings in `[ LOCINV ]`:
    - `LOC-MODE`
    - `LOC-R-SPACING`
    - `LOC-INT-FROM_SIGMA`
    - `LOC-INT-FROM_SIGMA-MASTER`
    - `LOC-INT-FROM_SIGMA-SCALABLE`
    - `LOC-INT-TO`
- Added support for non-periodic boundary-condition settings in `[ NOPER ]`:
    - `SAMPLE-RADIUS`
    - `RECENTRE-SPHERE`
- Added read/write support for `GAUSSIAN-SIGMA` in `[ VIBRAMP ]`.
- Added read/write support for the `[ CONC ]` advanced geometric constraint.
- Reused the existing free-format section/key handling; no new generic parser or unnecessary abstraction layer was
  introduced.

### Fixed format

- Preserved the existing physical-line-based handling of the fixed format.
- Added read/write support for the local invariance line used when `_LOCAL_INV` is enabled.
- Added read/write support for spherical-sample settings used when `_NO_PERIODIC` is enabled.
- Added read/write support for vibrational amplitudes used when `_VIBR_AMP` is enabled.
- Added insertion and removal of explicitly specified physical lines so optional fixed-format records can be handled
  without replacing the existing fixed-format model.
- Fixed-format positions are not determined from comments. Parsing does not depend on comment text or wording.
- Added a CP1252 fallback when an existing fixed-format file cannot be decoded as UTF-8.

### Scope

This update extends `.dat` handling required by the RMC_POT manual and reference samples, including Ar potential, CCl4
atomic/molecular cases, local invariance, flexible molecules, non-periodic calculations, vibrational amplitudes, and
advanced geometric constraints.

## v0.0.5 - 2026-10-12

- Updated the README with clearer installation instructions and descriptions of the current `rmc_util` functionality and
  usage.
- Documented handling of RMC_POT fixed and free formats through the common `RmcPotDat` API.
- Added an example of using `rmc_util` to handle RMC_POT from higher-level workflows such as RMC-DFT.

## v0.0.0 — 2026-10-07

### Initial release

- Extracted the RMC-related functionality from `rmc_dft` v0.6.13 into a standalone Python package named `rmc_util`.
- Included modules for working with RMC_POT input, configuration, and output data.
- Included RMC_POT file-conversion and analysis utilities.
- Prepared README files and documentation for RMC workflows.

**Origin:** This release was separated from `rmc_dft` **v0.6.13**.
