# Input Files

RMC_POT input consists of an atomic configuration, run parameters, experimental datasets, and, when required, structural constraints and potentials. RMC_UTIL is a Python library for reading, writing, and editing some of these files. Distinguish the **input specification of the RMC_POT executable** from the **RMC_UTIL API**.

## File roles

| File | Role | Related RMC_UTIL API |
| --- | --- | --- |
| `*.cfg` | Initial configuration, atom-type counts, simulation cell | `RmcPot`, `util.cfg2poscar`, `util.poscar2cfg` |
| `*.dat` | Run parameters, experimental datasets, constraints, output controls | `RmcPotDat`, `RmcPotDatFixed`, `RmcPotDatFree` |
| Experimental data files | Measured diffraction or EXAFS data and required coefficients | Referenced from `*.dat` |
| `*.fnc` | Fixed-neighbour relationships and allowed distances | `RmcPotDatFnc` |
| `*.top` | Molecular topology and interactions | `RmcPotDatTop` |

For syntax, headers, and column definitions, see [Detailed RMC_POT Input Files](../reference/rmcpot_input_explained.md), corresponding to sections II.C–II.I of the RMC_POT user guide 2023.1.

## Initial configuration `*.cfg`

According to section II.D, a text `*.cfg` file has a header specifying the total atom count, number of atom types, half-box length, and counts for each type. Coordinates then follow **grouped by atom type**. Each coordinate is reduced to the interval −1 to +1; distances and the half-box length are in Å. Do not confuse these coordinates with Cartesian coordinates in POSCAR.

The order of atom types determines the order of partial correlations. For three types, this is `1-1, 1-2, 1-3, 2-2, 2-3, 3-3`. Partial cutoffs and scattering coefficients in `*.dat` must use the corresponding order.

## Two `*.dat` formats

RMC_POT supports the original **fixed format** and a **free format** based on sections and keywords. The fixed format depends on line and field positions. Free-format input is identified by `#002` or `#003` at the beginning of the file and uses sections such as `[ GENERAL ]` and `[ EXP ]` with `KEY = VALUE` entries. The version marker is not merely a comment.

The default handling of X-ray scattering coefficients differs between `#002` and `#003`. According to section II.C, `#002` defaults to reading coefficients from files, whereas `#003` defaults to calculating them when chemical symbols are supplied. Check consistency with experimental data when using `READ-COEFFS`.

The `RmcPotDatFree` implementation supports template keywords such as `NDENS`, `CUT-OFF`, `MAX-MOVES`, `R-SPACING`, `RUN-TIME`, `SAVE-TIME`, `TYPE`, `DATAFILE`, `POINT-RANGE`, and `SIGMA`. **Template values are not universal recommendations**; they must be selected for the sample, atom types, and experimental range.

## Experimental data and units

RMC_POT supports neutron, X-ray, and electron diffraction, EXAFS, and partial or total pair-distribution data. Their data types, abscissae, scattering coefficients, and normalization conventions differ. Check the units in section I.B and the experimental-file specifications in section II.E.

When fitting multiple datasets, each `SIGMA` affects its contribution to the objective function. Distinguish experimental uncertainties from computational weighting; do not copy the same value indiscriminately.

## Consistency checks before loading

1. Verify total atom count, number of types, and counts per type in `*.cfg`.
2. Verify that density or cell dimensions in `*.dat` agree with the geometry in `*.cfg`.
3. Match atom-type order to partial cutoffs, move amplitudes, and scattering coefficients.
4. Match experimental data type, selected range, and coefficient reading/calculation mode.
5. When using `*.fnc` or `*.top`, verify atom indices, molecular mapping, and units. In particular, distinguish nm in GROMACS topologies from Å in RMC.

**References**: RMC_POT user guide 2023.1, I.A–I.B, II.C–II.I. For Python implementation, see the [API reference](../api/index.md).
