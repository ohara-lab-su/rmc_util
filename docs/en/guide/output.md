# Output Files and Analysis

RMC_POT outputs fitting status, calculation history, atomic configurations, partial pair distribution functions, and other data. The types of output files depend on the settings.

| File | Main contents | Corresponding module |
| --- | --- | --- |
| `.fit` | Comparison between experimental and calculated values | `rmc_pot_fit` |
| `.hst` | History of attempted and accepted moves, changes in goodness of fit, etc. | `rmc_pot_hst` |
| `.ppcf` | Partial Pair Correlation Function | `rmc_pot_ppcf` |
| `.cfg` | Atomic configuration | `rmc_pot` / related `util` modules |
| Logs | Records of the calculation process | `rmc_pot_log` |

When interpreting `.fit`, check whether the target data are $S(Q)$, $F(Q)$, $I(Q)$, or another quantity. When comparing values in `.hst`, also pay attention to the combination of fitting targets and constraints.

For the columns, headers, and interpretation of each file, see [Detailed Explanation of Output Files](../reference/rmcpot_output_explained.md).

*Reference: RMC_POT user guide 2023.1, II.B.*
