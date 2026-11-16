# Output Files and Analysis

RMC_POT outputs not only experimental fit information but also configurations, partial pair correlation functions, move histories, and constraint-related information. **The files produced depend on input options, enabled features, and saving settings.** RMC_UTIL provides modules for reading some of these outputs.

## Main files

| File | Main content | Related RMC_UTIL module |
| --- | --- | --- |
| `.fit` | Comparison of experimental and calculated values | `rmc_pot_fit` |
| `.hst` | Run history and evolution of fit and constraint terms | `rmc_pot_hst` |
| `.ppcf` | Partial pair correlation functions by atom-type pair | `rmc_pot_ppcf` |
| `.cfg` | Atomic configuration | `rmc_pot`, `util.cfg2poscar`, `util.poscar2cfg` |
| `.log` and related logs | Execution records | `rmc_pot_log` |
| `.free`, `.freer`, `.freers` | Free-format settings and non-default values | Related to `rmc_pot_dat_free` |
| `.cnc`, `.cncd` | Coordination-constraint results (feature/settings dependent) | See RMC_POT output specification |

See [detailed output-file descriptions](../reference/rmcpot_output_explained.md) for headers and column definitions. Do not infer every column layout solely from a filename extension.

## Interpreting `.fit`

A `.fit` file is used to compare calculated results against input data. First identify whether the quantity is neutron $S(Q)$, X-ray $F(Q)$ or $I(Q)$, electron $F(g)$, or EXAFS $E(k)$. Scattering coefficients, background corrections, and normalization settings affect the numerical meaning even when curve shapes are similar.

When using the [`.fit` API](../api/rmc_pot_fit.md), distinguish file-format interpretation from the physical interpretation of the measured quantity.

## `.hst` and convergence assessment

Distinguish objective-function contributions from experimental datasets from those of structural constraints and potentials. Section I.A explains the construction of $\chi^2$ from weighted dataset residuals. Values from runs with different `SIGMA`, numbers of data points, or constraint combinations therefore cannot be compared directly without accounting for these differences.

Assess acceptance rates, residuals, constraint satisfaction, and changes in configuration together. See the [`.hst` API](../api/rmc_pot_hst.md) and [log API](../api/rmc_pot_log.md).

## `.ppcf` and structural analysis

The partial pair correlation function $g_{ij}(r)$ describes the distribution of atom type $j$ at distance $r$ from a central atom of type $i$. Partial ordering follows the atom-type order in `*.cfg`. Section I.A also notes that RMC's internal histogram counts unique atom pairs, so its raw counts differ from those of a conventional histogram.

When comparing partial functions, verify atom-type order, radial bin width, and number-density normalization. See the [`.ppcf` API](../api/rmc_pot_ppcf.md) and [RMC theory](../reference/rmc_theory_explained.md).

## Reproducibility and saved settings

According to section II.C, RMC_POT writes free-format run settings to `.free` and non-default settings to `.freer`. When scalable sigma parameters are used, `.freers` also records the scaled values. To preserve reproducibility, retain **both the inputs actually used** and **the settings written after execution**.

**References**: RMC_POT user guide 2023.1, I.A, I.L, II.B–II.C.
