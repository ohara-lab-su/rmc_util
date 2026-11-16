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
