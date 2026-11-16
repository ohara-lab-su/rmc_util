# Checking structural constraints

Prepare any FNC/topology files required by the structural model. The `RmcPot.check_fnc_cutoff_consistency()` method checks FNC minimum distances against DAT hard-sphere cutoffs using the actual atom-index pairs in the FNC file and atom-type blocks in the CFG file. It does not assume a fixed mapping from constraint-type numbers to element pairs.

See the [RmcPot API](../api/rmc_pot.md) and the [input format reference](../reference/rmcpot_input_explained.md).

## SNC / Qn: network connectivity

Unlike a first-shell coordination constraint, SNC evaluates central–first-neighbor–second-neighbor connectivity. `coordination_number` is the number of first neighbors satisfying the connectivity condition; `fraction` is the target fraction (0–1) of central atoms. Each `index` identifies a separate `[ SNC ]` section.

```python
# SiO2: 1=Si, 2=O. Separate SNC sections for Q5 / Q4 / Q3
for index, coordination_number, fraction in [
    (0, 5, 0.002),
    (1, 4, 0.994),
    (2, 3, 0.004),
]:
    rmc_dat.set_qn_constraint(
        central_type=1,
        first_neighbor_type=2,
        first_neighbor_minimum=1.45,
        first_neighbor_maximum=1.80,
        second_neighbors=[(1, 1.45, 1.80)],
        coordination_number=coordination_number,
        fraction=fraction,
        sigma=0.04,
        index=index,
    )
```

```python
# Zeolite: Si-O-(Si/Al) and Al-O-(Si/Al)
rmc_dat.set_qn_constraint(
    central_type=1,
    first_neighbor_type=3,
    first_neighbor_minimum=1.40,
    first_neighbor_maximum=1.90,
    second_neighbors=[(1, 1.40, 1.90), (2, 1.55, 2.10)],
    coordination_number=4,
    fraction=1.0,
    sigma=0.03,
    index=0,
)
rmc_dat.set_qn_constraint(
    central_type=2,
    first_neighbor_type=3,
    first_neighbor_minimum=1.55,
    first_neighbor_maximum=2.10,
    second_neighbors=[(1, 1.40, 1.90), (2, 1.55, 2.10)],
    coordination_number=4,
    fraction=1.0,
    sigma=0.03,
    index=1,
)
```

To exclude Al–O–Al connectivity from the second-neighbor candidates, use `second_neighbors=[(1, 1.40, 1.90)]` for the Al-centered SNC. This selects allowed second-neighbor species; it does not fix individual atom indices as FNC does. See RMC_POT manual I.O.2 and free-format `[ SNC ]`.

## ANN potential (free format)

```python
rmc_dat.set_aenet_potential(
    potentials=[
        (1, "Si.nn", "Si"),
        (2, "O.nn", "O"),
    ],
    sigma=1.0,
    aenet_step=1,
    write_atomic_energy=True,
)
```

Place `Si.nn` and `O.nn` in the run directory. RMC_POT must be built with AENET support. `sigma` weights the ANN energy contribution; it is not directly the experimental measurement uncertainty. See the ANN-potential section I.Q.2 of the manual.
