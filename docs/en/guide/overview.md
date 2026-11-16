# RMC Method and RMC_POT

Reverse Monte Carlo (RMC) constructs three-dimensional atomic configurations consistent with scattering experiments and other measured data. It repeatedly proposes changes to atomic positions and evaluates differences between measured quantities and those calculated from the configuration. Unlike conventional molecular dynamics, which predicts structures from interatomic interactions, RMC uses agreement with experimental data as its principal evaluation criterion.

## Calculating Scattering Quantities from Atomic Configurations

An initial RMC_POT configuration specifies the atom count, atom types, simulation-cell dimensions, and atomic coordinates. The order of RMC atom types is determined by their order in the `.cfg` file and also determines the order of partial correlations. For $n$ atom types, there are $n(n+1)/2$ independent partial correlations. For three types, the order is 1–1, 1–2, 1–3, 2–2, 2–3, and 3–3.

Interatomic distances are accumulated into histograms with bin width $\Delta r$ and normalized to obtain partial pair correlation functions $g_{ij}(r)$. Fourier transformation then gives partial structure factors, which are combined with measurement-specific weights to obtain total scattering quantities. For neutrons, the weights depend on composition and scattering lengths. For X-rays and electrons, atomic scattering factors depend on the scattering vector, so the partial-correlation weights generally depend on $Q$ or $g$ as well.

RMC_POT handles neutron diffraction $S(Q)$, X-ray diffraction $F(Q)$ and $I(Q)$, electron diffraction $F(g)$, and EXAFS $E(k)$. It can also fit partial pair correlation functions $g_{ij}(r)$ directly. However, the official manual discourages transforming experimental diffraction data into $g(r)$ for fitting; this feature is primarily intended for testing potentials against $g(r)$ obtained from molecular dynamics simulations.

## Acceptance of Trial Atomic Moves

For each experimental dataset, a weighted $\chi^2$ evaluates the difference between calculated and observed values. Trial atomic moves that decrease the objective are generally accepted. Moves that increase it may also be accepted with probability corresponding to $\exp[-(\chi^2_{\mathrm{new}}-\chi^2_{\mathrm{old}})]$. This probabilistic acceptance explores configurations differently from a simple least-squares minimization.

Trial moves must also satisfy constraints such as minimum interatomic distances (hard-sphere cutoffs). Special handling applies when the initial configuration already contains distance violations: moves that eliminate or alleviate those violations are not judged solely by the change in $\chi^2$. The number of atoms moved and the maximum displacement affect exploration efficiency and acceptance rates; settings should therefore be evaluated alongside the run logs.

## Roles of Experimental Data and Structural Constraints

Scattering data alone may not uniquely determine local structure. Interatomic-distance, coordination-number, bond-angle, FNC, and other constraints may therefore be combined as necessary. Coordination constraints evaluate the number of neighbors in a specified distance range, while bond-angle constraints evaluate distributions of three-atom angles. Fixed Neighbour Constraints (FNC) keep specified atomic pairs within permitted distance ranges and can preserve molecular connectivity.

Constraints reduce structural ambiguity, but the imposed conditions are not necessarily determined directly by experiment. Agreement with imposed constraints must therefore be assessed separately from agreement with measured data. See [Structural Constraints](constraints.md) for configuration methods and input formats.

## Responsibilities of RMC_POT and RMC_UTIL

RMC_POT is a C++ calculation engine for generating and fitting structural models. RMC_UTIL does not replace that engine; it is a Python helper library for editing inputs, managing execution, and analyzing output files.

In the source code, `RmcPot` manages execution and associated objects, `RmcPotDat` handles `.dat` files, and `RmcPotLog` processes logs. These components have distinct functions but share a `Config` object for settings such as the calculation basename. See the [API Reference](../api/index.md) and [README-Based User Manual](readme_manual.md) for the interfaces.

Starting an RMC_POT calculation requires an initial atomic configuration, calculation settings, and the experimental datasets to be used. See [Input Files](input.md) for their roles and [Output Files](output.md) for post-run checks.

For more detailed theory, see [Explanation of the RMC Method](../reference/rmc_theory_explained.md).

*References: RMC_POT user guide 2023.1, I.A–I.C, I.K–I.Q. RMC_UTIL responsibilities were checked against `rmc_pot.py`, `rmc_pot_dat.py`, and `rmc_pot_log.py`.*
