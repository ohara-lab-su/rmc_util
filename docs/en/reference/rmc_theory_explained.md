# What is the RMC method?

Reverse Monte Carlo (RMC) is a method for exploring atomic configurations consistent with experimental data, such as scattering measurements, through repeated trial displacements and acceptance or rejection of atomic moves.

## Agreement with experimental data

RMC evaluates the difference between scattering functions calculated from an atomic configuration and experimental data. For example, if the standard deviation at measurement point $i$ is $\sigma_i$, a measure of agreement can be written as follows.

```{math}
\chi^2 = \sum_i \frac{\left[S_{\mathrm{calc}}(Q_i)-S_{\mathrm{exp}}(Q_i)\right]^2}{\sigma_i^2}
```

Here $S_{\mathrm{calc}}$ is the structure factor calculated from the atomic configuration, and $S_{\mathrm{exp}}$ is the experimental value. When multiple datasets or structural constraints are used, their contributions also enter the evaluation. The actual objective function and coefficient definitions depend on the RMC_POT configuration and version.

## Acceptance and rejection of atomic moves

The atomic configuration is modified provisionally, and the change in agreement before and after the move,

```{math}
\Delta\chi^2 = \chi^2_{\mathrm{new}}-\chi^2_{\mathrm{old}}
```

is calculated. The acceptance rule given in the RMC_POT user guide is

```{math}
P_{\mathrm{accept}} = \min\left[1,\exp(-\Delta\chi^2)\right]
```

Under this rule, moves that improve agreement ($\Delta\chi^2\leq0$) are accepted, while moves that worsen it may still be accepted with a finite probability.


## Role of standard deviations

The standard deviation $\sigma_i$ at each measurement point determines the weight of the residual between experimental and calculated data. For the same residual, a smaller $\sigma_i$ contributes more strongly to $\chi^2$.

## References

- Orsolya Gereben, *RMC_POT user guide*: see the official manual for the acceptance probability, definition of $\chi^2$, and dataset-specific standard deviations.
- https://www.szfki.hu/~nphys/rmc++/RMC_POT_user_guide.pdf
