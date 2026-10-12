# rmc_util

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/README.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/README.ja.md)

`rmc_util` は、RMC_POT の計算を Python から扱うためのライブラリです。

RMC_POT の入力条件の作成・編集、各種構造制約、FNC・topology の操作、RMC_POT の実行・入力検証、計算結果の退避、および `.log`・
`.hst`・`.fit`・`.ppcf` などの出力解析を Python から行うための機能を提供します。

単独でも RMC_POT の計算準備・実行・解析に利用できますが、特に RMC-DFT のような上位ワークフローの構成要素として利用すると、RMC
条件の変更、RMC_POT の反復実行、収束判定、結果の保存、その後の計算への構造受け渡しなどを一貫して制御できます。

## インストール

PyPI で公開されているパッケージは次のコマンドでインストールできます。

```bash
pip install rmc-util
```

PyPI 上のプロジェクト名は `rmc-util`、Python から利用するときのパッケージ名は `rmc_util` です。

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst
```

開発版をローカルに clone して利用する場合は、リポジトリのルートで次を実行します。

```bash
pip install .
```

## rmc_util が扱う範囲

### RMC_POT の入力条件と実行

`RmcPotDat` は RMC_POT の `.dat` を扱う中心的なインターフェースです。number density、cutoff、最大原子移動量、r spacing、実験データ範囲、計算時間・保存間隔などの計算条件を Python から設定できます。

fixed format と free format に共通する計算条件は同じ API で扱えます。既存 `.dat` を `prefer_existing=True` で使用する場合は形式を判定して読み込み、新規作成時には形式を指定できます。free format 固有の構造制約なども `RmcPotDat` から設定できます。

`RmcPot` は RMC_POT の実行を扱います。現在の実装では、preprocess、入力検証、RMC_POT の実行、計算後の結果回収・退避に加え、FNC の距離制約と原子種間 cutoff の整合性確認などを行えます。

### 自由形式の構造制約

自由形式 `.dat` では、Python から次のような制約・potential 関連設定を作成・編集できます。

- angle constraint
- coordination constraint
- SNC / Qn constraint
- BVS constraint
- pair potential
- AENET potential

そのため、RMC の実行ごとに `.dat` を手作業で書き換えるのではなく、上位スクリプトから計算条件を組み立てたり変更したりできます。

### FNC と topology

`RmcPotDatFnc` は、FNC データの作成、読み込み、編集、検証、書き出しを扱います。constraint type ごとの距離範囲、各原子のneighbour、原子ペアなどを
Python から操作できます。

`RmcPotDatTop` は、RMC_POT の topology を Python から構築・編集するための機能を提供します。molecule、atom、bond、angle、dihedral、exclusion、virtual
site などを扱い、topology の検証も行えます。

### 計算結果と解析

RMC_POT の実行部分とは独立して、出力ファイルの読み取りにも利用できます。

- `RmcPotLog`：RMC_POT のログを読み取り、generated / tried / accepted、χ²、Rw、RMC block / loop などを取得します。計算結果の収集・バックアップも扱います。
- `RmcPotHst`：`.hst` の履歴を読み取り、acceptance や χ² の履歴取得、収束判定を行います。
- `RmcPotFit`：`.fit` を読み取り、計算・実験 F (Q)、background、および対応する S (Q) を取得します。
- `RmcPotPpcf`：`.ppcf` を読み取り、部分二体分布関数 `g_ij(r)` を取得します。

## 基本例：RMC_POT `.dat` の設定

`RmcPotDat` は必要になるまで初期化を遅延できますが、明示的に `init()` することもできます。

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(
    cfg_name="sample",
    auto_write=False,
    use_free_format=True,
)

rmc_dat.init(
    use_free_format=True,
    prefer_existing=True,
)

rmc_dat.set_comment("SiO2 sample", auto_write=False)
rmc_dat.set_density(0.0665715652, auto_write=False)
rmc_dat.set_cutoffs([1.9, 1.1, 1.9], auto_write=False)
rmc_dat.set_maximum_moves([0.01, 0.01], auto_write=False)
rmc_dat.set_r_spacing(0.025, auto_write=False)
rmc_dat.write()
```

`sample.dat` がすでに存在し、`prefer_existing=True` の場合は、固定形式・自由形式を自動判定して既存ファイルを使用します。

## 例：自由形式の coordination / Qn constraint

自由形式では、構造制約を Python から直接設定できます。

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(
    cfg_name="sample",
    use_free_format=True,
)

rmc_dat.init(
    use_free_format=True,
    prefer_existing=True,
)

rmc_dat.set_element_info(["Si", "O"])

rmc_dat.set_coord_constraint(
    central_type=1,
    neighbors=[
        (2, 1.40, 1.90),
    ],
    subconstraints=[
        (4, 1.0, 0.01),
    ],
    index=0,
)

rmc_dat.set_qn_constraint(
    central_type=1,
    first_neighbor_type=2,
    first_neighbor_minimum=1.45,
    first_neighbor_maximum=1.80,
    second_neighbors=[
        (1, 1.45, 1.80),
    ],
    coordination_number=4,
    fraction=1.0,
    sigma=0.04,
    index=0,
)
```

複数原子種を含む系について、複数の coordination constraint や Qn constraint を設定することもできます。

## 例：RMC ワークフローから利用する

上位ワークフローでは、RMC の設定・実行オブジェクトを保持し、出力を読み取って次の処理を判断できます。

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst, RmcPotLog

rmc_dat = RmcPotDat(
    cfg_name="sample",
    use_free_format=True,
)
rmc_dat.init(prefer_existing=True)

rmc_log = RmcPotLog(cfg_name="sample")

rmc = RmcPot(
    rmc_dat=rmc_dat,
    rmc_log=rmc_log,
    cfg_name="sample",
)

if not rmc.preprocess():
    raise RuntimeError("RMC_POT input validation failed.")

if not rmc.check_fnc_cutoff_consistency(cfg_name="sample"):
    raise RuntimeError("FNC and cutoff settings are inconsistent.")

try:
    run_ok = rmc.run()
finally:
    rmc.postprocess(
        cfg_name="sample",
    )

if not run_ok:
    raise RuntimeError("RMC_POT execution failed.")

hst = RmcPotHst(cfg_name="sample")
loop = hst.detect_convergence(
    rel_tol=1.0e-2,
    acc_tol=1.0e-3,
    min_consecutive=2,
)
```

このような使い方では、RMC_POT を単独の計算として実行するだけでなく、より大きな計算フローの一工程として扱えます。たとえば
RMC-DFT では、RMC 条件を変更して RMC_POT を実行し、収束状態を確認し、結果を退避した上で、得られた構造を DFT
側へ渡す、といった制御に利用できます。

`rmc_util` 自体は DFT 計算を提供するライブラリではなく、そのようなワークフローで必要となる RMC_POT 側のハンドリングを担当します。

## 主なモジュール

| 分野         | モジュール          | 内容                                                          |
|--------------|---------------------|---------------------------------------------------------------|
| RMC 実行     | `rmc_pot`           | RMC_POT の preprocess・実行・検証・postprocess                |
| DAT 共通     | `rmc_pot_dat`       | fixed / free の違いを隠蔽し、共通の RMC 条件を同一 API で操作 |
| 固定形式 DAT | `rmc_pot_dat_fixed` | 固定形式 RMC_POT パラメータの読み書き                         |
| 自由形式 DAT | `rmc_pot_dat_free`  | 自由形式パラメータ・構造制約・potential 設定の読み書き        |
| FNC          | `rmc_pot_dat_fnc`   | FNC の作成・編集・検証                                        |
| topology     | `rmc_pot_dat_top`   | topology / ITP 形式データの作成・編集・検証                   |
| RMC log      | `rmc_pot_log`       | RMC ログ解析、結果の収集・バックアップ                        |
| history      | `rmc_pot_hst`       | `.hst` の解析と収束判定                                       |
| fit          | `rmc_pot_fit`       | `.fit` の読み取りと F(Q) / S(Q) の取得                        |
| PPCF         | `rmc_pot_ppcf`      | 部分二体分布関数の読み取り                                    |

CFG / POSCAR 変換などの構造変換・補助機能は `rmc_util.util` に含まれます。

## ドキュメント

- [ドキュメントホーム](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/index.md)
- [RMC 法と RMC_POT](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/overview.md)
- [入力ファイル](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/input.md)
- [構造制約](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/constraints.md)
- [出力と解析](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/guide/output.md)
- [ファイル形式の詳説](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/reference/index.md)
- [API リファレンス](https://github.com/ohara-lab-su/rmc_util/blob/main/docs/api/index.md)

ドキュメントをローカルで HTML 化する場合は次を実行します。

```bash
docs/build.sh
```

HTML は `docs/_build/html/` に出力されます。

## ソースコード

ソースコードと開発履歴は [GitHub](https://github.com/ohara-lab-su/rmc_util) で公開しています。

## 参考文献

Orsolya Gereben, *RMC_POT user guide for version 2023.1* (2023).
