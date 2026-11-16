# 2. `.dat` の作成・編集

`RmcPotDat` は固定形式・自由形式を共通の操作で扱うラッパーです。`init()` は既存ファイルの形式判定・読込または新規作成を行います。

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(cfg_name="sample", auto_write=False, use_free_format=True)
rmc_dat.init(use_free_format=True, prefer_existing=True)
rmc_dat.set_comment("SiO2 sample", auto_write=False)
rmc_dat.set_density(0.0665715652, auto_write=False)
rmc_dat.set_cutoffs([1.9, 1.1, 1.9], auto_write=False)
rmc_dat.set_maximum_moves([0.01, 0.01], auto_write=False)
rmc_dat.set_r_spacing(0.025, auto_write=False)
rmc_dat.write()
```

`prefer_existing=True` のときは既存 `.dat` を優先し、形式を自動判定します。`auto_write=False` は編集をまとめ、最後に `write()` で保存する用途に適します。数値は README 掲載の例であり、研究対象に応じて設定してください。

[API: RmcPotDat](../api/rmc_pot_dat.md) / [固定形式](../api/rmc_pot_dat_fixed.md) / [自由形式](../api/rmc_pot_dat_free.md)
