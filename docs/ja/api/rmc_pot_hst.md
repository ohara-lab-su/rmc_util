# `rmc_util.rmc_pot_hst`

RMC_POT の `.hst` 履歴ファイルを読み込み、RMCループごとの統計量と収束判定を扱います。

ソース: `src/rmc_util/rmc_pot_hst.py`

## `RmcPotHst`

`.hst` の履歴表から、`generated`、`tried`、`accepted`、`time`、`tried_per_gen`、`acc_per_tried`、`chi2_tot`、`chi2_set1` の8列を読み取ります。ヘッダー以降の数値行が履歴レコードです。

### `__init__(self, hst_name=None, cfg_name=None, config=None, logger=None)`

ファイルの選択優先順位は `hst_name`、`cfg_name`、`config` の順です。`hst_name` はそのままファイル名として使用し、`cfg_name` には `.hst` を付けます。

**実装上の注意:** `config` だけを指定した場合、渡されたオブジェクトを使用せず `Config("config.yaml")` を再生成します。

```python
RmcPotHst(hst_name="sample.hst")
RmcPotHst(cfg_name="sample")
```

### `read_chi2(self)`

`(steps, chi2)` を返します。`.hst` に明示的なステップ列がないため、`steps` は0始まりのレコード番号です。

### `detect_convergence(self, rel_tol=0.01, acc_tol=0.001, min_consecutive=3)`

隣接するループ間の `chi2_tot` の相対改善率と、`accepted/tried` の両方を判定します。

```text
delta = (chi2[i - 1] - chi2[i]) / chi2[i - 1]
delta < rel_tol
accepted / tried < acc_tol
```

条件を `min_consecutive` 回連続で満たしたとき、その連続区間の最初のループ番号を返します。条件を満たさなければ `None` を返します。

### `detect_convergence_set1(self, rel_tol=0.01, acc_tol=0.001, min_consecutive=2)`

`chi2_tot` の代わりに第1データセットの `chi2_set1`（`.hst` の `chi2/F(Q)_set#1`）を用いる収束判定です。

### `get_num_rmc_loops(self)`

読み込んだ履歴レコード数を整数で返します。

## 履歴値の取得

### `get_generated(self, loop_index=None)`

履歴列 `generated`（生成した移動数）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[int, List[int]]`。

### `get_tried(self, loop_index=None)`

履歴列 `tried`（試行した移動数）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[int, List[int]]`。

### `get_accepted(self, loop_index=None)`

履歴列 `accepted`（受理された移動数）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[int, List[int]]`。

### `get_time(self, loop_index=None)`

履歴列 `time`（履歴に記録された時間）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[int, List[int]]`。

### `get_tried_per_generated(self, loop_index=None)`

履歴列 `tried_per_gen`（生成数に対する試行数の比）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[float, List[float]]`。

### `get_accepted_per_tried(self, loop_index=None)`

履歴列 `acc_per_tried`（試行数に対する受理数の比）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[float, List[float]]`。

### `get_chi2_tot(self, loop_index=None)`

履歴列 `chi2_tot`（全データセットのχ²評価量）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[float, List[float]]`。

### `get_chi2_set1(self, loop_index=None)`

履歴列 `chi2_set1`（第1データセットのχ²評価量）を取得します。
 
`loop_index=None` なら全レコードのリスト、整数を指定するとそのレコードの値を返します。

戻り値: `Union[float, List[float]]`。

## 実装との対応

| メソッド | 定義行 |
|---|---:|
| `__init__` | 41 |
| `read_chi2` | 202 |
| `detect_convergence` | 231 |
| `detect_convergence_set1` | 327 |
| `get_num_rmc_loops` | 368 |
| `get_generated` | 382 |
| `get_tried` | 413 |
| `get_accepted` | 441 |
| `get_time` | 469 |
| `get_tried_per_generated` | 497 |
| `get_accepted_per_tried` | 525 |
| `get_chi2_tot` | 553 |
| `get_chi2_set1` | 575 |
