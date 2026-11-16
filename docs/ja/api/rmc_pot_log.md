# `rmc_util.rmc_pot_log`

ソース: `src/rmc_util/rmc_pot_log.py`

## クラス `RmcPotLog`

ソースにクラス説明の docstring はありません。

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, log_filename: Optional[str]=None)`

config インスタンスを与えると、cfg_name はいらない

Args:
    config (Config): 全てインスタンスが同じ Config()
    logger (XLogger): 全てのインスタンスが同じ XLogger()
    cfg_name (str):
    log_filename (str): jobファイル中にRMCのログを垂れ流した時はそれを書く
                        この指定がない時は cfg_name.log がログファイルとなる

### `load_log(self, log_filename: str=None)`

log ファイルが存在するなら読み込み、
self._log_lines に保存する。
(保存される内容はファイル全てなので、ファイルの中身は実はどうでもいい)

### `set_cfg_name(self, cfg_name: str)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_cfg_name(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `is_finished(self)`

ログの「最後の RMC パート」が正常終了しているかを判定する。

- RMC パートが一度も現れない       → False
- 最後の RMC パートが start のみ   → False
- 最後の RMC パートが start〜end   → True

ここでの「最後」は、ログの末尾から見て最後に現れた
RMC_POT++ program ... の開始ブロックを意味する。

### `get_num_rmc_block(self)`

ログ中に出現した RMC パートの個数（開始ブロックの個数）を返す。
未完のブロックも 1 と数える。

### `get_num_rmc_loop(self, block_index: int)`

RMC ブロック内での loop 数の数
Args:
    block_index:

Returns:

### `get_generated(self, block: int, loop: int)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_tried(self, block: int, loop: int)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_accepted(self, block: int, loop: int)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_chi2_tot(self, block: int, loop: int)`

Hst 側に合わせて golbal -> tot に名前を変える
(意味が変わってしまうかもしれないので注意)

おそらく
log側 (global)
hst側 (total)
で同じものを指している

Args:
    block:
    loop:

Returns:

### `get_chi2_dataset(self, block: int, loop: int)`

Golobal に対して、データーセット別の意味で dataset

もともと、
hst 側では set1(特定セット)
log 側では dataset(個別セット)
統計集団が異なる可能性があるので注意

Args:
    block:
    loop:

Returns:

### `get_rw(self, block: int, loop: int)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_tried_per_generated(self, block: int, loop: int)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_accepted_per_tried(self, block: int, loop: int)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `clear(self, cfg_name: str)`

rmc_pot の出力ファイルを消す

Args:
    cfg_name (str):

Returns:

### `remove_file(self, filename: str)`

現在の作業ディレクトリ（スクリプト実行フォルダ）にある指定ファイルを削除する。

Args:
    filename (str): 削除するファイル名（相対/絶対どちらでも可）

### `collect_result(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `backup_result(self, log_dir: Optional[str]=None, cfg_name: Optional[str]=None)`

Copy RMC log files to the specified directory.

Args:
    log_dir (str): Directory to copy the log files to.
    cfg_name (str): Name of the configuration file.


## 実装に基づく API 一覧

この一覧は提供された `rmc_pot_log(7).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `RmcPotLog` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 21 | config インスタンスを与えると、cfg_name はいらない |
| `load_log()` | 65 | log ファイルが存在するなら読み込み、 |
| `set_cfg_name()` | 99 | ソース内に説明なし |
| `get_cfg_name()` | 109 | ソース内に説明なし |
| `is_finished()` | 521 | ログの「最後の RMC パート」が正常終了しているかを判定する。 |
| `get_num_rmc_block()` | 552 | ログ中に出現した RMC パートの個数（開始ブロックの個数）を返す。 |
| `get_num_rmc_loop()` | 560 | RMC ブロック内での loop 数の数 |
| `get_generated()` | 584 | ソース内に説明なし |
| `get_tried()` | 594 | ソース内に説明なし |
| `get_accepted()` | 604 | ソース内に説明なし |
| `get_chi2_tot()` | 614 | Hst 側に合わせて golbal -> tot に名前を変える |
| `get_chi2_dataset()` | 636 | Golobal に対して、データーセット別の意味で dataset |
| `get_rw()` | 657 | ソース内に説明なし |
| `get_tried_per_generated()` | 663 | ソース内に説明なし |
| `get_accepted_per_tried()` | 677 | ソース内に説明なし |
| `clear()` | 695 | rmc_pot の出力ファイルを消す |
| `remove_file()` | 740 | 現在の作業ディレクトリ（スクリプト実行フォルダ）にある指定ファイルを削除する。 |
| `collect_result()` | 759 | ソース内に説明なし |
| `backup_result()` | 762 | Copy RMC log files to the specified directory. |

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `RmcPotLog.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |
| `cfg_name` | `Optional[str]` |
| `log_filename` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_log(7).py:21`。

### `RmcPotLog.load_log`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `log_filename` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_log(7).py:65`。

### `RmcPotLog.set_cfg_name`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_log(7).py:99`。

### `RmcPotLog.get_cfg_name`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_log(7).py:109`。

### `RmcPotLog.is_finished`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_log(7).py:521`。

### `RmcPotLog.get_num_rmc_block`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_log(7).py:552`。

### `RmcPotLog.get_num_rmc_loop`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block_index` | `int` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_log(7).py:560`。

### `RmcPotLog.get_generated`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[int]`。定義位置: `rmc_pot_log(7).py:584`。

### `RmcPotLog.get_tried`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[int]`。定義位置: `rmc_pot_log(7).py:594`。

### `RmcPotLog.get_accepted`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[int]`。定義位置: `rmc_pot_log(7).py:604`。

### `RmcPotLog.get_chi2_tot`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[float]`。定義位置: `rmc_pot_log(7).py:614`。

### `RmcPotLog.get_chi2_dataset`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[float]`。定義位置: `rmc_pot_log(7).py:636`。

### `RmcPotLog.get_rw`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[float]`。定義位置: `rmc_pot_log(7).py:657`。

### `RmcPotLog.get_tried_per_generated`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[float]`。定義位置: `rmc_pot_log(7).py:663`。

### `RmcPotLog.get_accepted_per_tried`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `block` | `int` |
| `loop` | `int` |

戻り値の型注釈: `Optional[float]`。定義位置: `rmc_pot_log(7).py:677`。

### `RmcPotLog.clear`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_log(7).py:695`。

### `RmcPotLog.remove_file`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `filename` | `str` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_log(7).py:740`。

### `RmcPotLog.collect_result`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot_log(7).py:759`。

### `RmcPotLog.backup_result`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `log_dir` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot_log(7).py:762`。

