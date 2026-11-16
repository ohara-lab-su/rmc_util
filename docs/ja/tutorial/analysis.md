# 5. 計算結果の解析

`rmc_util` は RMC_POT 実行と独立して、既存の計算結果を解析できます。

| クラス | 対象 | 主な取得内容 |
| --- | --- | --- |
| `RmcPotLog` | ログ | block / loop、generated / tried / accepted、χ²、Rw |
| `RmcPotHst` | `.hst` | 受理率、χ²履歴、収束判定 |
| `RmcPotFit` | `.fit` | 計算値・実験値、S(Q) |
| `RmcPotPpcf` | `.ppcf` | 距離配列と部分二体分布関数 |
| `RmcPotSnc` | `.snc` | Qn 分布 |

`.hst` の収束判定は次のように呼び出します。

```python
from rmc_util import RmcPotHst

hst = RmcPotHst(cfg_name="sample")
loop = hst.detect_convergence(
    rel_tol=1.0e-2,
    acc_tol=1.0e-3,
    min_consecutive=2,
)
```

[API: log](../api/rmc_pot_log.md) / [hst](../api/rmc_pot_hst.md) / [fit](../api/rmc_pot_fit.md) / [ppcf](../api/rmc_pot_ppcf.md) / [snc](../api/rmc_pot_snc.md)

出力形式そのものは [RMC_POT 出力ファイルの解説](../reference/rmcpot_output_explained.md) を参照してください。
