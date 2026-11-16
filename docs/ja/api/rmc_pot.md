# `rmc_util.rmc_pot`

ソース: `src/rmc_util/rmc_pot.py`

## クラス `RmcPot`

Utility class for managing and running local RMC commands.
And parsing configuration files.

### `__init__(self, *, rmc_log: Optional[RmcPotLog]=None, rmc_dat: Optional[RmcPotDat]=None, config: Optional[Config]=None, cfg_name: Optional[str]=None, use_free_format: bool=False, logger: Optional[XLogger]=None)`

config インスタンスを与えると、cfg_name はいらない

Args:
    rmc_log: RMC_POT のログ処理用のインスタンス
    rmc_dat: RMC_POT のDAT処理用のインスタンス
    config (Config): 全てのインスタンスが同じ Config()
    logger (XLogger): 全てインスタンスが同じ XLogger()
    cfg_name (str): cfg-filename

### `rmc_dat(self)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `set_cfg_name(self, cfg_name: str)`

このメソッドには docstring がありません。動作の詳細は実装を参照してください。

### `set_tag(self, tag_name: str, *args)`

RmcPotData 側の set_xxx メソッドを呼び出す互換I/F。

Args:
    tag_name (str): タグ名（例: 'cutoffs', 'potential'）
    *args: set_xxx に渡す引数

### `get_tag(self, tag_name: str, *args)`

RmcPotData 側の get_xxx メソッドを呼び出す互換I/F。

Args:
    tag_name (str): タグ名（例: 'cutoffs', 'potential'）
    *args: get_xxx に渡す引数（必要な場合）

Returns:
    Any: 対応する get_xxx の戻り値

### `init(self, cfg_name: str)`

RMC-DFT は RMC から始める。しかし構造ファイルは VASP ベースから
スタートするので、rmc_pot 側での初期化はこのルーチンでは明示的にしない
互換のフェイクI/F

Args:
    cfg_name:

Returns:

### `preprocess(self)`

 RMC_POT の実行前に必要な入力ファイルを検査する。

このコードを動かすときは RMC_POT 入力が揃っている前提とする
 1. 実験プロファイル（例: fesi04_smbt-rmc.txt）が実行カレントに存在しないときは止める
 2. label.txt が存在しないと止める

 *) 初期の構造変換は誤解が起きやすいので RmcPot クラスでは Preprocess() で勝手にやらないようにする


 Returns:
     bool:
         必要な入力ファイルがすべて存在し、実験データファイル名を
         正常に取得できた場合は ``True``。
         入力不足または設定不正の場合は ``False``。

### `postprocess(self, log_dir: Optional[str]=None, cfg_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None)`

後処理

RMC 後に DFT を動かすにあたっての
1) DATA-collect
2) BACKUP
3) xxx.CFG --> POSCAR (VASP4) 変換(xxx.vasp) --> VASP5 変換(xxx.vasp)

他のコードを使っても基本は poscar 経由を念頭におくので
postprocess は poscar にしておけば他のライブラリを使っても
齟齬は出ない

Args:
    log_dir (str): RMC用の log_dir
    cfg_name (str): cfg_name と vasp_name は等しいとする(デフォルトはコンストラの引数での cfg_name)
    element_info (str | list): 元素情報

Returns:
    bool:

### `check_fnc_cutoff_consistency(self, cfg_name: Optional[str]=None)`

RMC_POT 実行前に、*.fnc の rmin と *.dat の hard-sphere cutoff の
整合性を確認する。

FNC の constraint type 番号と原子種ペアを固定対応させず、
*.fnc に記録された実際の原子 index ペアと *.cfg の原子種別ブロックから
対応する RMC 原子タイプを決定する。

### `run(self, cfg_name: Optional[str]=None, blocking: Optional[bool]=True, save_stdout: Optional[bool]=True)`

RMC を実行する

Args:
    cfg_name (str):
    blocking (bool)_:  subprocessをブロッキングで起動(default: True)
    save_stdout (bool): True ならログをファイルに保存

Returns:
    bool: 正しく終わったデー

### `ensure_vasp5_format(poscar_name: str, element_info: Optional[str]=None, logger: XLogger=XLogger())`

RMC_POT には元素種の情報がなくて、VASP4 の POSCAR 相当のものしか
変換では作ることができない。そのために、VASP4 形式の POSCASR に
元素種の情報を付加する。そのための method (utility)

Args:
    poscar_name:
    element_info:
    logger:

Returns:

### `cfg2poscar(self, cfg_name: Optional[str]=None, vasp_name: Optional[str]=None, element_info: Optional[Union[str, Sequence[str]]]=None)`

CFG から POSCAR 変換

CFG からそのまま作るので、そのままだと元素種の情報がないので
VASP4 形式の POSCAR となる。

Args:
    cfg_name (str):  xxx.cfg（拡張子なしのベース名を想定）
    vasp_name (str): xxx.vasp（拡張子なしのベース名を想定）
    element_info (str or Sequence[str]): ["Fe","Si",,,]


## 実装に基づく API 一覧

この一覧は提供された `rmc_pot(20261116-081310).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `RmcPot` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 34 | config インスタンスを与えると、cfg_name はいらない |
| `rmc_dat()` | 114 | ソース内に説明なし |
| `set_cfg_name()` | 117 | ソース内に説明なし |
| `set_tag()` | 132 | RmcPotData 側の set_xxx メソッドを呼び出す互換I/F。 |
| `get_tag()` | 148 | RmcPotData 側の get_xxx メソッドを呼び出す互換I/F。 |
| `init()` | 167 | RMC-DFT は RMC から始める。しかし構造ファイルは VASP ベースから |
| `preprocess()` | 181 | RMC_POT の実行前に必要な入力ファイルを検査する。 |
| `postprocess()` | 261 | 後処理 |
| `check_fnc_cutoff_consistency()` | 342 | RMC_POT 実行前に、*.fnc の rmin と *.dat の hard-sphere cutoff の |
| `run()` | 729 | RMC を実行する |
| `ensure_vasp5_format()` | 839 | RMC_POT には元素種の情報がなくて、VASP4 の POSCAR 相当のものしか |
| `cfg2poscar()` | 863 | CFG から POSCAR 変換 |

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `RmcPot.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `rmc_log` | `Optional[RmcPotLog]` |
| `rmc_dat` | `Optional[RmcPotDat]` |
| `config` | `Optional[Config]` |
| `cfg_name` | `Optional[str]` |
| `use_free_format` | `bool` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot(20261116-081310).py:34`。

### `RmcPot.rmc_dat`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot(20261116-081310).py:114`。

### `RmcPot.set_cfg_name`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot(20261116-081310).py:117`。

### `RmcPot.set_tag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `tag_name` | `str` |
| `args` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `rmc_pot(20261116-081310).py:132`。

### `RmcPot.get_tag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `tag_name` | `str` |
| `args` | `指定なし` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot(20261116-081310).py:148`。

### `RmcPot.init`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `指定なし`。定義位置: `rmc_pot(20261116-081310).py:167`。

### `RmcPot.preprocess`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot(20261116-081310).py:181`。

### `RmcPot.postprocess`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `log_dir` | `Optional[str]` |
| `cfg_name` | `Optional[str]` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot(20261116-081310).py:261`。

### `RmcPot.check_fnc_cutoff_consistency`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `Optional[str]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot(20261116-081310).py:342`。

### `RmcPot.run`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `Optional[str]` |
| `blocking` | `Optional[bool]` |
| `save_stdout` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot(20261116-081310).py:729`。

### `RmcPot.ensure_vasp5_format`

| 引数 | 型注釈 |
|---|---|
| `poscar_name` | `str` |
| `element_info` | `Optional[str]` |
| `logger` | `XLogger` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot(20261116-081310).py:839`。

### `RmcPot.cfg2poscar`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `Optional[str]` |
| `vasp_name` | `Optional[str]` |
| `element_info` | `Optional[Union[str, Sequence[str]]]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot(20261116-081310).py:863`。

