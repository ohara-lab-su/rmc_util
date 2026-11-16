# Explanation of RMC_POT input files

# cfg file
The cfg file used to specify atomic configurations is explained in detail in the following document.
(rmcpot_cfg_explained.md)

# sq file
```{code}
2832
Dataset measured at BL04B2
0.263585 2.81259 0.308196 0.164155 0.329761 0.0218585 0.0878205 0.0882089 
0.281276 2.3427 0.308147 0.16408 0.329845 0.0218421 0.087817 0.0882679 
0.298966 1.91993 0.308095 0.164001 0.329935 0.0218247 0.0878133 0.0883307 
0.316656 1.57281 0.30804 0.163917 0.33003 0.0218063 0.0878092 0.0883972 
0.334346 1.29722 0.307982 0.163829 0.33013 0.0217868 0.0878049 0.0884676 
0.352037 1.06632 0.307921 0.163735 0.330235 0.0217663 0.0878003 0.0885417 
0.369727 0.88715 0.307857 0.163637 0.330346 0.0217447 0.0877954 0.0886195
   :        : 
```
Column 1 contains q [Å⁻¹],
column 2 contains the experimentally measured S(q),
and columns 3 onward contain weighting factors.

```math
coeff_{ii} = \frac{c_i^2 \overline{b_i}^2}{\sum_{i} \sum_{j} c_i c_j \overline{b_i b_j}} \qquad , \qquad 
coeff_{ij} = \frac{c_i c_j \overline{b_i b_j}}{\sum_{i} \sum_{j} c_i c_j \overline{b_i b_j}}
```
Official manual: https://www.szfki.hu/~nphys/rmc++/RMC_POT_user_guide.pdf
See Section E3.
This format is used to construct the total S(q) from the Faber–Ziman partial structure factors S_ij(q).
T. E. Faber　& J. M. Ziman, 1964, DOI: https://doi.org/10.1080/14786436508211931

When total-scattering measurements are analyzed using the BL04B2 analysis software (IGOR macro) at SPring-8, the output also includes weighting factors.
If these data are available, the factors need not be calculated separately.
http://rud.spring8.or.jp/member/0020758/distrbution.html

# dat file

```{code}
comment
0.0842566414       ! number density
1 1 1 1 1 1 ! cut offs
0.01 0.01 0.01   ! maximum moves
0.025        ! r spacing
.false.      ! whether to use moveout option
0            ! number of configurration to collect
5000         ! step for printing
0 0          ! time limit, step for saving
0 0 1 0      ! g(r), neutron, x-ray, EXAFS
S_q_fqd_0.3_0.03_40.sq
1 991
1.0
5E-3
.false.
.true.
.false.
.false.
0         ! number of cos. distr of bond angles constraint, dcos_theta (spacing in cos(theta) space
0  ! no of coord. constr.
0         ! no of av. coord. contsr.
0         ! potential
0         ! FNC switch
0         ! initial bin shift;
1         ! xmax used in the run.
1         ! number of atoms moved in a single move
200       ! size of the history buffer
10        ! number of display update beteen each history buffering
0         ! indicator of custom move
0         ! whether to load the histgram form file, if posible [0:no 1:yes]
5        ! maximum number of atoms in a gridcell
0 0       ! frction of swaps, ntypes*(ntypes-1)/2 0 not allowded or 1 allowed for the possible mixed part
4         ! total number of threads to use
```

The following explains each line from top to bottom (line numbers are assigned to the example for convenience).

1) comment
- Description: an optional comment describing the file or sample.

2) 0.0842566414       ! number density
- Description: number density of the system, in atoms/Å³.
- Note: it must agree with the atom count and simulation-box volume in the cfg file (the value is specified twice).

3) 1 1 1 1 1 1 ! cut offs
- Description: field specifying pair cutoff distances (or cutoff-enable flags) for the atomic species. The six entries in this example depend on the number of types and the program’s internal format.
- In practice: many implementations specify minimum allowed separations or pair-specific distance cutoffs. Supply the required number of entries for ntypes.
- For a three-component system, the order is expected to be 11, 12, 13, 22, 23, 33.
- For n components, the expected order is 11, 12, 13, 14, …, 1n, 22, 23, …, 2n, 33, 34, …, 3n, …, nn.

4) 0.01 0.01 0.01   ! maximum moves
- Description: maximum atomic displacement per move. Multiple entries may correspond to atomic species or move types. Units: Å.
- Note: move amplitude affects acceptance rate and structural exploration. Since acceptance also depends on constraints and the current configuration, no universal target acceptance rate is specified here.

5) 0.025        ! r spacing
- Description: bin width for the pair distribution function g(r), in Å.
- Note: a smaller value improves resolution but increases computational cost.

6) .false.      ! whether to use moveout option
- Description: Boolean flag (.true./.false.) enabling moveout, which resolves atom pairs violating minimum-separation constraints.
- Note: behavior depends on the implementation; consult the corresponding manual section.

7) 0            ! number of configuration to collect
- Description: number of configurations to collect; zero in this example.
- Note: distinguish this from intermediate configuration-saving behavior.

8) 5000         ! step for printing
- Description: interval, in steps, between progress/log outputs.

9) 0 0          ! time limit, step for saving
- Description: the first value is a time limit (elapsed-time stopping condition, in minutes); the second is the step interval for saving files.
- Note: two zeros often mean disabled/default behavior.

10) 0 0 1 0      ! g(r), neutron, x-ray, EXAFS
- Description: flags for calculated/output quantities, in the order g(r), neutron scattering, X-ray scattering, and EXAFS.
- Example: these values request X-ray output but not g(r), neutron, or EXAFS output (verify the ordering and interpretation against the implementation manual).

11) S_q_fqd_0.3_0.03_40.sq
- Description: path or filename of the sq dataset containing S(q); relative or absolute paths may be used.

12) 1 991
- Description: range selection for reading the sq file (possibly first/last line indices or minimum/maximum q indices).
- Note: the exact meaning depends on the RMC_POT version and input format; consult its manual.

13) 1.0
- Description: the exact definition of this value cannot be established from this example alone. Do not assign a parameter name by conjecture; verify the input specification.

14) 5E-3
- Description: standard deviation for this dataset. It determines the weight of experimental–calculated residuals in the objective function; it is neither a convergence tolerance nor a temperature.
- Note: check the applicable RMC_POT input specification for additional settings following the standard deviation and for the objective-function selection.

15) .false.
16) .true.
17) .false.
18) .false.
- Description: Boolean settings associated with the dataset. Their individual names and meanings cannot be established uniquely from this example. They are not arbitrarily labeled as background correction, smoothing, etc.; verify the specification for the version in use.

19) 0         ! number of cos. distr of bond angles constraint, dcos_theta (spacing in cos(theta) space
- Description: number of bond-angle-distribution constraints. Zero disables these constraints. The trailing comment refers to dcos_theta, the spacing in cos(theta) space.

20) 0  ! no of coord. constr.
- Description: number of coordination-number constraints. Zero means none are applied.

21) 0         ! no of av. coord. contsr.
- Description: number of average-coordination constraints. Zero disables them.

22) 0         ! potential
- Description: potential-related flag or selection index. Zero often means no potential is used.

23) 0         ! FNC switch
- Description: FNC (for example, Fixed Neighbour Constraints) switch. Zero means off; consult the implementation manual.

24) 0         ! initial bin shift;
- Description: initial bin offset for g(r) or similar histograms. Zero means no shift.

25) 1         ! xmax used in the run.
- Description: scaling value or flag for the maximum r (xmax) used to calculate g(r) and related quantities; the meaning of 1 depends on the implementation.

26) 1         ! number of atoms moved in a single move
- Description: number of atoms moved simultaneously per move (one in this example). Standard atomic RMC with the RMC_POT 2023.1 free format assumes one-atom moves; multiple-atom moves are not asserted to be supported.

27) 200       ! size of the history buffer
- Description: history-buffer size for past move information, acceptance rates, and related statistics.

28) 10        ! number of display update beteen each history buffering
- Description: number of display updates between history-buffer updates.

29) 0         ! indicator of custom move
- Description: flag for user-defined/custom move algorithms. Zero disables them.

30) 0         ! whether to load the histgram form file, if posible [0:no 1:yes]
- Description: whether to load an existing histogram from a file (0: no; 1: yes).

31) 5        ! maximum number of atoms in a gridcell
- Description: maximum number of atoms allowed per spatial grid cell; a parameter for neighbor searching or neighbor-list construction.

32) 0 0       ! frction of swaps, ntypes*(ntypes-1)/2 0 not allowded or 1 allowed for the possible mixed part
- Description: swap settings. The first value is a swap fraction/control value; the second enables or disables swaps (0: disallowed, 1: allowed). The comment associates ntypes*(ntypes-1)/2 with the number of possible mixed-type pairs.

33) 4         ! total number of threads to use
- Description: number of threads to use. Set according to the machine; verify actual parallel behavior against the build and runtime environment.

---

Additional notes and cautions
- The exact order and meaning of these lines may vary slightly with RMC_POT (or RMC++) version and implementation. The descriptions here indicate general roles and units; consult the official manual (https://www.szfki.hu/~nphys/rmc++/RMC_POT_user_guide.pdf) for the complete specification.
- The number of species (ntypes) in cfg must match the number expected in dat, including the number of cutoff and per-species parameter entries.
- After changing values, inspect logs, acceptance rates, bin widths, and related quantities and adjust as appropriate. Maximum displacement strongly affects acceptance.
- Incorrect weighting-factor values or ordering in sq will compromise S(q) reproduction. Handle atomic fractions c_i and scattering lengths (including average scattering lengths) correctly.
