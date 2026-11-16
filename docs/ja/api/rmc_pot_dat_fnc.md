# `rmc_util.rmc_pot_dat_fnc`

ソース: `src/rmc_util/rmc_pot_dat_fnc.py`

## クラス `FncNeighbour`

FNC に記録する近接原子 1 件を表す。

Attributes:
    atom_index: 相手原子の 1 始まり RMC index。
    constraint_type: 距離範囲表を参照する制約タイプ番号。

## クラス `RmcPotDatFnc`

RMC_POT ``*.fnc`` ファイルを生成・編集する独立クラス。

低水準メソッドは最終構造の 1 始まり RMC 原子 index を直接扱う。
テンプレート用メソッドはローカル原子番号から RMC index への対応表を
明示的に展開するだけであり、元素名や原子間距離から結合を推定しない。

### `__init__(self, name: str, *, atom_count: Optional[int]=None, auto_write: bool=True, logger: Optional[XLogger]=None)`

インスタンスを初期化する。

Args:
    name: name に指定する値。
    atom_count: atom_count に指定する値。
    auto_write: auto_write に指定する値。
    logger: logger に指定する値。

### `path(self)`

現在の入出力パスを返す。

Returns:
    処理結果。

### `initialize(self, atom_count: int, *, title: Optional[str]=None, auto_write: Optional[bool]=None)`

内部状態を初期化する。

Args:
    atom_count: atom_count に指定する値。
    title: title に指定する値。
    auto_write: auto_write に指定する値。

### `load(self)`

既存ファイルを読み込む。
        

### `write(self, out_name: Optional[str]=None)`

現在の内部状態をファイルへ書き出す。

Args:
    out_name: out_name に指定する値。

### `set_title(self, title: str, *, auto_write: Optional[bool]=None)`

title を設定する。

Args:
    title: title に指定する値。
    auto_write: auto_write に指定する値。

### `get_title(self)`

title を取得する。

Returns:
    処理結果。

### `get_atom_count(self)`

atom count を取得する。

Returns:
    処理結果。

### `set_distance_range(self, constraint_type: int, rmin: float, rmax: float, *, auto_write: Optional[bool]=None)`

distance range を設定する。

Args:
    constraint_type: constraint_type に指定する値。
    rmin: rmin に指定する値。
    rmax: rmax に指定する値。
    auto_write: auto_write に指定する値。

### `set_distance_ranges(self, ranges: Union[Mapping[int, Tuple[float, float]], Sequence[Tuple[float, float]]], *, auto_write: Optional[bool]=None)`

distance ranges を設定する。

Args:
    ranges: ranges に指定する値。
    auto_write: auto_write に指定する値。

### `get_distance_ranges(self)`

distance ranges を取得する。

Returns:
    処理結果。

### `set_atom_neighbours(self, atom_index: int, neighbours: Iterable[Union[FncNeighbour, Tuple[int, int]]], *, auto_write: Optional[bool]=None)`

atom neighbours を設定する。

Args:
    atom_index: atom_index に指定する値。
    neighbours: neighbours に指定する値。
    auto_write: auto_write に指定する値。

### `get_atom_neighbours(self, atom_index: int)`

atom neighbours を取得する。

Args:
    atom_index: atom_index に指定する値。

Returns:
    処理結果。

### `add_neighbour(self, atom_index: int, neighbour_index: int, constraint_type: int, *, reciprocal: bool=False, auto_write: Optional[bool]=None)`

neighbour を追加する。

Args:
    atom_index: atom_index に指定する値。
    neighbour_index: neighbour_index に指定する値。
    constraint_type: constraint_type に指定する値。
    reciprocal: reciprocal に指定する値。
    auto_write: auto_write に指定する値。

### `add_pair(self, atom_index1: int, atom_index2: int, constraint_type: int, *, auto_write: Optional[bool]=None)`

pair を追加する。

Args:
    atom_index1: atom_index1 に指定する値。
    atom_index2: atom_index2 に指定する値。
    constraint_type: constraint_type に指定する値。
    auto_write: auto_write に指定する値。

### `add_pairs(self, pairs: Iterable[Tuple[int, int, int]], *, auto_write: Optional[bool]=None)`

pairs を追加する。

Args:
    pairs: pairs に指定する値。
    auto_write: auto_write に指定する値。

### `remove_pair(self, atom_index1: int, atom_index2: int, *, reciprocal: bool=True, auto_write: Optional[bool]=None)`

pair を削除する。

Args:
    atom_index1: atom_index1 に指定する値。
    atom_index2: atom_index2 に指定する値。
    reciprocal: reciprocal に指定する値。
    auto_write: auto_write に指定する値。

### `clear_atom_neighbours(self, atom_index: int, *, reciprocal: bool=True, auto_write: Optional[bool]=None)`

atom neighbours を消去する。

Args:
    atom_index: atom_index に指定する値。
    reciprocal: reciprocal に指定する値。
    auto_write: auto_write に指定する値。

### `add_template_instance(self, local_pairs: Iterable[Tuple[int, int, int]], local_to_rmc: Mapping[int, int], *, auto_write: Optional[bool]=None)`

Expand one local molecular template to final RMC atom indices.

### `add_template_instances(self, local_pairs: Iterable[Tuple[int, int, int]], instances: Iterable[Mapping[int, int]], *, auto_write: Optional[bool]=None)`

template instances を追加する。

Args:
    local_pairs: local_pairs に指定する値。
    instances: instances に指定する値。
    auto_write: auto_write に指定する値。

### `add_group_complete_graph(self, atom_indices: Sequence[int], constraint_type: int, *, auto_write: Optional[bool]=None)`

Constrain every pair within an explicitly supplied atom group.

### `validate(self, *, require_reciprocal: bool=True)`

現在の設定内容を検証する。

Args:
    require_reciprocal: require_reciprocal に指定する値。

### `as_pairs(self, *, unique: bool=True)`

as pairs を実行する。

Args:
    unique: unique に指定する値。

Returns:
    処理結果。

## `main()`

SiO2 の小さな例を用いて ``sample.fnc`` を生成する。

実運用では、``atom_count`` と RMC 原子 index の組を対象構造に合わせて
置き換える。ここでは 1--2 と 1--3 を同じ距離制約タイプで相互登録する。


## 実装に基づく API 一覧

この一覧は提供された `rmc_pot_dat_fnc(10).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `FncNeighbour` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### `RmcPotDatFnc` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 39 | インスタンスを初期化する。 |
| `path()` | 84 | 現在の入出力パスを返す。 |
| `initialize()` | 92 | 内部状態を初期化する。 |
| `load()` | 116 | 既存ファイルを読み込む。 |
| `write()` | 186 | 現在の内部状態をファイルへ書き出す。 |
| `set_title()` | 228 | title を設定する。 |
| `get_title()` | 238 | title を取得する。 |
| `get_atom_count()` | 246 | atom count を取得する。 |
| `set_distance_range()` | 254 | distance range を設定する。 |
| `set_distance_ranges()` | 282 | distance ranges を設定する。 |
| `get_distance_ranges()` | 309 | distance ranges を取得する。 |
| `set_atom_neighbours()` | 317 | atom neighbours を設定する。 |
| `get_atom_neighbours()` | 341 | atom neighbours を取得する。 |
| `add_neighbour()` | 353 | neighbour を追加する。 |
| `add_pair()` | 381 | pair を追加する。 |
| `add_pairs()` | 405 | pairs を追加する。 |
| `remove_pair()` | 421 | pair を削除する。 |
| `clear_atom_neighbours()` | 444 | atom neighbours を消去する。 |
| `add_template_instance()` | 469 | Expand one local molecular template to final RMC atom indices. |
| `add_template_instances()` | 488 | template instances を追加する。 |
| `add_group_complete_graph()` | 507 | Constrain every pair within an explicitly supplied atom group. |
| `validate()` | 521 | 現在の設定内容を検証する。 |
| `as_pairs()` | 550 | as pairs を実行する。 |

### モジュール関数 `main()`

- 定義位置：644 行
- 説明：SiO2 の小さな例を用いて ``sample.fnc`` を生成する。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `RmcPotDatFnc.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `atom_count` | `Optional[int]` |
| `auto_write` | `bool` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:39`。

### `RmcPotDatFnc.path`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Path`。定義位置: `rmc_pot_dat_fnc(10).py:84`。

### `RmcPotDatFnc.initialize`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_count` | `int` |
| `title` | `Optional[str]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:92`。

### `RmcPotDatFnc.load`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:116`。

### `RmcPotDatFnc.write`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `out_name` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:186`。

### `RmcPotDatFnc.set_title`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `title` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:228`。

### `RmcPotDatFnc.get_title`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_dat_fnc(10).py:238`。

### `RmcPotDatFnc.get_atom_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fnc(10).py:246`。

### `RmcPotDatFnc.set_distance_range`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `constraint_type` | `int` |
| `rmin` | `float` |
| `rmax` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:254`。

### `RmcPotDatFnc.set_distance_ranges`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `ranges` | `Union[Mapping[int, Tuple[float, float]], Sequence[Tuple[float, float]]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:282`。

### `RmcPotDatFnc.get_distance_ranges`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Dict[int, Tuple[float, float]]`。定義位置: `rmc_pot_dat_fnc(10).py:309`。

### `RmcPotDatFnc.set_atom_neighbours`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_index` | `int` |
| `neighbours` | `Iterable[Union[FncNeighbour, Tuple[int, int]]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:317`。

### `RmcPotDatFnc.get_atom_neighbours`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_index` | `int` |

戻り値の型注釈: `List[FncNeighbour]`。定義位置: `rmc_pot_dat_fnc(10).py:341`。

### `RmcPotDatFnc.add_neighbour`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_index` | `int` |
| `neighbour_index` | `int` |
| `constraint_type` | `int` |
| `reciprocal` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:353`。

### `RmcPotDatFnc.add_pair`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_index1` | `int` |
| `atom_index2` | `int` |
| `constraint_type` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:381`。

### `RmcPotDatFnc.add_pairs`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `pairs` | `Iterable[Tuple[int, int, int]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:405`。

### `RmcPotDatFnc.remove_pair`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_index1` | `int` |
| `atom_index2` | `int` |
| `reciprocal` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:421`。

### `RmcPotDatFnc.clear_atom_neighbours`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_index` | `int` |
| `reciprocal` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:444`。

### `RmcPotDatFnc.add_template_instance`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `local_pairs` | `Iterable[Tuple[int, int, int]]` |
| `local_to_rmc` | `Mapping[int, int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:469`。

### `RmcPotDatFnc.add_template_instances`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `local_pairs` | `Iterable[Tuple[int, int, int]]` |
| `instances` | `Iterable[Mapping[int, int]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:488`。

### `RmcPotDatFnc.add_group_complete_graph`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_indices` | `Sequence[int]` |
| `constraint_type` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:507`。

### `RmcPotDatFnc.validate`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `require_reciprocal` | `bool` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:521`。

### `RmcPotDatFnc.as_pairs`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `unique` | `bool` |

戻り値の型注釈: `List[Tuple[int, int, int]]`。定義位置: `rmc_pot_dat_fnc(10).py:550`。

### `main`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fnc(10).py:644`。

