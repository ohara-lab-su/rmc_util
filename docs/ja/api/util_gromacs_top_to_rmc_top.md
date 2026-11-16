# `rmc_util.util.gromacs_top_to_rmc_top`

ソース: `src/rmc_util/util/gromacs_top_to_rmc_top.py`

## クラス `TopologyConvertError`

GROMACS topology から RMC_POT topology への変換に失敗した場合の例外。

## クラス `GroAtom`

GROMACS gro ファイルの 1 原子分の情報。

### `__init__(self, index: int, residue_name: str, atom_name: str)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

## クラス `MoleculeType`

topology 中の molecule type 定義。

### `__init__(self, name: str, nrexcl: str)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

## クラス `TopologyInfo`

topology の変換に必要な最小情報。

### `__init__(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

## `read_text_lines(path: str)`

テキストファイルを行末付きで読む。

## `write_text_lines(path: str, lines: Sequence[str])`

テキストファイルを書き出す。

## `read_gro(path: str)`

GROMACS gro ファイルを読み、原子順を返す。

gro の原子番号欄は 99999 で wrap することがあるため、ここではファイル内の出現順を
1 始まり index として扱う。

## `expand_local_includes(top_path: str, lines: Sequence[str], include_dirs: Optional[Sequence[str]]=None, expand_local_itp: bool=False, _seen: Optional[set]=None)`

ローカル分子定義用 itp を必要に応じて展開する。

force-field include らしい ``ff*.itp`` は展開せず、そのまま残す。

## `parse_topology_info(lines: Sequence[str])`

topology から molecule type と molecules 数を読む。

## `build_rmc_index_map(info: TopologyInfo)`

molecule type ごとの offset と local atom ごとの RMC index を作る。

戻り値:
    offsets: molecule type -> その type の最初の RMC index の直前までの原子数。
    index_map: (molecule type, local atom index) -> occurrence ごとの RMC index list。
    total_atoms: topology から期待される総原子数。

## `replace_force_field_include(lines: Sequence[str], force_field_include: Optional[str])`

force-field include を必要に応じて置換する。

``force_field_include`` が None なら何もしない。
既存の ``#include "ff*.itp"`` があれば最初の 1 個を置換する。
無ければ ``[ defaults ]`` ブロックの直後に挿入する。

## `convert_topology_lines(top_lines: Sequence[str], gro_atoms: Sequence[GroAtom], force_field_include: Optional[str]=None)`

GROMACS topology 行列を RMC_POT 用 topology 行列へ変換する。

## `convert_gromacs_top_to_rmc_top(top_path: str, gro_path: str, output_path: str, force_field_include: Optional[str]=None, include_dirs: Optional[Sequence[str]]=None, expand_local_itp: bool=False)`

GROMACS ``*.top`` と ``*.gro`` から RMC_POT 用 ``*.top`` を生成する。

## `build_arg_parser()`

CLI 用 argument parser を作る。

## `main(argv: Optional[Sequence[str]]=None)`

CLI entry point。


## 実装に基づく API 一覧

この一覧は提供された `gromacs_top_to_rmc_top(2).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `TopologyConvertError` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### `GroAtom` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 54 | ソース内に説明なし |

### `MoleculeType` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 63 | ソース内に説明なし |

### `TopologyInfo` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 72 | ソース内に説明なし |

### モジュール関数 `read_text_lines()`

- 定義位置：109 行
- 説明：テキストファイルを行末付きで読む。

### モジュール関数 `write_text_lines()`

- 定義位置：115 行
- 説明：テキストファイルを書き出す。

### モジュール関数 `read_gro()`

- 定義位置：125 行
- 説明：GROMACS gro ファイルを読み、原子順を返す。

### モジュール関数 `expand_local_includes()`

- 定義位置：176 行
- 説明：ローカル分子定義用 itp を必要に応じて展開する。

### モジュール関数 `parse_topology_info()`

- 定義位置：239 行
- 説明：topology から molecule type と molecules 数を読む。

### モジュール関数 `build_rmc_index_map()`

- 定義位置：310 行
- 説明：molecule type ごとの offset と local atom ごとの RMC index を作る。

### モジュール関数 `replace_force_field_include()`

- 定義位置：378 行
- 説明：force-field include を必要に応じて置換する。

### モジュール関数 `convert_topology_lines()`

- 定義位置：430 行
- 説明：GROMACS topology 行列を RMC_POT 用 topology 行列へ変換する。

### モジュール関数 `convert_gromacs_top_to_rmc_top()`

- 定義位置：489 行
- 説明：GROMACS ``*.top`` と ``*.gro`` から RMC_POT 用 ``*.top`` を生成する。

### モジュール関数 `build_arg_parser()`

- 定義位置：515 行
- 説明：CLI 用 argument parser を作る。

### モジュール関数 `main()`

- 定義位置：544 行
- 説明：CLI entry point。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `GroAtom.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |
| `residue_name` | `str` |
| `atom_name` | `str` |

戻り値の型注釈: `None`。定義位置: `gromacs_top_to_rmc_top(2).py:54`。

### `MoleculeType.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `nrexcl` | `str` |

戻り値の型注釈: `None`。定義位置: `gromacs_top_to_rmc_top(2).py:63`。

### `TopologyInfo.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `gromacs_top_to_rmc_top(2).py:72`。

### `read_text_lines`

| 引数 | 型注釈 |
|---|---|
| `path` | `str` |

戻り値の型注釈: `List[str]`。定義位置: `gromacs_top_to_rmc_top(2).py:109`。

### `write_text_lines`

| 引数 | 型注釈 |
|---|---|
| `path` | `str` |
| `lines` | `Sequence[str]` |

戻り値の型注釈: `None`。定義位置: `gromacs_top_to_rmc_top(2).py:115`。

### `read_gro`

| 引数 | 型注釈 |
|---|---|
| `path` | `str` |

戻り値の型注釈: `List[GroAtom]`。定義位置: `gromacs_top_to_rmc_top(2).py:125`。

### `expand_local_includes`

| 引数 | 型注釈 |
|---|---|
| `top_path` | `str` |
| `lines` | `Sequence[str]` |
| `include_dirs` | `Optional[Sequence[str]]` |
| `expand_local_itp` | `bool` |
| `_seen` | `Optional[set]` |

戻り値の型注釈: `List[str]`。定義位置: `gromacs_top_to_rmc_top(2).py:176`。

### `parse_topology_info`

| 引数 | 型注釈 |
|---|---|
| `lines` | `Sequence[str]` |

戻り値の型注釈: `TopologyInfo`。定義位置: `gromacs_top_to_rmc_top(2).py:239`。

### `build_rmc_index_map`

| 引数 | 型注釈 |
|---|---|
| `info` | `TopologyInfo` |

戻り値の型注釈: `Tuple[Dict[str, int], Dict[Tuple[str, int], List[int]], int]`。定義位置: `gromacs_top_to_rmc_top(2).py:310`。

### `replace_force_field_include`

| 引数 | 型注釈 |
|---|---|
| `lines` | `Sequence[str]` |
| `force_field_include` | `Optional[str]` |

戻り値の型注釈: `List[str]`。定義位置: `gromacs_top_to_rmc_top(2).py:378`。

### `convert_topology_lines`

| 引数 | 型注釈 |
|---|---|
| `top_lines` | `Sequence[str]` |
| `gro_atoms` | `Sequence[GroAtom]` |
| `force_field_include` | `Optional[str]` |

戻り値の型注釈: `Tuple[List[str], TopologyInfo]`。定義位置: `gromacs_top_to_rmc_top(2).py:430`。

### `convert_gromacs_top_to_rmc_top`

| 引数 | 型注釈 |
|---|---|
| `top_path` | `str` |
| `gro_path` | `str` |
| `output_path` | `str` |
| `force_field_include` | `Optional[str]` |
| `include_dirs` | `Optional[Sequence[str]]` |
| `expand_local_itp` | `bool` |

戻り値の型注釈: `TopologyInfo`。定義位置: `gromacs_top_to_rmc_top(2).py:489`。

### `build_arg_parser`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `argparse.ArgumentParser`。定義位置: `gromacs_top_to_rmc_top(2).py:515`。

### `main`

| 引数 | 型注釈 |
|---|---|
| `argv` | `Optional[Sequence[str]]` |

戻り値の型注釈: `int`。定義位置: `gromacs_top_to_rmc_top(2).py:544`。

