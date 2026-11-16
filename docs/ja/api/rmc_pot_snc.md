# `rmc_util.rmc_pot_snc`

ソース: `src/rmc_util/rmc_pot_snc.py`

## クラス `RmcPotSnc`

RMC_POT の Second Neighbour Constraint 出力を読み取る。

### `__init__(self, path: str)`

``*.snc`` を読み込む。

Args:
    path: 解析する ``*.snc`` ファイル。

### `load(self)`

ファイルを読み直し、制約情報と中心原子ごとの配位数を保持する。

Raises:
    FileNotFoundError: 指定ファイルが存在しない場合。
    ValueError: ``*.snc`` の必須部分を解釈できない場合。

### `get_qn_counts(self, constraint_index: int=0)`

指定制約ブロックに記録された中心原子の Qn 分布を返す。

Args:
    constraint_index: 0 始まりの制約番号。

Returns:
    Qn をキー、中心原子数を値とする辞書。

### `get_common_qn_counts(self)`

全制約に同じ配位数列が保存されていることを確認して分布を返す。

Returns:
    Qn をキー、中心原子数を値とする辞書。

Raises:
    ValueError: 制約ごとの中心原子配位数が一致しない場合。


## 実装に基づく API 一覧


### `RmcPotSnc` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 17 | \`\`*.snc\`\` を読み込む。 |
| `load()` | 27 | ファイルを読み直し、制約情報と中心原子ごとの配位数を保持する。 |
| `get_qn_counts()` | 69 | 指定制約ブロックに記録された中心原子の Qn 分布を返す。 |
| `get_common_qn_counts()` | 82 | 全制約に同じ配位数列が保存されていることを確認して分布を返す。 |

## ソースコードに基づく引数・戻り値一覧


### `RmcPotSnc.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `path` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_snc(3).py:17`。

### `RmcPotSnc.load`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_snc(3).py:27`。

### `RmcPotSnc.get_qn_counts`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `constraint_index` | `int` |

戻り値の型注釈: `Dict[int, int]`。定義位置: `rmc_pot_snc(3).py:69`。

### `RmcPotSnc.get_common_qn_counts`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Dict[int, int]`。定義位置: `rmc_pot_snc(3).py:82`。

