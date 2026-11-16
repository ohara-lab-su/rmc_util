# `rmc_util.rmc_pot_fit`

ソース: `src/rmc_util/rmc_pot_fit.py`

## クラス `RmcPotFit`

RMC_POT の .fit ファイルを読み取って、
Q, F(Q)、renormalized F(Q)_exp などを保持するクラス。

### `__init__(self, *, fit_name: Optional[str]=None, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

Args:
    fit_name (str): aaa.fit まで含めた名前
    cfg_name (str): cfg_name.fit (.fitを含むフルのファイル名)
    config (Config):
    logger (XLogger):

### `read_fit(self, filename: Optional[str]=None)`

.fit ファイルを読み取り、主要データ列を格納する。
self.filename: fullname

Args:
    filename:

Returns:

### `get_S_calc(self)`

S_calc(Q) = F_calc + 1
RMC_POT の F(Q) はこちらの形

### `get_S_exp(self)`

S_exp(Q) = renormalized F_exp + 1

### `get_S_exp_original(self)`

S_exp_original(Q) = original F_exp + 1

### `as_dict(self)`

辞書形式で返したい場合に使用


## 実装に基づく API 一覧


### `RmcPotFit` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 20 | Args: |
| `read_fit()` | 59 | .fit ファイルを読み取り、主要データ列を格納する。 |
| `get_S_calc()` | 114 | S_calc(Q) = F_calc + 1 |
| `get_S_exp()` | 136 | S_exp(Q) = renormalized F_exp + 1 |
| `get_S_exp_original()` | 140 | S_exp_original(Q) = original F_exp + 1 |
| `as_dict()` | 144 | 辞書形式で返したい場合に使用 |

## ソースコードに基づく引数・戻り値一覧


### `RmcPotFit.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `fit_name` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot_fit(7).py:20`。

### `RmcPotFit.read_fit`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `filename` | `Optional[str]` |

戻り値の型注釈: `Optional[bool]`。定義位置: `rmc_pot_fit(7).py:59`。

### `RmcPotFit.get_S_calc`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[float]`。定義位置: `rmc_pot_fit(7).py:114`。

### `RmcPotFit.get_S_exp`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[float]`。定義位置: `rmc_pot_fit(7).py:136`。

### `RmcPotFit.get_S_exp_original`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[float]`。定義位置: `rmc_pot_fit(7).py:140`。

### `RmcPotFit.as_dict`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Dict[str, List[float]]`。定義位置: `rmc_pot_fit(7).py:144`。

