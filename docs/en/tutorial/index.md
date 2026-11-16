# Tutorial

This tutorial collects Python examples for configuring RMC calculations, specifying structural constraints, and analyzing results with RMC_UTIL. An RMC_POT calculation requires an atomic configuration, experimental data, a calculation-parameter file, and the RMC_POT executable.

```{toctree}
:maxdepth: 2

readme_examples
```

## Prepare the input files

RMC_POT uses an atomic configuration such as `sample.cfg` and calculation parameters such as `sample.dat`, sharing the same basename. `sample` is a filename basename; choose a name appropriate to the actual calculation. Ensure consistency among the number of atoms, atom-type order, number density, interatomic-distance cutoffs, and experimental-data settings.

See [Input files](../guide/input.md) for the `.cfg` coordinate format and the distinction between fixed-format and free-format `.dat` files. The [File-format reference](../reference/index.md) describes the RMC_POT input specifications.

## Configure calculation parameters from Python

The [RMC_UTIL code examples](readme_examples.md) demonstrate how to initialize a `.dat` file with `RmcPotDat` and configure number density, cutoffs, maximum displacement, and histogram bin spacing. The example that saves the settings with `write()` suppresses automatic writing during the individual configuration steps.

The number density must be consistent with the atom count and cell volume, and the cutoffs must follow the order of atom-type pairs. These values depend on the structural model and experimental conditions; use values appropriate to the system rather than copying the numerical examples unchanged.

## Specify structural constraints

The code examples include coordination-number and Qn constraints. A coordination constraint specifies the central atom type, neighboring atom types, distance intervals, target coordination number, fraction, and weighting parameter. See [Structural constraints](../guide/constraints.md) for their physical meaning and the corresponding RMC_POT input format.

## Inspect calculation results

After the calculation, inspect the generated, attempted, and accepted move counts in the log, changes in the objective function, fit results, and partial pair-correlation functions. A normal-termination check is distinct from assessing agreement with scattering data and satisfaction of structural constraints. See [Output files](../guide/output.md) for the roles of output files and the [API reference](../api/index.md) for class interfaces.
