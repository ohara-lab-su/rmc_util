# Structural Constraints

RMC searches for configurations consistent with experimental data, but scattering data alone may not uniquely determine local structure. RMC_POT supports distance, coordination-number, bond-angle, and fixed-neighbour constraints. Constraints are **not substitutes for experimental data**; they incorporate independent structural information into the objective function or move acceptance.

## Hard-sphere cutoffs

Minimum allowed distances are specified for each pair of atom types to suppress unphysical overlaps. For $n$ atom types, the number of unique partials is $n(n+1)/2$. Cutoffs follow this partial ordering. Select values consistent with the sample chemistry and starting configuration.

## Coordination-number and average-coordination constraints

A coordination-number constraint evaluates how many neighbours of specified types lie within a distance interval around a central atom. It can constrain the fraction of central atoms with a target coordination and can include multiple neighbour types. Section I.L explains how subconstraints can represent different coordination targets and fractions for the same central and neighbour types.

An average-coordination constraint instead restricts the **mean coordination number** across central atoms, not the fraction of individual atoms satisfying a specific count. These represent different structural information and should be selected accordingly (section I.M).

## Bond-angle distributions

The bond-angle constraints in section I.K operate on the **$\cos\theta$ distribution** for a central atom and two neighbours. The order in which central and neighbour types are specified matters. Target distributions can be uniform over an interval, Gaussian, exclude an angular region, or be read from an experimental distribution file.

Some parameters specify angles in degrees, while others specify widths in $\cos\theta$ space; identical numerical values do not have identical meanings. When combining positive and exclusion constraints, avoid unintended overlap of their target regions.

## Fixed Neighbour Constraint (FNC)

FNC preserves molecular connectivity by restricting distances between pairs identified by atom indices. The `*.fnc` file records neighbour indices, constraint types, and permitted distance intervals. Section I.N describes modes that require the initial structure to satisfy the limits, adjust the limits to initial distances, or allow moves that improve initially out-of-range distances.

In free-format `*.dat`, `FNC-TYPE` supports values including `NONE`, `NORMAL`, `ADJUST`, and `MOVE-IN`. See the [FNC API](../api/rmc_pot_dat_fnc.md) for the RMC_UTIL-side file operations.

## Advanced geometric constraints and potentials

RMC_POT also supports advanced geometric constraints such as common-neighbour constraints. Section I.O explicitly identifies a dependency on the `_ADVANCED_GEOM_CONST` compile option. The presence of an input keyword alone does not establish that the executable was built with the required feature.

Section I.Q also describes GROMACS-like interactions and tabulated nonbonding potentials. These are not equivalent to geometric constraints. In particular, check exclusions and possible double counting of intramolecular interactions.

## Configuration and evaluation

Stronger constraints do not necessarily improve agreement with experiment. Evaluate constraint weights, distance intervals, and target fractions separately from the fit to experimental data. See [input-file details](../reference/rmcpot_input_explained.md), [RMC theory](../reference/rmc_theory_explained.md), and [output files](output.md).

**References**: RMC_POT user guide 2023.1, I.K–I.Q, II.C, II.G.
