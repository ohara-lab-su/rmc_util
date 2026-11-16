# `rmc_util.install`

ソース: `src/rmc_util/install.py`

## `find_installed_scripts()`

インストール先と配布記録を調べ、同名の雛形を一度だけ取得する。

## `install_scripts(destination: Path, *, force: bool=False)`

雛形を配置する。forceが真のときだけ既存ファイルを上書きする。

## `main()`

--force指定時のみ既存の雛形を上書きする。


## 実装に基づく API 一覧

この一覧は提供された `install.py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### モジュール関数 `find_installed_scripts()`

- 定義位置：19 行
- 説明：インストール先と配布記録を調べ、同名の雛形を一度だけ取得する。

### モジュール関数 `install_scripts()`

- 定義位置：41 行
- 説明：雛形を配置する。forceが真のときだけ既存ファイルを上書きする。

### モジュール関数 `main()`

- 定義位置：76 行
- 説明：--force指定時のみ既存の雛形を上書きする。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `find_installed_scripts`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `list[Path]`。定義位置: `install.py:19`。

### `install_scripts`

| 引数 | 型注釈 |
|---|---|
| `destination` | `Path` |
| `force` | `bool` |

戻り値の型注釈: `tuple[int, int]`。定義位置: `install.py:41`。

### `main`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `None`。定義位置: `install.py:76`。

