# `rmc_util.util.cfg2poscar`

ソース: `src/rmc_util/util/cfg2poscar.py`

## `parse_elements(element_info: Optional[Union[str, Sequence[str]]]=None)`

この関数には docstring がありません。動作の詳細は実装を参照してください。

## `make_vasp_elements_line(elements: List[str])`

この関数には docstring がありません。動作の詳細は実装を参照してください。

## `cfg2poscar(cfg_name: str, vasp_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None, logger: Optional[Any]=None)`

RMCPOT cfg 形式を poscar 形式にする
SAE を使わない独立版(noLIB)

Args:
    cfg_name (str):
    vasp_name (str):
    element_info (str or Sequence[str]):
    logger (Any):
Returns:
    bool:


## 実装に基づく API 一覧


### モジュール関数 `parse_elements()`

- 定義位置：42 行
- 説明：ソース内に説明なし

### モジュール関数 `make_vasp_elements_line()`

- 定義位置：87 行
- 説明：ソース内に説明なし

### モジュール関数 `cfg2poscar()`

- 定義位置：99 行
- 説明：RMCPOT cfg 形式を poscar 形式にする

## ソースコードに基づく引数・戻り値一覧


### `parse_elements`

| 引数 | 型注釈 |
|---|---|
| `element_info` | `Optional[Union[str, Sequence[str]]]` |

戻り値の型注釈: `Optional[List[str]]`。定義位置: `cfg2poscar(5).py:42`。

### `make_vasp_elements_line`

| 引数 | 型注釈 |
|---|---|
| `elements` | `List[str]` |

戻り値の型注釈: `str`。定義位置: `cfg2poscar(5).py:87`。

### `cfg2poscar`

| 引数 | 型注釈 |
|---|---|
| `cfg_name` | `str` |
| `vasp_name` | `Optional[str]` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |
| `logger` | `Optional[Any]` |

戻り値の型注釈: `bool`。定義位置: `cfg2poscar(5).py:99`。

