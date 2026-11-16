# RMC Method and RMC_POT

The Reverse Monte Carlo (RMC) method constructs three-dimensional atomic configurations consistent with data obtained from scattering experiments and other measurements. It evaluates the difference between scattering quantities calculated from atomic configurations and measured values, and iteratively attempts changes to atomic positions.

RMC_POT handles neutron diffraction $S(Q)$, X-ray diffraction $F(Q)$ and $I(Q)$, electron diffraction $F(g)$, EXAFS $E(k)$, and other data. Partial pair distribution functions $g_{ij}(r)$ are important structural quantities obtained from atomic configurations.

Scattering data alone may not uniquely determine local structures. Therefore, interatomic distances, coordination numbers, bond angles, FNC, and other structural constraints are combined as needed.

To start an RMC_POT calculation, prepare an initial atomic configuration, calculation conditions, and the experimental data to be used. The roles of the individual files are summarized in [Input Files](input.md).

For more detailed theory, see [Explanation of the RMC Method](../reference/rmc_theory_explained.md).

*Reference: RMC_POT user guide 2023.1, I.A–I.C, I.K–I.Q.*
