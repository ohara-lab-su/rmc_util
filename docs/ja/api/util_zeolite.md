# `rmc_util.util.zeolite`

ソース: `src/rmc_util/util/zeolite.py`

## クラス `ZeoliteCutoffs`

ゼオライト骨格の結合判定距離 [Å]。

Notes:
    デフォルト値は現在の RMC 設定に合わせている。
    これは「実在ゼオライトの許容結合長範囲」を定義するものではなく、
    どの原子を bonded neighbour とみなすかの解析 cutoff である。

### `range_for_t(self, symbol: str)`

T 原子種に対応する T-O cutoff を返す。

## クラス `ZeoliteRmcConfig`

RMC 設定から取得したゼオライト解析用パラメータ。

``source`` は値を取得した ``*.dat`` または ``rmc_init*.py`` を示す。
``element_info`` は RMC type の順序で、1-origin の type 番号を元素へ
対応付けるために使用する。

``ZeoliteCutoffs`` に変換するときは、COORD に指定された
Si->O / Al->O の neighbour range をそのまま解析 bond range として使う。

## `load_zeolite_rmc_config_from_dat(path: str | Path)`

RMC_POT free-format ``*.dat`` から解析用パラメータを取得する。

取得対象:
    - ``[ GENERAL ] / CHEMICAL-SYMBOLS``
    - ``[ COORD ] / CENT-TYPE``
    - ``[ COORD ] / NEIGH-TYPE_FROM_TO``

Si->O および Al->O の COORD neighbour range をゼオライト解析の
T-O bond range として使用する。

Raises:
    ValueError: 必要な element 情報または COORD range が取得できない場合。

## `load_zeolite_rmc_config_from_init(path: str | Path)`

``rmc_init*.py`` の有効な RmcPotDat 設定から解析条件を取得する。

Python ファイルは実行しない。AST で、
``set_element_info()`` と ``set_coord_constraint()`` の
コメントアウトされていない呼び出しだけを読む。

これにより rmc_init 自体に副作用があっても解析時には実行されない。

## `rmc_config_to_cutoffs(config: ZeoliteRmcConfig)`

RMC 設定を ``ZeoliteCutoffs`` に変換する。

## `find_rmc_parameter_source(directory: str | Path='.')`

解析ディレクトリから RMC parameter source を自動探索する。

優先順位:
    1. ``*.dat``
    2. ``rmc_init.py``
    3. ``rmc_init*.py``

``*.dat`` が複数ある場合は basename が ``aaa.dat`` のものを優先し、
それ以外は名前順の最初を返す。

## `load_zeolite_rmc_config(source: str | Path)`

``*.dat`` または ``rmc_init*.py`` を拡張子から自動判定して読む。

## クラス `ZeoliteCriteria`

RMC 構造を zeolite-like と判定するための明示的閾値。

Notes:
    これらは IZA の正式な定義値ではない。
    RMC 途中構造を「ゼオライト型構造空間から逸脱していないか」
    スクリーニングするための実務的閾値である。

    binary 判定だけでなく、必ず各連続量も確認すること。

## クラス `PeriodicEdge`

周期グラフの無向 edge。

shift は node_u のセルから見た node_v の周期像を表す整数格子ベクトル。

## `validate_framework_elements(structure: Structure)`

Si/Al/O を含む構造であることを確認する。

Na や H などの非骨格元素が含まれていてもよい。

## `build_to_bonds(structure: Structure, cutoffs: ZeoliteCutoffs=ZeoliteCutoffs())`

T=(Si,Al)-O bond を cutoff から作る。

Returns:
    T 原子を node_u、O を node_v とする PeriodicEdge の一覧。

## `coordination_distributions(structure: Structure, edges: Sequence[PeriodicEdge])`

Si/Al の O 配位数と O の T 配位数分布を計算する。

## `bond_length_statistics(structure: Structure, edges: Sequence[PeriodicEdge])`

Si-O / Al-O bond length の統計を返す。

## `angle_statistics(structure: Structure, edges: Sequence[PeriodicEdge])`

O-T-O と T-O-T の角度分布を計算する。

## `periodic_network_statistics(structure: Structure, edges: Sequence[PeriodicEdge])`

T-O framework の連結成分と周期次元を求める。

周期次元は periodic graph の spanning tree を作り、
non-tree edge が生成する格子並進ベクトルの rank から求める。

rank=3 なら、骨格は a,b,c の独立3方向へ周期的に連結している。

## `build_tt_graph(structure: Structure, edges: Sequence[PeriodicEdge])`

bridging O を edge とみなした T-T quotient graph を作る。

Notes:
    O が2個以上の T に結合している場合、その全組合せを T-T edge にする。
    ring 解析は原子番号だけからなる有限周期セルの quotient graph 上で行う。
    IZA の strict primitive-ring / vertex-symbol 解析とは異なる。

## `shortest_ring_statistics(structure: Structure, edges: Sequence[PeriodicEdge], max_ring_size: int=16)`

T-T network の shortest-ring 統計を近似的に求める。

各 T-T edge を一度除去し、その両端を結ぶ最短経路を探索する。
edge + shortest path を一つの shortest ring とみなす。

同じ原子集合を持つ ring は一つにまとめる。

## `loewenstein_statistics(structure: Structure, edges: Sequence[PeriodicEdge])`

bridging O の T-T 組から Al-O-Al の割合を求める。

## `framework_density(structure: Structure)`

framework density [T atoms / 1000 Å^3] を返す。

## `evaluate_zeolite_like(coordination: Mapping[str, object], network: Mapping[str, object], criteria: ZeoliteCriteria=ZeoliteCriteria())`

連続指標から zeolite-like screening 判定を行う。

## `analyze_zeolite(structure: Structure, *, cutoffs: ZeoliteCutoffs=ZeoliteCutoffs(), criteria: ZeoliteCriteria=ZeoliteCriteria(), max_ring_size: int=16, calculate_rings: bool=True)`

ゼオライト型フレームワークを一括解析する。

Args:
    structure: pymatgen ``Structure``。
    cutoffs: Si-O / Al-O bond 判定距離。
    criteria: zeolite-like screening の閾値。
    max_ring_size: shortest-ring 探索の最大員環。
    calculate_rings: False なら ring 解析を省略する。

Returns:
    解析結果をまとめた辞書。


## 実装に基づく API 一覧

この一覧は提供された `zeolite(2).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `ZeoliteCutoffs` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `range_for_t()` | 60 | T 原子種に対応する T-O cutoff を返す。 |

### `ZeoliteRmcConfig` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### モジュール関数 `load_zeolite_rmc_config_from_dat()`

- 定義位置：137 行
- 説明：RMC_POT free-format ``*.dat`` から解析用パラメータを取得する。

### モジュール関数 `load_zeolite_rmc_config_from_init()`

- 定義位置：259 行
- 説明：``rmc_init*.py`` の有効な RmcPotDat 設定から解析条件を取得する。

### モジュール関数 `rmc_config_to_cutoffs()`

- 定義位置：330 行
- 説明：RMC 設定を ``ZeoliteCutoffs`` に変換する。

### モジュール関数 `find_rmc_parameter_source()`

- 定義位置：343 行
- 説明：解析ディレクトリから RMC parameter source を自動探索する。

### モジュール関数 `load_zeolite_rmc_config()`

- 定義位置：376 行
- 説明：``*.dat`` または ``rmc_init*.py`` を拡張子から自動判定して読む。

### `ZeoliteCriteria` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### `PeriodicEdge` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### モジュール関数 `validate_framework_elements()`

- 定義位置：452 行
- 説明：Si/Al/O を含む構造であることを確認する。

### モジュール関数 `build_to_bonds()`

- 定義位置：482 行
- 説明：T=(Si,Al)-O bond を cutoff から作る。

### モジュール関数 `coordination_distributions()`

- 定義位置：542 行
- 説明：Si/Al の O 配位数と O の T 配位数分布を計算する。

### モジュール関数 `bond_length_statistics()`

- 定義位置：652 行
- 説明：Si-O / Al-O bond length の統計を返す。

### モジュール関数 `angle_statistics()`

- 定義位置：679 行
- 説明：O-T-O と T-O-T の角度分布を計算する。

### モジュール関数 `periodic_network_statistics()`

- 定義位置：753 行
- 説明：T-O framework の連結成分と周期次元を求める。

### モジュール関数 `build_tt_graph()`

- 定義位置：834 行
- 説明：bridging O を edge とみなした T-T quotient graph を作る。

### モジュール関数 `shortest_ring_statistics()`

- 定義位置：901 行
- 説明：T-T network の shortest-ring 統計を近似的に求める。

### モジュール関数 `loewenstein_statistics()`

- 定義位置：955 行
- 説明：bridging O の T-T 組から Al-O-Al の割合を求める。

### モジュール関数 `framework_density()`

- 定義位置：992 行
- 説明：framework density [T atoms / 1000 Å^3] を返す。

### モジュール関数 `evaluate_zeolite_like()`

- 定義位置：998 行
- 説明：連続指標から zeolite-like screening 判定を行う。

### モジュール関数 `analyze_zeolite()`

- 定義位置：1031 行
- 説明：ゼオライト型フレームワークを一括解析する。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `ZeoliteCutoffs.range_for_t`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `symbol` | `str` |

戻り値の型注釈: `BondRange`。定義位置: `zeolite(2).py:60`。

### `load_zeolite_rmc_config_from_dat`

| 引数 | 型注釈 |
|---|---|
| `path` | `str \| Path` |

戻り値の型注釈: `ZeoliteRmcConfig`。定義位置: `zeolite(2).py:137`。

### `load_zeolite_rmc_config_from_init`

| 引数 | 型注釈 |
|---|---|
| `path` | `str \| Path` |

戻り値の型注釈: `ZeoliteRmcConfig`。定義位置: `zeolite(2).py:259`。

### `rmc_config_to_cutoffs`

| 引数 | 型注釈 |
|---|---|
| `config` | `ZeoliteRmcConfig` |

戻り値の型注釈: `ZeoliteCutoffs`。定義位置: `zeolite(2).py:330`。

### `find_rmc_parameter_source`

| 引数 | 型注釈 |
|---|---|
| `directory` | `str \| Path` |

戻り値の型注釈: `Optional[Path]`。定義位置: `zeolite(2).py:343`。

### `load_zeolite_rmc_config`

| 引数 | 型注釈 |
|---|---|
| `source` | `str \| Path` |

戻り値の型注釈: `ZeoliteRmcConfig`。定義位置: `zeolite(2).py:376`。

### `validate_framework_elements`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |

戻り値の型注釈: `None`。定義位置: `zeolite(2).py:452`。

### `build_to_bonds`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `cutoffs` | `ZeoliteCutoffs` |

戻り値の型注釈: `List[PeriodicEdge]`。定義位置: `zeolite(2).py:482`。

### `coordination_distributions`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:542`。

### `bond_length_statistics`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:652`。

### `angle_statistics`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:679`。

### `periodic_network_statistics`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:753`。

### `build_tt_graph`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |

戻り値の型注釈: `Dict[int, Set[int]]`。定義位置: `zeolite(2).py:834`。

### `shortest_ring_statistics`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |
| `max_ring_size` | `int` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:901`。

### `loewenstein_statistics`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `edges` | `Sequence[PeriodicEdge]` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:955`。

### `framework_density`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |

戻り値の型注釈: `float`。定義位置: `zeolite(2).py:992`。

### `evaluate_zeolite_like`

| 引数 | 型注釈 |
|---|---|
| `coordination` | `Mapping[str, object]` |
| `network` | `Mapping[str, object]` |
| `criteria` | `ZeoliteCriteria` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:998`。

### `analyze_zeolite`

| 引数 | 型注釈 |
|---|---|
| `structure` | `Structure` |
| `cutoffs` | `ZeoliteCutoffs` |
| `criteria` | `ZeoliteCriteria` |
| `max_ring_size` | `int` |
| `calculate_rings` | `bool` |

戻り値の型注釈: `Dict[str, object]`。定義位置: `zeolite(2).py:1031`。

