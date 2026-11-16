# 4. RMC_POT 実行ワークフロー

推奨する通常の実行経路は、`rmc_util install` で展開した `rmc_init.py` の計算条件を編集し、`python rmc.py` で起動する方法です。パッケージ側の `run_rmc()` は `config` を必須とし、`rmc_dat` を呼び出し元から受け取ります。

```python
from rmc_util.runners.run_rmc import run_rmc

ok = run_rmc(
    config=config,
    rmc_log=rmc_log,
    rmc_dat=rmc_dat,
    rmc_pot=None,
    auto_converge=False,
    postprocess=True,
)
```

上記の `config`、`rmc_log`、`rmc_dat` は呼び出し元で初期化済みのオブジェクトを表します。実際の生成と条件設定は配布スクリプト側の責務です。`run_rmc()` は preprocess、FNC/cutoff 整合性確認、RMC 実行、後処理を実施します。`postprocess=True` の場合は実行中断時も `finally` 節で後処理を試みます。`auto_converge=True` の場合は `.hst` を利用して収束判定し、未収束なら次の反復へ進みます。

[API: runner](../api/runners_run_rmc.md) / [RmcPot](../api/rmc_pot.md) / [RmcPotHst](../api/rmc_pot_hst.md)
