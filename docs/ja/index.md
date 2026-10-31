# rmc_util

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://ohara-lab-su.github.io/rmc_util/en/index.html)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://ohara-lab-su.github.io/rmc_util/ja/index.html)

[![GitHub](https://img.shields.io/badge/GitHub-ohara--lab--su%2Frmc_util-181717?logo=github)](https://github.com/ohara-lab-su/rmc_util/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Documentation-222222?logo=githubpages&logoColor=white)](https://ohara-lab-su.github.io/rmc_util/ja/)
[![Ohara Lab](https://img.shields.io/badge/Ohara%20Lab-Home-4B5563?logo=homeassistant&logoColor=white)](https://ohara-lab-su.github.io/index.html)

`rmc_util` は、**RMC_POT の入力作成・計算実行・結果解析を Python から扱うためのオープンソースライブラリ**です。RMC_POT の計算エンジンをそのまま利用しながら、計算条件や構造拘束の編集、反復実行、結果の保存・解析を自動化できます。

`.dat`、FNC、topology の操作から、`.log`・`.hst`・`.fit`・`.ppcf` の解析まで対応します。RMC_POT 単独の計算にも、RMC-DFT などのワークフローにも利用できます。

**初期構造の生成には [packmol_util](https://ohara-lab-su.github.io/packmol_util/ja/) も利用できます。** 組成・密度・原子数を指定した非晶質構造の作成や、RMC_POT 用 FNC 拘束ファイルの生成に対応する、独立したライブラリです。

```{toctree}
:maxdepth: 2
:caption: 利用ガイド

guide/overview
guide/input
guide/constraints
guide/output
```

```{toctree}
:maxdepth: 2
:caption: 詳細資料

reference/index
api/index
```
