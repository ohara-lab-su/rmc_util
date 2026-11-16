# Calculation parameters: fixed and free formats

`RmcPotDat` operates on fixed-format and free-format `.dat` files through the same Python API. **The setters are shared; `init()` selects the file format.** With `prefer_existing=True`, detection of an existing file takes precedence over `use_free_format`. To select a format for a new file, ensure that the target `.dat` does not already exist. `prefer_existing=False` replaces an existing file after creating a `.bak_init` backup.

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(cfg_name="sample", auto_write=False)
rmc_dat.init(use_free_format=True, prefer_existing=True)  # False selects fixed format
rmc_dat.set_comment("comment SiO2")
rmc_dat.set_density(0.0665715652)
rmc_dat.set_cutoffs([2.40, 1.25, 2.10])
rmc_dat.set_maximum_moves([0.01, 0.01])
rmc_dat.set_sigma_factor(0.05)
rmc_dat.set_moveout_option(True)
rmc_dat.set_time_and_save(15, 1)
rmc_dat.set_exp_range(1, 588)
rmc_dat.set_r_spacing(0.025)
rmc_dat.set_data_flags([0, 0, 1, 0])
rmc_dat.set_swap_settings(0.0, 0)
rmc_dat.set_num_atoms_per_move(1)
rmc_dat.write()
```

`set_density()` sets number density (Å⁻³), `set_cutoffs()` minimum interatomic distances (Å) for each species pair, `set_maximum_moves()` maximum displacements (Å) for each species, and `set_r_spacing()` the radial histogram bin width (Å). `set_time_and_save(15, 1)` configures run and save times. `set_exp_range(1, 588)` specifies the experimental-data point range, and `set_data_flags([0, 0, 1, 0])` selects data types. These are one set of SiO₂ parameters, not universal values; adapt them to the measured points, density, and species order.

## Examples for different numbers of atomic species

For $n$ species, `set_cutoffs()` takes $n(n+1)/2$ values; `set_maximum_moves()` takes $n$ values. The following blocks are **independent alternatives**, not settings to apply together.

**SiO₂ (Si, O)**

```python
rmc_dat.set_density(0.0665715652)
rmc_dat.set_cutoffs([2.40, 1.25, 2.10])  # Si-Si, Si-O, O-O
rmc_dat.set_maximum_moves([0.01, 0.01])  # Si, O
```

**Fe–Si–B (Fe, Si, B)**

```python
rmc_dat.set_density(0.0915)
rmc_dat.set_cutoffs([2.2, 1.9, 1.75, 1.8, 1.75, 1.5])
# Fe-Fe, Fe-Si, Fe-B, Si-Si, Si-B, B-B
rmc_dat.set_maximum_moves([0.1, 0.1, 0.1])
```

**Li₃PO₄ (Li, P, O)**

```python
rmc_dat.set_density(0.0772877)
rmc_dat.set_cutoffs([
    1.8,  # Li-Li
    2.0,  # Li-P
    1.7,  # Li-O
    2.5,  # P-P
    1.3,  # P-O
    2.0,  # O-O
])
rmc_dat.set_maximum_moves([0.1, 0.1, 0.1])
```

**Zeolite (Si, Al, O, Na)**

```python
rmc_dat.set_density(0.0570880440)
rmc_dat.set_cutoffs([
    2.10, 2.20, 1.35, 2.20,  # Si-Si, Si-Al, Si-O, Si-Na
    2.20, 1.50, 2.20,        # Al-Al, Al-O, Al-Na
    2.00, 1.90, 2.30,        # O-O, O-Na, Na-Na
])
rmc_dat.set_maximum_moves([0.01, 0.01, 0.01, 0.01])
```

**Li–S–P–C (Li, S, P, C)**

```python
rmc_dat.set_density(0.0453277972)
rmc_dat.set_cutoffs([
    1.80, 1.80, 1.80, 1.70,  # Li-Li, Li-S, Li-P, Li-C
    1.80, 1.75, 1.60,        # S-S, S-P, S-C
    1.80, 1.60, 1.30,        # P-P, P-C, C-C
])
rmc_dat.set_maximum_moves([0.01, 0.01, 0.01, 0.01])
```

## Settings specific to free format

Unlike the shared setters, operations on `[ COS ]`, `[ COORD ]`, `[ SNC ]`, and AENET-potential sections are free-format features. Check `is_free_format` before configuring them. Species indices follow the `.cfg` species order.

```python
if rmc_dat.is_free_format:
    rmc_dat.set_element_info(["Si", "O"])
    rmc_dat.set_history_buffer_size(200)
```

### Bond angles: SiO₂ and zeolite

The following examples use different species indices and distance ranges.

```python
# SiO2: 1=Si, 2=O; O-Si-O
rmc_dat.set_angle_constraint(
    central_type=1,
    neighbor1=(2, 1.40, 1.90),
    neighbor2=(2, 1.40, 1.90),
    distribution_type="GAUSSIAN",
    angle_degrees=109.47,
    distribution_width=0.12,  # width in cos(theta) space
    dcosth=0.05,
    sigma=0.01,
    index=0,
)
```

```python
# Zeolite: 1=Si, 2=Al, 3=O, 4=Na
rmc_dat.set_angle_constraint(
    central_type=1,
    neighbor1=(3, 1.40, 1.90),
    neighbor2=(3, 1.40, 1.90),
    distribution_type="GAUSSIAN",
    angle_degrees=109.47,
    distribution_width=0.12,
    dcosth=0.05,
    sigma=0.03,
    index=0,
)
rmc_dat.set_angle_constraint(
    central_type=2,
    neighbor1=(3, 1.55, 2.10),
    neighbor2=(3, 1.55, 2.10),
    distribution_type="GAUSSIAN",
    angle_degrees=109.47,
    distribution_width=0.15,
    dcosth=0.05,
    sigma=0.03,
    index=1,
)
```

### Coordination: one or multiple neighbor species

`neighbors` is a list of `(species_index, rmin, rmax)` tuples; `subconstraints` is a list of `(coordination_number, target_fraction, sigma)` tuples. Multiple target coordination numbers can be specified **within one `subconstraints` list**.

```python
# SiO2: Si-O coordination distribution
rmc_dat.set_coord_constraint(
    central_type=1,
    neighbors=[(2, 1.40, 1.90)],
    subconstraints=[
        (4, 0.998, 0.003),
        (5, 0.002, 0.012),
    ],
    index=0,
)
```

```python
# Zeolite: total O coordination by Si + Al = 2
rmc_dat.set_coord_constraint(
    central_type=3,
    neighbors=[
        (1, 1.40, 1.90),  # Si
        (2, 1.55, 2.10),  # Al
    ],
    subconstraints=[(2, 1.0, 0.01)],
    index=2,
)
```

## FNC and molecular topology

FNC uses **fixed neighbor relations identified by atom indices** in an existing `.fnc` file. `set_fnc_switch(3)` selects the FNC `MOVE-IN` mode; `set_fnc_switch(4)` selects topology mode. **These modes are alternatives, not simultaneous settings.** In free-format topology mode, `[ BPOT ]` is used while `FNC-TYPE` itself becomes `NONE`.

```python
# Molecular FNC: with an existing aaa.fnc
rmc_dat.set_fnc_switch(3)
rmc_dat.set_fnc_distance_ranges({
    1: (1.20, 1.80),  # existing FNC constraint type 1
})
```

```python
# Separate calculation: topology mode using aaa.top
rmc_dat.set_fnc_switch(4)
```

`set_fnc_distance_ranges()` does not rebuild atom pairs or constraint types in `.fnc`; it only updates distance bounds for existing types. See the RMC_POT manual sections I.N, I.Q, and II for FNC, topology, and potential syntax, and the [FNC API](../api/rmc_pot_dat_fnc.md) and [TOP API](../api/rmc_pot_dat_top.md).

## Integration with the run scripts

`rmc.py` creates `Config("config.yml")`, `RmcPotLog`, and `RmcPotDat`, calls `run_rmc_init(config=config, rmc_dat=rmc_dat, logger=logger)` to edit calculation parameters, and then calls `run_rmc()`. The settings on this page can be placed in `run_rmc_init()` in `rmc_init.py`. Select the relevant blocks for the material and constraint method.

Relevant RMC_POT manual sections are I.C (cutoffs), I.K (angles), I.L (coordination), I.N (FNC), I.O.2 (SNC/Qn), I.Q (potentials), and II.C (`.dat` formats). The shared RMC_UTIL API is described in [RmcPotDat](../api/rmc_pot_dat.md).
