# Checking structural constraints

Prepare any FNC/topology files required by the structural model. The `RmcPot.check_fnc_cutoff_consistency()` method checks FNC minimum distances against DAT hard-sphere cutoffs using the actual atom-index pairs in the FNC file and atom-type blocks in the CFG file. It does not assume a fixed mapping from constraint-type numbers to element pairs.

See the [RmcPot API](../api/rmc_pot.md) and the [input format reference](../reference/rmcpot_input_explained.md).
