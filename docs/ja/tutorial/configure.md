# 計算条件の設定例：固定形式・自由形式

`RmcPotDat` は固定形式と自由形式の `.dat` を同じ Python API で操作します。**同じ setter を使い、ファイル形式の選択は `init()` で行います。** 既存ファイルを優先する `prefer_existing=True` では、指定した `use_free_format` より既存ファイルの形式判定が優先されます。新規作成時に形式を指定する場合は、対象の `.dat` が存在しないことを確認してください。既存ファイルを置き換える `prefer_existing=False` は `.bak_init` を作成します。

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(cfg_name="sample", auto_write=False)
rmc_dat.init(use_free_format=True, prefer_existing=True)  # False なら固定形式
rmc_dat.set_comment("comment SiO2")
rmc_dat.set_density(0.0665715652)
rmc_dat.set_cutoffs([2.40, 1.25, 2.10])
rmc_dat.set_maximum_moves([0.01, 0.01])
rmc_dat.set_sigma_factor(0.05)
rmc_dat.set_moveout_option(True)
rmc_dat.set_time_and_save(15, 1)
rmc_dat.set_exp_range(1, 588)
rmc_dat.set_r_spacing(0.025)
rmc_dat.set_data_flags([0, 0, 1, 0])
rmc_dat.set_swap_settings(0.0, 0)
rmc_dat.set_num_atoms_per_move(1)
rmc_dat.write()
```

`set_density()` は原子数密度（Å⁻³）、`set_cutoffs()` は原子種ペアごとの最短距離（Å）、`set_maximum_moves()` は原子種ごとの最大移動量（Å）、`set_r_spacing()` は動径ヒストグラム間隔（Å）を指定します。`set_time_and_save(15, 1)` は RMC_POT の実行時間・保存時間の設定です。`set_exp_range(1, 588)` は実験データの点範囲であり、`set_data_flags([0, 0, 1, 0])` は使用データ種のフラグです。数値は SiO₂ の一設定例であり、測定点数・密度・原子種順序に合わせて変更します。

## 原子種の数による書き方

cutoff の個数は原子種数 $n$ に対して $n(n+1)/2$ 個です。`set_maximum_moves()` は原子種数と同じ個数です。以下のブロックは**相互に独立した選択例**であり、一つの計算にすべて適用するものではありません。

**SiO₂（Si, O）**

```python
rmc_dat.set_density(0.0665715652)
rmc_dat.set_cutoffs([2.40, 1.25, 2.10])  # Si-Si, Si-O, O-O
rmc_dat.set_maximum_moves([0.01, 0.01])  # Si, O
```

**Fe–Si–B（Fe, Si, B）**

```python
rmc_dat.set_density(0.0915)
rmc_dat.set_cutoffs([2.2, 1.9, 1.75, 1.8, 1.75, 1.5])
# Fe-Fe, Fe-Si, Fe-B, Si-Si, Si-B, B-B
rmc_dat.set_maximum_moves([0.1, 0.1, 0.1])
```

**Li₃PO₄（Li, P, O）**

```python
rmc_dat.set_density(0.0772877)
rmc_dat.set_cutoffs([
    1.8,  # Li-Li
    2.0,  # Li-P
    1.7,  # Li-O
    2.5,  # P-P
    1.3,  # P-O
    2.0,  # O-O
])
rmc_dat.set_maximum_moves([0.1, 0.1, 0.1])
```

**ゼオライト（Si, Al, O, Na）**

```python
rmc_dat.set_density(0.0570880440)
rmc_dat.set_cutoffs([
    2.10, 2.20, 1.35, 2.20,  # Si-Si, Si-Al, Si-O, Si-Na
    2.20, 1.50, 2.20,        # Al-Al, Al-O, Al-Na
    2.00, 1.90, 2.30,        # O-O, O-Na, Na-Na
])
rmc_dat.set_maximum_moves([0.01, 0.01, 0.01, 0.01])
```

**Li–S–P–C（Li, S, P, C）**

```python
rmc_dat.set_density(0.0453277972)
rmc_dat.set_cutoffs([
    1.80, 1.80, 1.80, 1.70,  # Li-Li, Li-S, Li-P, Li-C
    1.80, 1.75, 1.60,        # S-S, S-P, S-C
    1.80, 1.60, 1.30,        # P-P, P-C, C-C
])
rmc_dat.set_maximum_moves([0.01, 0.01, 0.01, 0.01])
```

## 自由形式に固有の設定

固定形式・自由形式に共通する setter と異なり、`[ COS ]`、`[ COORD ]`、`[ SNC ]`、AENET ポテンシャルなどのセクション操作は自由形式の機能です。`is_free_format` を確認して指定します。原子種番号は `.cfg` の原子種順序に対応します。

```python
if rmc_dat.is_free_format:
    rmc_dat.set_element_info(["Si", "O"])
    rmc_dat.set_history_buffer_size(200)
```

### 結合角：SiO₂ とゼオライト

以下は異なる原子種番号・距離範囲の例です。

```python
# SiO2: 1=Si, 2=O; O-Si-O
rmc_dat.set_angle_constraint(
    central_type=1,
    neighbor1=(2, 1.40, 1.90),
    neighbor2=(2, 1.40, 1.90),
    distribution_type="GAUSSIAN",
    angle_degrees=109.47,
    distribution_width=0.12,  # cos(theta) 空間の幅
    dcosth=0.05,
    sigma=0.01,
    index=0,
)
```

```python
# ゼオライト: 1=Si, 2=Al, 3=O, 4=Na
rmc_dat.set_angle_constraint(
    central_type=1,
    neighbor1=(3, 1.40, 1.90),
    neighbor2=(3, 1.40, 1.90),
    distribution_type="GAUSSIAN",
    angle_degrees=109.47,
    distribution_width=0.12,
    dcosth=0.05,
    sigma=0.03,
    index=0,
)
rmc_dat.set_angle_constraint(
    central_type=2,
    neighbor1=(3, 1.55, 2.10),
    neighbor2=(3, 1.55, 2.10),
    distribution_type="GAUSSIAN",
    angle_degrees=109.47,
    distribution_width=0.15,
    dcosth=0.05,
    sigma=0.03,
    index=1,
)
```

### 配位数：単一近接種と複数近接種

`neighbors` は `(原子種番号, rmin, rmax)` のリスト、`subconstraints` は `(配位数, 目標割合, sigma)` のリストです。複数の配位数分布は**一つの `subconstraints` にまとめる**書き方ができます。

```python
# SiO2: Si-O 配位数分布
rmc_dat.set_coord_constraint(
    central_type=1,
    neighbors=[(2, 1.40, 1.90)],
    subconstraints=[
        (4, 0.998, 0.003),
        (5, 0.002, 0.012),
    ],
    index=0,
)
```

```python
# ゼオライト: O の Si + Al 合計配位数を2に設定
rmc_dat.set_coord_constraint(
    central_type=3,
    neighbors=[
        (1, 1.40, 1.90),  # Si
        (2, 1.55, 2.10),  # Al
    ],
    subconstraints=[(2, 1.0, 0.01)],
    index=2,
)
```

## FNC と分子トポロジー

FNC は既存 `.fnc` に記述された**原子番号で指定する固定近接関係**を用います。`set_fnc_switch(3)` は FNC の `MOVE-IN` モード、`set_fnc_switch(4)` はトポロジーに対応するモードです。**同時に有効化するものではありません。** 自由形式のトポロジーモードでは `[ BPOT ]` が用いられ、`FNC-TYPE` 自体は `NONE` になります。

```python
# 分子の FNC: aaa.fnc を用意した場合
rmc_dat.set_fnc_switch(3)
rmc_dat.set_fnc_distance_ranges({
    1: (1.20, 1.80),  # 既存 FNC の constraint type 1
})
```

```python
# 別の計算例: aaa.top を用いるトポロジーモード
rmc_dat.set_fnc_switch(4)
```

`set_fnc_distance_ranges()` は `.fnc` の既存の原子ペアや constraint type を作り直すものではなく、既存 type の距離範囲のみを更新します。RMC_POT マニュアル I.N、I.Q、II の FNC・topology・ポテンシャル仕様、および [FNC API](../api/rmc_pot_dat_fnc.md)、[TOP API](../api/rmc_pot_dat_top.md) を参照してください。

## 実行スクリプトとの接続

`rmc.py` は `Config("config.yml")`、`RmcPotLog`、`RmcPotDat` を生成し、`run_rmc_init(config=config, rmc_dat=rmc_dat, logger=logger)` で計算条件を編集した後、`run_rmc()` を呼び出します。`rmc_init.py` の `run_rmc_init()` 内に本ページの設定を記述できます。設定例の各ブロックは対象の物質系・制約方式に応じて選択します。

RMC_POT マニュアルの対応箇所は I.C（cutoff）、I.K（角度）、I.L（配位数）、I.N（FNC）、I.O.2（SNC/Qn）、I.Q（ポテンシャル）、II.C（`.dat` 形式）です。RMC_UTIL の共通 API は [RmcPotDat](../api/rmc_pot_dat.md) にまとめています。
