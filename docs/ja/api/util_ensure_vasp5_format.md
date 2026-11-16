# `rmc_util.util.ensure_vasp5_format`

ソース: `src/rmc_util/util/ensure_vasp5_format.py`

## `ensure_vasp5_format(poscar_name: str, element_info: Optional[Union[str, Sequence[str]]]=None, logger: Optional[XLogger]=XLogger())`

VASPファイルの6行目にラベルを設定する
VASP4 type POSCAR to VASP5 type POSCAR
繰り返し実行しても副作用はない

RMC pot の cfg 形式は元素名がないために、POSCAR 形式に変換したときに困る場合があるので
VASP5 形式にする (cfg2poscar は element 情報がない VASP4 形式)

Args:
    poscar_name (str): POSCAR
    element_info (str): element 情報があるファイル名 or element のリスト
    logger (XLogger):

Returns:
    bool: True/False


## 実装に基づく API 一覧

この一覧は提供された `ensure_vasp5_format(1).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### モジュール関数 `ensure_vasp5_format()`

- 定義位置：10 行
- 説明：VASPファイルの6行目にラベルを設定する

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `ensure_vasp5_format`

| 引数 | 型注釈 |
|---|---|
| `poscar_name` | `str` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `bool`。定義位置: `ensure_vasp5_format(1).py:10`。

