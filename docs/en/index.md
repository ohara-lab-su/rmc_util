# rmc_util

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://ohara-lab-su.github.io/rmc_util/en/index.html)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://ohara-lab-su.github.io/rmc_util/ja/index.html)

[![GitHub](https://img.shields.io/badge/GitHub-ohara--lab--su%2Frmc_util-181717?logo=github)](https://github.com/ohara-lab-su/rmc_util/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Documentation-222222?logo=githubpages&logoColor=white)](https://ohara-lab-su.github.io/rmc_util/en/)
[![Ohara Lab](https://img.shields.io/badge/Ohara%20Lab-Home-4B5563?logo=homeassistant&logoColor=white)](https://ohara-lab-su.github.io/index.en.html)

`rmc_util` is an **open-source Python library for preparing RMC_POT inputs, automating calculations, and analyzing results**. It works with the existing RMC_POT calculation engine and provides Python interfaces for editing calculation settings and structural constraints, running repeated calculations, and saving and analyzing results.

It covers `.dat`, FNC, and topology handling, as well as analysis of `.log`, `.hst`, `.fit`, and `.ppcf` outputs. It can be used for standalone RMC_POT calculations or integrated into workflows such as RMC-DFT.

**For initial structure generation, see [packmol_util](https://ohara-lab-su.github.io/packmol_util/en/).** This independent library supports amorphous structure generation from composition, density, and atom count, including FNC constraint file generation for RMC_POT.

```{toctree}
:maxdepth: 2
:caption: User guide

guide/overview
guide/input
guide/constraints
guide/output
```

```{toctree}
:maxdepth: 2
:caption: Reference

reference/index
api/index
```
