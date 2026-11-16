# `rmc_util.rmc_pot_hst`

ソース: `src/rmc_util/rmc_pot_hst.py`

## クラス `RmcPotHst`

ソースにクラス説明の docstring はありません。

### `__init__(self, hst_name: Optional[str]=None, cfg_name: Optional[str]=None, config: Optional[Config]=None, logger: Optional[XLogger]=None)`

RmcPotHst を初期化し、.hst ファイルの読み込みとパースを行う。

hst_name、cfg_name、config のいずれかを指定することで
対象となる .hst ファイルが決定される。
hst_name が指定されている場合はそれが最優先される。

1) cfg_name があればそれが優先
   hst_nameと書いている場合がある
   基本的には hst_name.hst ファイルを読む
   内部的には cfg_name として扱う
2) config があればそれが優先

Args:
    hst_name (Optional[str]): 読み込む .hst ファイル名。
    cfg_name (Optional[str]): CFG 名。指定された場合は「{cfg_name}.hst」を対象とする。
    config (Optional[Config]): Config オブジェクト。内部から cfg_name を参照する。
    logger (Optional[XLogger]): 使用するロガー。

### `read_chi2(self)`

chi2_tot の履歴を取得するための互換 API。

旧 RmcPotHst クラスとの互換性を保つため、
ステップ番号は行番号（0 始まり）として扱う。

（互換 API）
旧 RmcPotHst は：
    steps = [0, 1, 2, ...]
    chi2_list = [chi2_tot_of_loop0, chi2_tot_of_loop1, ...]
の形式で返していたため、それを再現する。

※ hst には "step" が存在しないため、
  行番号＝ステップ番号として扱う。

Returns:
    Tuple[List[int], List[float]]:
        ステップ番号のリストと chi2_tot のリスト。

### `detect_convergence(self, rel_tol: float=0.01, acc_tol: float=0.001, min_consecutive: int=3)`

RMC の履歴データに基づいて「実質的な収束点」を判定する。

本関数は、chi2_tot の絶対値ではなく、
連続ループ間での「相対的な改善率」と
探索の活動度（accepted/tried）を用いて収束を定義する。

判定の考え方は以下の通り：

1. 各ループ i について、直前ループとの差分から
   相対改善率 delta を計算する。

       delta = (chi2[i-1] - chi2[i]) / chi2[i-1]

2. 次の 2 条件を同時に満たす場合、
   そのループは「改善がほぼ止まっている」とみなす。

   (a) 相対改善率が十分小さい
       delta < rel_tol

   (b) 試行の受理率が十分小さい
       accepted/tried < acc_tol

   これは、
   「chi2 はほとんど下がらず、かつ探索も動いていない」
   状態を意味する。

3. 上記の「停滞状態」が min_consecutive 回
   連続して観測された場合にのみ、
   偶然ではない実質的な収束と判断する。

4. 戻り値として返す loop index は、
   「収束状態に最初に入ったループ番号」であり、
   最終ループ番号ではない点に注意する。

Args:
    rel_tol (float):
        連続ループ間の相対変化率
        chi2 の相対改善率に対する閾値。
        これ未満の改善は「停滞」とみなす。
    acc_tol (float):
        accepted/tried に対する閾値。
        これ未満は「探索がほぼ停止」とみなす。
    min_consecutive (int):
        停滞状態が連続して必要な最小ループ数。

Returns:
    Optional[int]:
        収束と判断された最初の loop index。
        判定条件を満たさない場合は None。

### `detect_convergence_set1(self, rel_tol: float=0.01, acc_tol: float=0.001, min_consecutive: int=2)`

F(Q) set#1 の chi2 を用いて RMC の実質的収束点を判定する。

chi2_tot ではなく、hst 中の
「chi2/F(Q)_set#1」を評価量として用いる点のみが
detect_convergence() との違いである。

Returns:
    Optional[int]:
        収束と判断された最初の loop index。
        判定できない場合は None。

### `get_num_rmc_loops(self)`

.hst に含まれる履歴レコード数を返す。

Returns:
    int: RMC ループ回数。

### `get_generated(self, loop_index: Optional[int]=None)`

指定したループに対応する値、または全ループ分の値を取得する。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

generated（このループで生成した移動数）を返す。
loop_index=None → 全ループ list
loop_index=int → 当該ループの値

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[int, float, List[int], List[float]]:
        対応する値。

### `get_tried(self, loop_index: Optional[int]=None)`

指定したループに対応する tried の値、または全ループ分の値を取得する。

tried は、そのループにおいて試行された移動回数を表す。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[int, List[int]]:
        tried の値。

### `get_accepted(self, loop_index: Optional[int]=None)`

指定したループに対応する accepted の値、または全ループ分の値を取得する。

accepted は、そのループにおいて受理された移動回数を表す。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[int, List[int]]:
        accepted の値。

### `get_time(self, loop_index: Optional[int]=None)`

指定したループに対応する time の値、または全ループ分の値を取得する。

time は、そのループに対応する経過時間（hst 出力に記録された値）を表す。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[int, List[int]]:
        time の値。

### `get_tried_per_generated(self, loop_index: Optional[int]=None)`

指定したループに対応する tried_per_gen の値、または全ループ分の値を取得する。

tried_per_gen は、generated に対する tried の比率を表す。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[float, List[float]]:
        tried_per_gen の値。

### `get_accepted_per_tried(self, loop_index: Optional[int]=None)`

指定したループに対応する acc_per_tried の値、または全ループ分の値を取得する。

acc_per_tried は、tried に対する accepted の比率を表す。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[float, List[float]]:
        acc_per_tried の値。

### `get_chi2_tot(self, loop_index: Optional[int]=None)`

全データーセットをまとめた chi
chi2_tota/data_point

Args:
    loop_index:

Returns:

### `get_chi2_set1(self, loop_index: Optional[int]=None)`

指定したループに対応する chi2_set1 の値、または全ループ分の値を取得する。

chi2_set1 は、hst 出力における
「chi2/F(Q)_set#1」に対応する chi2 値であり、
第 1 データセット（set#1）の評価量を表す。

loop_index を指定しない場合は全ループ分のリストを返し、
指定した場合は対応する単一の値を返す。

Args:
    loop_index (Optional[int]):
        取得対象のループ番号。

Returns:
    Union[float, List[float]]:
        chi2_set1 の値。


## 実装に基づく API 一覧


### `RmcPotHst` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 41 | RmcPotHst を初期化し、.hst ファイルの読み込みとパースを行う。 |
| `read_chi2()` | 202 | chi2_tot の履歴を取得するための互換 API。 |
| `detect_convergence()` | 231 | RMC の履歴データに基づいて「実質的な収束点」を判定する。 |
| `detect_convergence_set1()` | 327 | F(Q) set#1 の chi2 を用いて RMC の実質的収束点を判定する。 |
| `get_num_rmc_loops()` | 368 | .hst に含まれる履歴レコード数を返す。 |
| `get_generated()` | 382 | 指定したループに対応する値、または全ループ分の値を取得する。 |
| `get_tried()` | 413 | 指定したループに対応する tried の値、または全ループ分の値を取得する。 |
| `get_accepted()` | 441 | 指定したループに対応する accepted の値、または全ループ分の値を取得する。 |
| `get_time()` | 469 | 指定したループに対応する time の値、または全ループ分の値を取得する。 |
| `get_tried_per_generated()` | 497 | 指定したループに対応する tried_per_gen の値、または全ループ分の値を取得する。 |
| `get_accepted_per_tried()` | 525 | 指定したループに対応する acc_per_tried の値、または全ループ分の値を取得する。 |
| `get_chi2_tot()` | 553 | 全データーセットをまとめた chi |
| `get_chi2_set1()` | 575 | 指定したループに対応する chi2_set1 の値、または全ループ分の値を取得する。 |

## ソースコードに基づく引数・戻り値一覧


### `RmcPotHst.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `hst_name` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_hst(6).py:41`。

### `RmcPotHst.read_chi2`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[List[int], List[float]]`。定義位置: `rmc_pot_hst(6).py:202`。

### `RmcPotHst.detect_convergence`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `rel_tol` | `float` |
| `acc_tol` | `float` |
| `min_consecutive` | `int` |

戻り値の型注釈: `Optional[int]`。定義位置: `rmc_pot_hst(6).py:231`。

### `RmcPotHst.detect_convergence_set1`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `rel_tol` | `float` |
| `acc_tol` | `float` |
| `min_consecutive` | `int` |

戻り値の型注釈: `Optional[int]`。定義位置: `rmc_pot_hst(6).py:327`。

### `RmcPotHst.get_num_rmc_loops`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_hst(6).py:368`。

### `RmcPotHst.get_generated`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[int, List[int]]`。定義位置: `rmc_pot_hst(6).py:382`。

### `RmcPotHst.get_tried`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[int, List[int]]`。定義位置: `rmc_pot_hst(6).py:413`。

### `RmcPotHst.get_accepted`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[int, List[int]]`。定義位置: `rmc_pot_hst(6).py:441`。

### `RmcPotHst.get_time`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[int, List[int]]`。定義位置: `rmc_pot_hst(6).py:469`。

### `RmcPotHst.get_tried_per_generated`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[float, List[float]]`。定義位置: `rmc_pot_hst(6).py:497`。

### `RmcPotHst.get_accepted_per_tried`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[float, List[float]]`。定義位置: `rmc_pot_hst(6).py:525`。

### `RmcPotHst.get_chi2_tot`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[float, List[float]]`。定義位置: `rmc_pot_hst(6).py:553`。

### `RmcPotHst.get_chi2_set1`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `loop_index` | `Optional[int]` |

戻り値の型注釈: `Union[float, List[float]]`。定義位置: `rmc_pot_hst(6).py:575`。

