# `rmc_util.util.poscar2cfg`

ソース: `src/rmc_util/util/poscar2cfg.py`

## `contcar2cfg(cfg_name: str, logger: Optional[Any]=None)`

2025.10.29 update CONTCAR タイプ対応
コア部分を分離

Args:
    cfg_name (str):  CFG 保存用の名前
    logger (str):

Returns:

## `poscar2cfg(cfg_name: str, poscar_name: Optional[str]=None, logger: Optional[Any]=None)`

2025.10.29 update CONTCAR タイプ対応
コア部分を分離

Args:
    cfg_name (str): CFG 保存用の名前
    poscar_name (str):
    logger (Any):

Returns:

## `vasp2cfg(vasp_name: str, cfg_name: str=None, logger: Optional[Any]=None)`

2025.10.29 update CONTCAR タイプ対応

*) poscar2cfg ではなく vasp2cfg にしているのは
   poscar --> xxx.cfg ではなく
   xxx.vasp --> xxx.cfg を意図しているから

Args:
    cfg_name (str): cfg_name.vasp ファイルを読み込む(POSCAR相当)
                    もし、cfg_name.vasp ファイルが存在しなければ
                    CONTCAR を読み込む
    vasp_name (str):
    logger:

Returns:

## `convert_to_cfg(poscar_name: str='POSCAR', cfg_name: str='aaa', logger: Optional[Any]=None)`

name ファイルを中身 POSCAR/CONTCAR とみなして、そのファイルを cfg 形式にする

Args:
    poscar_name (str): この名前のファイルをそのまま読み込む
    cfg_name (str): cfg_name.cfg として書き出す
    logger (XLogger):

Returns:


## 実装に基づく API 一覧

この一覧は提供された `poscar2cfg(8).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### モジュール関数 `contcar2cfg()`

- 定義位置：42 行
- 説明：2025.10.29 update CONTCAR タイプ対応

### モジュール関数 `poscar2cfg()`

- 定義位置：67 行
- 説明：2025.10.29 update CONTCAR タイプ対応

### モジュール関数 `vasp2cfg()`

- 定義位置：98 行
- 説明：2025.10.29 update CONTCAR タイプ対応

### モジュール関数 `convert_to_cfg()`

- 定義位置：137 行
- 説明：name ファイルを中身 POSCAR/CONTCAR とみなして、そのファイルを cfg 形式にする

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `contcar2cfg`

| 引数 | 型注釈 |
|---|---|
| `cfg_name` | `str` |
| `logger` | `Optional[Any]` |

戻り値の型注釈: `指定なし`。定義位置: `poscar2cfg(8).py:42`。

### `poscar2cfg`

| 引数 | 型注釈 |
|---|---|
| `cfg_name` | `str` |
| `poscar_name` | `Optional[str]` |
| `logger` | `Optional[Any]` |

戻り値の型注釈: `bool`。定義位置: `poscar2cfg(8).py:67`。

### `vasp2cfg`

| 引数 | 型注釈 |
|---|---|
| `vasp_name` | `str` |
| `cfg_name` | `str` |
| `logger` | `Optional[Any]` |

戻り値の型注釈: `指定なし`。定義位置: `poscar2cfg(8).py:98`。

### `convert_to_cfg`

| 引数 | 型注釈 |
|---|---|
| `poscar_name` | `str` |
| `cfg_name` | `str` |
| `logger` | `Optional[Any]` |

戻り値の型注釈: `bool`。定義位置: `poscar2cfg(8).py:137`。

