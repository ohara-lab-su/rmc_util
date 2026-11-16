# 計算結果の解析

RMC_UTIL では、RMC_POT の出力ファイルを種類ごとのクラスで読み取ります。ファイルの存在と読込み可否、計算の終了状態、実験データへの適合度、構造制約の充足はそれぞれ別に確認します。

| クラス | 対象ファイル | 解析内容 |
| --- | --- | --- |
| `RmcPotLog` | ログ | 計算ブロック、移動の生成・試行・受理回数、χ²、Rw、終了状態 |
| `RmcPotHst` | `.hst` | χ²履歴、移動受理率、停滞に基づく収束判定 |
| `RmcPotFit` | `.fit` | 計算・実験プロファイルと散乱関数 |
| `RmcPotPpcf` | `.ppcf` | 距離軸と原子種対ごとの部分二体分布関数 |
| `RmcPotSnc` | `.snc` | Second Neighbour Constraint の中心原子ごとの配位数と Qn 分布 |

## χ²履歴と受理率

`RmcPotHst` は、指定した `.hst` ファイルを読み込んで履歴を解析します。`detect_convergence()` は、隣接する記録間のχ²の相対改善率と移動受理率が、指定したしきい値を連続して満たす最初のループを返します。判定できない場合は `None` を返します。

```python
from rmc_util import RmcPotHst

hst = RmcPotHst(cfg_name="sample")
loop = hst.detect_convergence(
    rel_tol=1.0e-2,
    acc_tol=1.0e-3,
    min_consecutive=3,
)
```

この判定は探索の停滞を示すもので、実験データとの一致や構造の妥当性を保証しません。χ²とRwの推移、`.fit` の残差、`.ppcf` の原子間距離と配位環境を併せて評価します。

## SNCによるQn分布の確認

`.snc` の解析にはファイルパスを指定します。`get_qn_counts()` は指定した制約ブロックのQn別中心原子数を辞書で返します。複数の制約ブロックで同じ中心原子の配位数が記録されている場合は、`get_common_qn_counts()` で共通の分布を取得できます。一致しない場合は `ValueError` になります。

```python
from rmc_util.rmc_pot_snc import RmcPotSnc

snc = RmcPotSnc("sample.snc")
qn_counts = snc.get_qn_counts(constraint_index=0)
```

Qnの意味は対象のネットワークと制約の定義に依存します。制約ブロックごとの中心原子・第二近接原子の指定と対応させて解釈します。

各クラスのメソッドは [APIリファレンス](../api/index.md)、出力データの形式は [RMC_POT出力ファイル](../reference/rmcpot_output_explained.md) を参照してください。
