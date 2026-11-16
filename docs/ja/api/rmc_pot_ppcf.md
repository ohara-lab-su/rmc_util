# `rmc_util.rmc_pot_ppcf`

ソース: `src/rmc_util/rmc_pot_ppcf.py`

## クラス `RmcPotPpcf`

ソースにクラス説明の docstring はありません。

### `__init__(self, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Args:
    cfg_name (str):
    config (Config):
    logger (XLogger):

### `load(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_r(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_gij(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `get_single(self, index: int)`

Return one partial g_ij(r) selected by its zero-based index.

### `get_labels(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。


## 実装に基づく API 一覧


### `RmcPotPpcf` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 17 | Args: |
| `load()` | 42 | ソース内に説明なし |
| `get_r()` | 82 | ソース内に説明なし |
| `get_gij()` | 85 | ソース内に説明なし |
| `get_single()` | 88 | Return one partial g_ij(r) selected by its zero-based index. |
| `get_labels()` | 94 | ソース内に説明なし |

## ソースコードに基づく引数・戻り値一覧


### `RmcPotPpcf.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `Optional[str]` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot_ppcf(9).py:17`。

### `RmcPotPpcf.load`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_ppcf(9).py:42`。

### `RmcPotPpcf.get_r`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `np.ndarray`。定義位置: `rmc_pot_ppcf(9).py:82`。

### `RmcPotPpcf.get_gij`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `np.ndarray`。定義位置: `rmc_pot_ppcf(9).py:85`。

### `RmcPotPpcf.get_single`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |

戻り値の型注釈: `np.ndarray`。定義位置: `rmc_pot_ppcf(9).py:88`。

### `RmcPotPpcf.get_labels`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[str]`。定義位置: `rmc_pot_ppcf(9).py:94`。

