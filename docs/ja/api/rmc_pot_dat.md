# `rmc_util.rmc_pot_dat`

ソース: `src/rmc_util/rmc_pot_dat.py`

## クラス `RmcPotDat`

固定形式と自由形式の RmcPotDat を統一して扱う透明なラッパークラス。

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, auto_write: bool=True, use_free_format: Optional[bool]=None)`

RmcPotDat ラッパーを生成する。

Args:
    config: Config インスタンス。
    logger: XLogger インスタンス。
    cfg_name: *.dat の拡張子を除いたファイル名。
    auto_write: 自動保存フラグ。
    use_free_format: 新規 *.dat 作成時に使う既定形式。
        True は自由形式、False は固定形式、None は自由形式を既定とする。

Notes:
    コンストラクタでは *.dat の読込み・生成を行わない。
    実際の初期化は init() で行う。

### `set_free_format(self, use_free_format: bool)`

新規 ``*.dat`` 作成時に使用する形式を設定する。

初期化前は保持中の形式指定を更新する。初期化後は現在の ``*.dat`` の
形式を変更せず、実際に使用している形式をログへ出力する。

### `set_cfg_name(self, cfg_name: str)`

読み書き対象の構成名を変更する。

初期化前はラッパーが保持する名前だけを変更する。初期化後は内部実装にも
同じ名前を反映する。

### `init(self, *, use_free_format: Optional[bool]=None, prefer_existing: bool=True)`

*.dat を読み込むか、各形式クラスの初期値から新規作成する。

Args:
    use_free_format: 新規作成時の形式。None の場合はコンストラクタまたは
        set_free_format() で保持した形式を使う。
    prefer_existing: 既存 *.dat がある場合に既存ファイルを優先する。
        False の場合は既存ファイルをバックアップし、指定形式の初期値で
        作り直す。

### `is_free_format(self)`

現在使用中の実体が自由形式かどうかを返す。

未初期化の場合は、既存 ``*.dat`` の読込みまたは初期ファイル生成を
遅延実行してから判定する。

## `main()`

自由形式 DAT を選択し、基本設定を書き込む利用例。

Notes:
    ``sample_dat.dat`` が存在しない場合は、自由形式のデフォルト DAT を
    作成する。SNC 関係の操作は従来どおり ``RmcPotDatFree`` に委譲される。


## 実装に基づく API 一覧

この一覧は提供された `rmc_pot_dat(20261116-081310).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `RmcPotDat` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 25 | RmcPotDat ラッパーを生成する。 |
| `set_free_format()` | 55 | 新規 \`\`*.dat\`\` 作成時に使用する形式を設定する。 |
| `set_cfg_name()` | 71 | 読み書き対象の構成名を変更する。 |
| `init()` | 82 | *.dat を読み込むか、各形式クラスの初期値から新規作成する。 |
| `is_free_format()` | 155 | 現在使用中の実体が自由形式かどうかを返す。 |

### モジュール関数 `main()`

- 定義位置：181 行
- 説明：自由形式 DAT を選択し、基本設定を書き込む利用例。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `RmcPotDat.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |
| `cfg_name` | `Optional[str]` |
| `auto_write` | `bool` |
| `use_free_format` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat(20261116-081310).py:25`。

### `RmcPotDat.set_free_format`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `use_free_format` | `bool` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat(20261116-081310).py:55`。

### `RmcPotDat.set_cfg_name`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat(20261116-081310).py:71`。

### `RmcPotDat.init`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `use_free_format` | `Optional[bool]` |
| `prefer_existing` | `bool` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat(20261116-081310).py:82`。

### `RmcPotDat.is_free_format`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat(20261116-081310).py:155`。

### `main`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat(20261116-081310).py:181`。

