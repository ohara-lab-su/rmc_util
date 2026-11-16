# First RMC calculation

## 1. Prepare the working directory

```bash
pip install rmc-util
rmc_util install
```

Verify that `rmc.py` and `rmc_init.py` are present. Existing files are not overwritten by default.

## 2. Edit calculation parameters

Open `rmc_init.py` and configure the input structure, filenames, and execution parameters. Use the script shipped with your installed version as the authoritative source of parameter names.

## 3. Prepare input files

Provide the `.cfg` structure, `.dat` settings, experimental profiles, and any required FNC/topology inputs. `RmcPot.preprocess()` validates required inputs; it does not construct the starting structure.

## 4. Run

```bash
python rmc.py
```

## 5. Inspect results and rerun

Inspect the log and result files before modifying the calculation. When reusing DAT input, check the existing-format detection performed by `RmcPotDat.init(prefer_existing=True)`. Log directory indices are selected by scanning existing directories.
