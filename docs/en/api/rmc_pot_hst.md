# `rmc_util.rmc_pot_hst`

Histogram output analysis. Source: `src/rmc_util/rmc_pot_hst.py`.

## Class `RmcPotHst`

### `__init__(self, hst_name: Optional[str]=None, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Initializes `RmcPotHst`, reads the selected `.hst` file, and parses its contents. The target is determined from `hst_name`, `cfg_name`, or `config`; an explicitly supplied `hst_name` takes precedence. `cfg_name` identifies `{cfg_name}.hst`, and `config` supplies the configuration's CFG name.

Parameters:

- `hst_name`: Name of the `.hst` file to read.
- `cfg_name`: CFG name used to determine the `.hst` filename.
- `config`: Configuration object supplying the CFG name.
- `logger`: Logger instance.

### `read_chi2(self)`

Compatibility method returning the `chi2_tot` history. The `.hst` file has no explicit `step` field, so the method uses zero-based row indices as step numbers, reproducing the behavior of the earlier `RmcPotHst` interface.

Returns `Tuple[List[int], List[float]]`: the step indices and corresponding `chi2_tot` values.

### `detect_convergence(self, rel_tol: float=0.01, acc_tol: float=0.001, min_consecutive: int=3)`

Estimates the onset of practical convergence from the RMC history. Rather than relying on the absolute value of `chi2_tot`, it combines the relative improvement between successive loops with the acceptance fraction (`accepted/tried`).

For loop `i`, the relative improvement is

```text
delta = (chi2[i-1] - chi2[i]) / chi2[i-1]
```

A loop is considered stagnant when both `delta < rel_tol` and `accepted/tried < acc_tol`. Convergence is reported only after this condition holds for `min_consecutive` successive loops. The returned loop index identifies the **first loop in the stagnant sequence**, not the last loop.

Parameters:

- `rel_tol`: Threshold for the relative improvement in `chi2_tot`.
- `acc_tol`: Threshold for the acceptance fraction.
- `min_consecutive`: Minimum number of consecutive stagnant loops.

Returns `Optional[int]`: the first loop index of the converged sequence, or `None` if the criteria are not met.
