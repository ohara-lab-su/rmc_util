# README execution and configuration examples

The examples cover installation, calculation parameters, and structural constraints. Numerical values and filenames are illustrative and must be adjusted to the target system.

## README code example 1

```bash
pip install rmc-util
```

## README code example 2

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst
```

## README code example 3

```bash
pip install .
```

## README code example 4

```bash
rmc_util install
```

## README code example 5

```bash
rmc_util install --force
```

## README code example 6

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(
    cfg_name="sample",
    auto_write=False,
    use_free_format=True,
)

rmc_dat.init(
    use_free_format=True,
    prefer_existing=True,
)

rmc_dat.set_comment("SiO2 sample", auto_write=False)
rmc_dat.set_density(0.0665715652, auto_write=False)
rmc_dat.set_cutoffs([1.9, 1.1, 1.9], auto_write=False)
rmc_dat.set_maximum_moves([0.01, 0.01], auto_write=False)
rmc_dat.set_r_spacing(0.025, auto_write=False)
rmc_dat.write()
```

## README code example 7

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(
    cfg_name="sample",
    use_free_format=True,
)

rmc_dat.init(
    use_free_format=True,
    prefer_existing=True,
)

rmc_dat.set_element_info(["Si", "O"])

rmc_dat.set_coord_constraint(
    central_type=1,
    neighbors=[
        (2, 1.40, 1.90),
    ],
    subconstraints=[
        (4, 1.0, 0.01),
    ],
    index=0,
)

rmc_dat.set_qn_constraint(
    central_type=1,
    first_neighbor_type=2,
    first_neighbor_minimum=1.45,
    first_neighbor_maximum=1.80,
    second_neighbors=[
        (1, 1.45, 1.80),
    ],
    coordination_number=4,
    fraction=1.0,
    sigma=0.04,
    index=0,
)
```

## README code example 8

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst, RmcPotLog

rmc_dat = RmcPotDat(
    cfg_name="sample",
    use_free_format=True,
)
rmc_dat.init(prefer_existing=True)

rmc_log = RmcPotLog(cfg_name="sample")

rmc = RmcPot(
    rmc_dat=rmc_dat,
    rmc_log=rmc_log,
    cfg_name="sample",
)

if not rmc.preprocess():
    raise RuntimeError("RMC_POT input validation failed.")

if not rmc.check_fnc_cutoff_consistency(cfg_name="sample"):
    raise RuntimeError("FNC and cutoff settings are inconsistent.")

try:
    run_ok = rmc.run()
finally:
    rmc.postprocess(
        cfg_name="sample",
    )

if not run_ok:
    raise RuntimeError("RMC_POT execution failed.")

hst = RmcPotHst(cfg_name="sample")
loop = hst.detect_convergence(
    rel_tol=1.0e-2,
    acc_tol=1.0e-3,
    min_consecutive=2,
)
```

## README code example 9

```bash
docs/build.sh
```

## README code example 10

```bash
rmc_util install
python rmc.py
```
