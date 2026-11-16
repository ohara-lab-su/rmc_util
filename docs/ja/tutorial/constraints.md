# 3. 自由形式の構造制約

以下は README の coordination / Qn 設定例です。自由形式を指定して初期化します。

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(cfg_name="sample", use_free_format=True)
rmc_dat.init(use_free_format=True, prefer_existing=True)
rmc_dat.set_element_info(["Si", "O"])
rmc_dat.set_coord_constraint(
    central_type=1,
    neighbors=[(2, 1.40, 1.90)],
    subconstraints=[(4, 1.0, 0.01)],
    index=0,
)
rmc_dat.set_qn_constraint(
    central_type=1,
    first_neighbor_type=2,
    first_neighbor_minimum=1.45,
    first_neighbor_maximum=1.80,
    second_neighbors=[(1, 1.45, 1.80)],
    coordination_number=4,
    fraction=1.0,
    sigma=0.04,
    index=0,
)
```

制約の物理的意味と RMC_POT の書式は [RMC 法・ファイル形式の解説](../reference/index.md) に分離しています。FNC は `RmcPotDatFnc`、topology は `RmcPotDatTop` を使用します。

[API: 自由形式](../api/rmc_pot_dat_free.md) / [FNC](../api/rmc_pot_dat_fnc.md) / [topology](../api/rmc_pot_dat_top.md)

## SNC / Qn：ネットワーク形成

SNC は単なる第一近接配位数とは異なり、中心原子―第一近接原子―第二近接原子の連結を評価します。`coordination_number` は条件を満たす第一近接原子の数、`fraction` は条件を満たす中心原子の目標割合（0～1）です。各 `index` は独立した `[ SNC ]` セクションに対応します。

```python
# SiO2: 1=Si, 2=O。Q5 / Q4 / Q3 を別々の SNC として設定
for index, coordination_number, fraction in [
    (0, 5, 0.002),
    (1, 4, 0.994),
    (2, 3, 0.004),
]:
    rmc_dat.set_qn_constraint(
        central_type=1,
        first_neighbor_type=2,
        first_neighbor_minimum=1.45,
        first_neighbor_maximum=1.80,
        second_neighbors=[(1, 1.45, 1.80)],
        coordination_number=coordination_number,
        fraction=fraction,
        sigma=0.04,
        index=index,
    )
```

```python
# ゼオライト: Si-O-(Si/Al) と Al-O-(Si/Al)
rmc_dat.set_qn_constraint(
    central_type=1,
    first_neighbor_type=3,
    first_neighbor_minimum=1.40,
    first_neighbor_maximum=1.90,
    second_neighbors=[(1, 1.40, 1.90), (2, 1.55, 2.10)],
    coordination_number=4,
    fraction=1.0,
    sigma=0.03,
    index=0,
)
rmc_dat.set_qn_constraint(
    central_type=2,
    first_neighbor_type=3,
    first_neighbor_minimum=1.55,
    first_neighbor_maximum=2.10,
    second_neighbors=[(1, 1.40, 1.90), (2, 1.55, 2.10)],
    coordination_number=4,
    fraction=1.0,
    sigma=0.03,
    index=1,
)
```

Al–O–Al の連結を SNC の第二近接候補から除外する場合は、Al 中心の `second_neighbors` を `[(1, 1.40, 1.90)]` とします。これは第二近接候補の指定であり、結合相手の個別原子番号を固定する FNC とは異なります。RMC_POT マニュアル I.O.2、自由形式 `[ SNC ]` を参照してください。

## ANNポテンシャル（自由形式）

```python
rmc_dat.set_aenet_potential(
    potentials=[
        (1, "Si.nn", "Si"),
        (2, "O.nn", "O"),
    ],
    sigma=1.0,
    aenet_step=1,
    write_atomic_energy=True,
)
```

`Si.nn` と `O.nn` は実行ディレクトリに配置します。RMC_POT 側には AENET 対応ビルドが必要です。`sigma` はANNエネルギー項の重みであり、実験データの誤差を直接表すものではありません。マニュアル I.Q.2 の ANN ポテンシャルの項目と対応します。
