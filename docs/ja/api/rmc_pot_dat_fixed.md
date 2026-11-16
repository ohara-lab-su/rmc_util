# `rmc_util.rmc_pot_dat_fixed`

ソース: `src/rmc_util/rmc_pot_dat_fixed.py`

## クラス `RmcPotDatFixed`

RMC_POT の .dat ファイルを行番号ベースで編集するためのクラス。

使い方:
    dat = RmcPotDat("/abs/path/to/aaa.dat", auto_write=True)
    rho = dat.get_density()
    dat.set_cutoffs((2.5, 2.2, 2.0))  # auto_write=True なら即時保存
    dat.write()  # 明示保存も可能

注意:
    - 行番号は 1 始まり。内部処理では 0 始まりのリストに対応付け
    - 既存コメントは保持します。コメント無しの行へ値を設定した場合はコメント無しで書き出し

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, auto_write: bool=True)`

config インスタンスを与えると、_cfg_name はいらない

Args:
    config (Config): 全てのインスタンが同じ Config()
    logger (XLogger): 全てインスタンスが同じ XLogger()
    cfg_name (str): xxxx.dat の絶対パス、基本名前（拡張子は付けない）
    auto_write (bool): True の場合 set_* / set_line で即時書き出し

### `set_cfg_name(self, cfg_name: str)`

読み書き対象の構成名を変更する。

Args:
    cfg_name: cfg_name に指定する値。

### `create_dat_file(self, basename: str)`

与えられたベース名から <basename>.dat を作成し、
デフォルトの RMC_POT 用 dat 内容を書き込む。

### `load(self)`

ファイルを読み込んで内部行リストを構築。

### `write(self, out_name: Optional[str]=None)`

現在の内容を書き出す (.dat は自動付加される)

Args:
    out_name (str): 出力先。未指定なら self._cfg_name に上書き保存。

### `get_line(self, line_no_1based: int)`

任意行の値部分を返す（コメントは含めない）
本来の RMC_POT を編集するための raw メソッド

Args:
    line_no_1based: 1 始まりの行番号

Returns:
    値（文字列）

### `set_line(self, line_no_1based: int, value: Union[str, int, float, Sequence[Union[int, float]], bool], *, auto_write: Optional[bool]=None)`

任意行の値部分を更新（コメントは保持）。

Args:
    line_no_1based (int): 1 始まりの行番号
    value: 置換値（数値/数値列/真偽/文字列）
    auto_write (bool): True 指定で即時保存。None の場合はインスタンス既定(self._auto_write)に従う。

Raises:
    IndexError: 行番号が範囲外
    ValueError: 真偽解釈など不正値

### `insert_line(self, line_no_1based: int, value: Union[str, int, float, Sequence[Union[int, float]], bool], *, comment: str='', auto_write: Optional[bool]=None)`

fixed format の指定物理行へ1行挿入する。

### `remove_line(self, line_no_1based: int, *, auto_write: Optional[bool]=None)`

fixed format の指定物理行を削除する。

### `set_element_info(self, element_info: Sequence[str], *, auto_write: Optional[bool]=None)`

固定形式には元素記号を保持する欄がないため設定できない。

自由形式と同じ起動スクリプトから呼ばれた場合に、黙って無視せず
固定形式では非対応であることを明示する互換メソッド。

### `get_comment(self)`

1 行目 comment を str で返す。

### `set_comment(self, comment: str, *, auto_write: Optional[bool]=True)`

1 行目 comment を更新。

### `get_density(self)`

2 行目 density を float で返す。

Notes:
    例)
    0.0842566414       ! number densit

    - 系の数密度（number density） 単位は原子数 / Å^3。
    - cfg ファイル中の原子数とシミュレーションボックス体積の
      関係で一致させる必要がある（二重定義）

### `set_density(self, rho: Union[int, float], *, auto_write: Optional[bool]=True)`

2 行目 density を更新。

### `get_cutoffs(self)`

3 行目 cut offs を (c1, c2, c3) で返す。

例)
1 1 1 1 1 1 ! cut offs

- 説明: 原子種ごとのカットオフ距離（またはカットオフの有無フラグ）を指定するフィールド。
- 実務上: 多くの実装では「最低許容距離（min separation）」や「ペアごとの距離カットオフ」を指定。
         型の数 (ntypes) に応じた個数を並べる必要がある
- 並びは3元型の場合、11,12,13,22,23,33となっている
- n元型の場合、11,12,13,14, ... , 1n, 22, 23,...,2n, 33, 34, ..., 3n, ..., nn となる

### `set_cutoffs(self, values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=True)`

3 行目 cut offs を更新。可変長対応。
それ以上原子同士が近づかない距離

Notes:
    Fe Si B の３つのときは 6つのパターンが生まれる

    Fe–Fe
    Fe–Si
    Fe–B
    Si–Si
    Si–B
    B–B

    6つが必要

    cutoff の与え方（固定フォーマット版 RMC_POT の厳密仕様）:

        cutoff は「原子種の組み合わせごと」に 1 つずつ値を並べる。
        原子種数を ntypes とすると、必要となる cutoff の数は

            ntypes * (ntypes + 1) / 2

        である。

        並べる順序は RMC_POT 固定フォーマットの既定順で、以下のように
        “11, 12, 13, …, 22, 23, …, 33, …” のような三角行列形式で並べる。

    例1:
        3 元系（Fe, Si, B）の場合（ntypes = 3）

        必要な cutoff は 6 個：
            11, 12, 13, 22, 23, 33

        set_cutoffs へ渡すリストは次のように 6 要素で指定する：

            set_cutoffs([c11, c12, c13, c22, c23, c33])

        実際の実行例：

            set_cutoffs([2.3, 2.1, 2.0, 2.3, 2.1, 2.0])

    例2:
        2 元系（A, B）の場合（ntypes = 2）

        必要な cutoff は 3 個：
            11, 12, 22

        set_cutoffs([c11, c12, c22])

    注意:
        - cutoff の個数は必ず ntypes*(ntypes+1)/2 と一致させること。
        - 固定フォーマット版 RMC_POT ではこの並びと個数が崩れると、
          直後の行（maximum moves 等）の読み込み位置がずれ、実行時エラーになる。
        - 可変長の free-format (#003) ではこの限りではないが、
          本クラスは固定フォーマット互換を前提としている。

Args:
    values (Sequence[Union[int|float]]):
        上記の定義に従い、原子種組み合わせごとの cutoff を並べたリスト。
        原子種ごとのカットオフ距離リストを指定する。
        要素数は ntypes に応じて可変（3 要素に限定しない）

    auto_write (bool | None):
        True の場合は即時書き出し。None はインスタンス既定値に従う。

### `get_max_moves(self)`

4 行目 maximum moves を (m1, m2) で返す。

Notes:
    例)
    0.01 0.01 0.01   ! maximum moves

    - 説明: 原子移動の最大振幅（1 回の move での最大変位）を指定します。複数値が並んでいる場合はタイプごと、
           または移動タイプごとの設定になっていることがある。単位は Å。
    - 備考: 値が小さいほど受理率が高くなるがサンプリング効率は落ちます
           調整して受理率を 20–50% 程度に保つのが一般的

### `set_maximum_moves(self, values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=True)`

4 行目 maximum moves を可変長で更新する。

Args:
    values (Sequence[Union[int, float]]):
        任意個数の maximum move 値。順序はそのまま書き込み。

    auto_write (bool | None):
        True の場合即時保存。None の場合はインスタンス既定に従う。

### `get_r_spacing(self)`

5 行目 r spacing を float で返す。i
近接分布関数 g(r) のビン幅（r の刻み幅）。単位は Å。
RMC の g(r) や部分 g(r) を計算する際、距離 r の空間を等間隔に区切ってヒストグラムを作成します。
この ビン間隔（dr） を指定するのが R-SPACING

Notes:
    例:
        0.025        ! r spacing

        - 備考: 小さいほど解像度は上がるが計算負荷が増える

### `set_r_spacing(self, dr: Union[int, float], *, auto_write: Optional[bool]=True)`

5 行目 r spacing を更新。

### `get_moveout_option(self)`

6 行目（whether to use moveout option）を取得する。

Notes:
    内容:
        - RMC 計算において「moveout オプション」を使用するかどうかを指定するブール値。
          moveout オプションは、原子のランダム移動試行時に追加的な処理を行う機能であり、
          一般的には「移動後の局所最適化」や「過大な変位の制限」を目的とする

    マニュアル定義:
        - ラベル: “whether to use moveout option”
        - 型: 論理値（.true. / .false.）
        - 意味:
            - .true.  : moveout 処理を有効化。
                        → 原子移動試行のたびに補助的な判定・制約が加わる。
            - .false. : moveout 処理を無効化。
                        → 通常の RMC 移動アルゴリズムを使用。
        - 挙動の詳細は実装依存（例: moveout モジュール内で距離閾値チェックを行うなど）。

    例:
        .true.   ! whether to use moveout option
            → moveout 処理を有効化（制約付き移動を実施）。
        .false.  ! whether to use moveout option
            → 通常のランダム移動。

Returns:
    bool: moveout オプションを有効化している場合は True、無効なら False。

### `set_moveout_option(self, use_moveout: bool, *, auto_write: Optional[bool]=True)`

6 行目（whether to use moveout option）を更新する。

Notes:
    内容:
        - moveout オプションを有効化するかどうかを設定する。
          moveout は RMC における原子移動の特殊処理オプションであり、
          一般には「移動後の拘束条件」「局所最適化ステップ」「排他領域判定」などを伴う。

    指定方法:
        - True  → .true. を書き込み、有効化。
        - False → .false. を書き込み、無効化。

    例:
        set_moveout_option(True)
            → moveout 処理を有効にする。
        set_moveout_option(False)
            → moveout 処理を無効にする。

Args:
    use_moveout (bool):
        moveout オプションを有効化する場合は True、無効化する場合は False。
    auto_write (bool | None):
        True なら即時保存、None の場合はインスタンス既定に従う。

### `get_num_config_to_collect(self)`

7 行目（number of configuration to collect）を取得する。

Notes:
    内容:
        - RMC 実行中に「構成（configuration）」をどの程度の頻度で収集するかを指定する。
          ここでいう configuration とは、特定ステップ時点の原子配置を指す。
          解析や平均化、統計処理に利用するため、指定回数ぶんを記録できる。

    マニュアル定義:
        - ラベル: “number of configuration to collect”
        - 単位: 個数（整数）
        - 意味:
            RMC 計算中に「収集用構成」を保存する数。
            この値が 0 の場合、多くの実装では「構成を収集しない」または
            「最終構成のみを保存」として扱われる。

    典型的な設定例:
        0     ! number of configuration to collect
            → 構成を収集せず、最終結果のみを出力。
        10    ! number of configuration to collect
            → 全実行中に 10 構成を等間隔で保存。
        100   ! number of configuration to collect
            → 100 構成を収集（より細かい統計解析に利用）。

    備考:
        - 保存間隔は RMC_POT 内部で自動的に均等分配される。
        - このパラメータは出力用ヒストグラムや g(r) 平均化などに影響を与える。

Returns:
    int: 収集する構成数。

### `set_num_config_to_collect(self, num_config: int, *, auto_write: Optional[bool]=True)`

7 行目（number of configuration to collect）を更新する。

Notes:
    内容:
        - RMC 実行中にどのくらいの頻度で「構成（configuration）」を保存するかを指定する。
          これは構造平均化や g(r) 平均などの統計解析に使う複数構成を得るための設定。

    指定方法:
        - 0 の場合:
            → 構成を収集しないか、最終構成のみを保存。
        - 正の整数値:
            → 指定数の構成を収集。
              RMC_POT はシミュレーション全体を等間隔に分割して収集ステップを決定する。

    例:
        set_num_config_to_collect(0)
            → 収集しない（最終構成のみ）。
        set_num_config_to_collect(20)
            → 全体で 20 構成を等間隔で保存。

Args:
    num_config (int):
        収集する構成数（0 以上の整数）
    auto_write (bool | None):
        True の場合は即時保存。None の場合はインスタンス既定に従う。

### `get_print_interval(self)`

8 行目（step for printing）を取得する。

Notes:
    内容:
        - RMC_POT の計算進行中、標準出力やログファイルに
          エネルギー・受理率・コスト関数などの経過情報を
          どの間隔で出力するかを指定するステップ数。

    マニュアル定義:
        - ラベル: “step for printing”
        - 意味: RMC の実行ループ中で何ステップごとに
                計算状況（χ²値、受理率、平均変位など）を表示するか。
        - 値の単位: ステップ数（整数）
        - 0 または負値: 無効（出力を行わない、もしくは既定間隔を使用）

    例:
        5000  ! step for printing
        → 5000 ステップごとに進行情報を出力。
        100   ! step for printing
        → 100 ステップごとに頻繁に出力。
        0     ! step for printing
        → 出力を抑止または既定間隔に従う。

Returns:
    int: ログ出力間隔（ステップ数単位）

### `set_print_interval(self, interval_step: int, *, auto_write: Optional[bool]=True)`

8 行目（step for printing）を更新する。

Notes:
    内容:
        - 計算経過を標準出力やログに記録する間隔を指定する。
          値は「ステップ数」で指定し、0 の場合は無効または既定値使用。

    例:
        5000 → 5000 ステップごとに出力。
        100  → 100 ステップごとに出力。
        0    → 出力を抑止。

Args:
    interval_step (int):
        出力間隔（ステップ数単位）
    auto_write (bool | None):
        True の場合は即時保存。None の場合はインスタンス既定値に従う。

### `get_time_and_save(self)`

9 行目（time limit, step for saving）を取得する。

Notes:
    内容:
        - 9 行目は、計算の停止条件と出力間隔を設定する 2 つの値からなる。
          RMC_POT マニュアルでは「time limit, step for saving」と定義されている。

          (1) time limit:
              - 計算の最大実行時間（単位: 分）
              - 経過時間がこの値を超えると自動停止する。
              - 0 の場合は無効（時間制限なし）

          (2) step for saving:
              - RMC 計算の進行中、どの間隔で現在構造などをファイルに保存するか。
              - ステップ数単位で指定（例: 5000 → 5000 ステップごとに保存）
              - 0 の場合は無効（または既定間隔に従う）

    例:
        0.2 0   ! time limit, step for saving
        → 最大 0.2 分（12 秒）で終了、保存間隔は無効
        60 500  ! time limit, step for saving
        → 60 分で停止、500 ステップごとに保存

Returns:
    tuple[float, int]:
        (time_limit_min, save_interval_step)

### `set_time_and_save(self, time_limit_min: float, save_interval_step: float, *, auto_write: Optional[bool]=True)`

9 行目（time limit, step for saving）を更新する。

Notes:
    内容:
        - time limit:
            計算の最大実行時間（分単位, float）。
            0 の場合は時間制限なし。
        - step for saving:
            結果ファイルを出力するステップ間隔（整数ステップ）。
            0 の場合は自動保存を無効化。

    例:
        (60, 1000)
        → 最大 60 分で停止、1000 ステップごとに結果保存。
        (0, 0)
        → 両方無効化（時間制限も保存間隔も設定しない）。

Args:
    time_limit_min (float): 最大実行時間（単位: 分）
    save_interval_step (float): 保存ステップ時間
    auto_write (bool | None): True で即時保存。None は既定に従う。

### `get_data_flags(self)`

10 行目（g(r), neutron, x-ray, EXAFS の出力フラグ）を取得する。

Notes:
    各整数は、その物理量の計算・出力を行うかどうかを指定する。

    順序は常に以下で固定される（RMC_POT マニュアル II.E 節より）:
        1. g(r) の計算フラグ
        2. neutron S(Q) の計算フラグ
        3. X-ray F(Q) の計算フラグ
        4. EXAFS χ(k) の計算フラグ

    仕様:
        - 0: 無効（そのデータ種を出力・比較しない）
        - 1: 有効（そのデータ種を出力・比較する）

    例:
        0 0 1 0  ! g(r), neutron, x-ray, EXAFS
        → g(r)=0, neutron=0, x-ray=1, EXAFS=0
        → X線データのみ出力・比較対象とする設定。

Returns:
    tuple[int, int, int, int]:
        (gr_flag, neutron_flag, xray_flag, exafs_flag)

### `set_data_flags(self, flags: Sequence[int], *, auto_write: Optional[bool]=True)`

10 行目（g(r), neutron, x-ray, EXAFS の出力フラグ）を更新する。

Notes:
    内容:
        - 10 行目は、4 つの整数値で各データ種の出力可否を指定する。
          順序は固定:
            (1) g(r)
            (2) neutron S(Q)
            (3) X-ray F(Q)
            (4) EXAFS χ(k)
        - 各値の意味:
            0: 無効（出力・比較を行わない）
            1: 有効（出力・比較を行う）

    例:
        (0, 0, 1, 0)
        [0, 0, 1, 0]
        → g(r)=off, neutron=off, X-ray=on, EXAFS=off
          → X線 F(Q) のみを比較対象に設定。

Args:
    flags (Sequence[int]):
        (gr_flag, neutron_flag, xray_flag, exafs_flag) を表す長さ 4 の列。
        tuple でも list でもよい。
    auto_write (bool | None):
        True なら即時保存。None の場合はインスタンス既定に従う。

### `get_exp_filename(self)`

11 行目（実験データファイル名）を返す（旧来固定フォーマット）。

Notes:
    - .dat ファイルの 10 行目には、
      g(r), neutron S(Q), X-ray F(Q), EXAFS χ(k) の順に
      4 つの整数が並びます。これらは各データ種のブロック数を表し、
      0 は「そのデータ種のブロックが無い」ことを意味します。

    - 11 行目以降には、ブロック数が 1 以上のデータ種だけが
      上記の順番で並びます。各データ種について 2 行が 1 ブロックで、
      1 行目が実験データファイル名、
      2 行目が使用点範囲（開始・終了の 2 整数）です。

    - このメソッドは、そのうち最初のブロック（= 11 行目）に書かれている
      実験データファイル名だけを返します。
      例えば 10 行目が ``0 0 1 0`` の場合、11 行目は X-ray F(Q) 用の
      実験データファイル名になります。

    - 実験データファイル（.dat が参照する外部ファイル）のフォーマットは
      次のように固定されています。
      1 行目: データ点数 N（整数）
      2 行目: タイトル行（任意文字列）
      3 行目以降: データ点列

    - データ点列の列構成はデータ種ごとに次のようになります。
      g(r)        : r, g(r)（2 列）
      neutron S(Q): Q, S(Q)（2 列）
      X-ray F(Q)  : Q, F(Q), c_αβ が M 本（2+M 列）
      EXAFS χ(k)  : k, χ(k)（2 列）

    - X-ray F(Q) の場合、c_αβ の本数 M は
      ``M = ntypes * (ntypes + 1) / 2`` で決まります。
      c_αβ の並び順（いわゆる RMC 順）は
      11, 12, 13, …, 22, 23, …, 33 のような上三角の順序です。

    - 典型的な列構成の例として、
      5 列のファイルは 2 元系（Q, F(Q), c11, c12, c22）、
      8 列のファイルは 3 元系（Q, F(Q), c11, c12, c13, c22, c23, c33）
      に対応します。

### `set_exp_filename(self, path: Union[str, Path], *, auto_write: Optional[bool]=None)`

11 行目（実験データファイル名）を更新する（旧来固定フォーマット）。

Notes:
    .dat 側の決まり（旧来固定）:
        - 10 行目の順序は常に:
            g(r), neutron S(Q), X-ray F(Q), EXAFS χ(k)
        - 11 行目は、上記で有効な最初のブロックが X-ray の場合には
          その「ファイル名行」となる（例: `0 0 1 0`）。
          本メソッドは **11 行目のみ** を対象として文字列を書き換える。

    実験データファイルの中身（確認用の定義）
        - 1 行目: N（整数）
        - 2 行目: タイトル（任意。数値としては読まれない）
        - 3 行目以降（厳密定義）:
          - g(r)        : r, g(r)                                         （2 列）
          - neutron S(Q): Q, S(Q)                                         （2 列）
          - X-ray F(Q)  : Q, F(Q), c_αβ × M（RMC 順, M = ntypes*(ntypes+1)/2）
          - EXAFS χ(k)  : k, χ(k)                                         （2 列）

Args:
    path: 実験データファイルへのパス（相対・絶対いずれも可）。
    auto_write: True の場合は即時保存。None の場合はインスタンス既定に従う。

### `get_exp_range(self)`

12 行目（実験データの読み込み範囲）を取得する。

Notes:
    - 旧来固定フォーマットでは、
      11 行目が実験データファイル名、
      12 行目が読み込み範囲を表す 2 つの整数になっています。

    - 12 行目の 2 つの整数は、
      「開始インデックス」と「終了インデックス」を 1 始まり（inclusive）で指定します。
      対象は実験データファイルの「データ本体行」であり、
      1 行目の点数 N、2 行目のタイトル行は含みません。

    - 範囲指定の例:
      ``1 290`` → データ本体の 1〜290 行を利用
      ``1 991`` → データ本体の 1〜991 行を利用
                  （実データ点数 N を超える指定は推奨されません）

    - 終了インデックスが実データ点数 N を超えた場合の挙動は
      RMC_POT の版に依存する可能性があります。
      このメソッド自身は読み取りのみを行い、範囲の検査や補正は行いません。

### `set_exp_range(self, start: int, end: int, *, auto_write: Optional[bool]=None)`

12 行目（実験データの読み込み範囲）を更新する。

Notes:
    【書式（旧来固定フォーマット）】
    - 2 整数のみ（1 始まり・inclusive）
      ・start: 開始インデックス（>=1）
      ・end  : 終了インデックス（>= start）

    【推奨運用】
    - 実験データファイル 1 行目の点数 N を参照し、end を N 以下に揃えること。

Args:
    start (int): 1 始まりの開始行（inclusive, >=1）
    end (int):   1 始まりの終了行（inclusive, >=start）
    auto_write (bool | None): True で即時保存。None はインスタンス既定に従う。

### `get_scale_factor(self)`

13 行目（scale factor）を取得する。

Notes:
    - 実験 S(Q) や F(Q) に対してスケールを合わせるための係数。
      シミュレーション出力を実験データと正規化するために使用される。
    - 一般的な初期値は 1.0。

Returns:
    float: スケーリング因子。

### `set_scale_factor(self, value: float, *, auto_write: Optional[bool]=None)`

13 行目（scale factor）を設定する。

Args:
    value (float): スケーリング因子。
    auto_write (bool | None): True で即時保存。

### `get_sigma_factor(self)`

14 行目（standard deviation / temperature factor）を取得する。

Notes:
    - メトロポリス法で使用する標準偏差 σ（温度因子）を表す。
    - マニュアルでは “standard deviation” と記載されており、
      サンプルでは「5E-3 0」や「5E-3 1」のように 2 つの値を取る場合がある。
      ここでは先頭値 σ のみを返す。

Returns:
    float: 標準偏差（σ）。

### `set_sigma_factor(self, sigma: float, *, auto_write: Optional[bool]=None)`

14 行目（standard deviation / temperature factor）を設定する。

Args:
    sigma (float): 標準偏差（σ）。
    auto_write (bool | None): True で即時保存。

### `get_flag_15(self)`

15 行目（boolean flag 1）を取得する。

Notes:
    - ブール値 (.true./.false.)。
      通常は S(Q) のバックグラウンド補正や平滑化の有無を指定する。

Returns:
    bool: True の場合は有効化。

### `set_flag_15(self, value: bool, *, auto_write: Optional[bool]=None)`

15 行目（boolean flag 1）を設定する。

### `get_flag_16(self)`

16 行目（boolean flag 2）を取得する。

Notes:
    - ブール値 (.true./.false.)。
      データ重み付けを行うかどうかを示すことが多い。

Returns:
    bool: True の場合は有効化。

### `set_flag_16(self, value: bool, *, auto_write: Optional[bool]=None)`

16 行目（boolean flag 2）を設定する。

### `get_flag_17(self)`

17 行目（boolean flag 3）を取得する。

Notes:
    - ブール値 (.true./.false.)。
      追加オプション（誤差正規化・スムージングなど）を制御する場合がある。

Returns:
    bool: True の場合は有効化。

### `set_flag_17(self, value: bool, *, auto_write: Optional[bool]=None)`

17 行目（boolean flag 3）を設定する。

### `get_flag_18(self)`

18 行目（boolean flag 4）を取得する。

Notes:
    - ブール値 (.true./.false.)。
      一般的に、データ処理や誤差解析の補助機能をオン/オフする。

Returns:
    bool: True の場合は有効化。

### `set_flag_18(self, value: bool, *, auto_write: Optional[bool]=None)`

18 行目（boolean flag 4）を設定する。

### `get_angle_constraint_count(self)`

19 行目（number of cos. distr of bond angles constraint）を取得する。

Notes:
    - ボンド角度分布に基づく制約数。
      0 の場合、角度分布制約を適用しない。

Returns:
    int: 角度制約数。

### `set_angle_constraint_count(self, value: int, *, auto_write: Optional[bool]=None)`

19 行目（角度制約数）を設定する。

### `get_coord_constraint_count(self)`

20 行目（number of coordination constraints）を取得する。

Note:
    - 配位数に基づく制約の数。
      0 の場合は適用しない。

Returns:
    int: 配位数制約の数。

### `set_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None)`

20 行目（配位数制約数）を設定する。

### `get_avg_coord_constraint_count(self)`

21 行目（number of average coordination constraints）を取得する。

Note:
    - 平均配位数に関する制約数。
      0 の場合は制約なし。

Returns:
    int: 平均配位数制約の数。

### `set_avg_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None)`

21 行目（平均配位数制約数）を設定する。

### `get_potential_flag(self)`

22 行目（potential flag）を取得する。

Note:
    - ポテンシャル使用のフラグまたは選択番号。
      0 の場合はポテンシャル未使用。

Returns:
    int: ポテンシャルフラグ。

### `set_potential_flag(self, value: int, *, auto_write: Optional[bool]=None)`

22 行目（ポテンシャルフラグ）を設定する。

### `get_fnc_switch(self)`

23 行目（FNC switch）の先頭番号を取得する。

Note:
    - 0: FNC なし
    - 1: 通常 FNC。初期構造が FNC 距離範囲内にあることを要求する。
    - 2: FNC 距離範囲を初期構造に合わせて調整して開始する。
    - 3: 範囲外ペアを許して開始し、範囲内へ近づく move を受理する。
    - 4: flexible molecule / bonded potential。通常 FNC ではなく topology を使う。

Returns:
    int: FNC switch の先頭番号。

### `get_fnc_options(self)`

23 行目（FNC switch）の先頭番号以降のオプションを取得する。

Returns:
    List[str]: 例: ["-D_FF_OPLS", "-D_FLEX", "-DORI_ANGLE"]

### `set_fnc_switch(self, value: Union[bool, int], *, opt: Optional[Union[str, Sequence[str]]]=None, keep_existing_opt: bool=True, auto_write: Optional[bool]=None)`

23 行目（FNC switch）を設定する。

Args:
    value: True/False または RMC_POT の FNC switch 番号。
        True は 1、False は 0 に変換する。
        int を渡した場合は、その番号指定を最優先する。
    opt: FNC switch 番号の後ろに付ける追加オプション。
        例: "-D_FF_OPLS -D_FLEX -DORI_ANGLE -DORI_BOND"
    keep_existing_opt: opt が None の場合に、既存行の追加オプションを保持する。
        ただし value が bool の場合は通常の有効/無効操作なので保持しない。
    auto_write: True 指定で即時保存。None の場合はインスタンス既定に従う。

Examples:
    set_fnc_switch(True)
        -> "1"
    set_fnc_switch(False)
        -> "0"
    set_fnc_switch(3)
        -> "3"
    set_fnc_switch(4, opt="-D_FF_OPLS -D_FLEX -DORI_ANGLE -DORI_BOND")
        -> "4 -D_FF_OPLS -D_FLEX -DORI_ANGLE -DORI_BOND"

### `get_fnc_distance_ranges(self, fnc_name: Optional[str]=None)`

FNC ファイルの constraint type ごとの rmin/rmax を取得する。

### `set_fnc_distance_ranges(self, ranges: Dict[int, Tuple[float, float]], fnc_name: Optional[str]=None)`

FNC ファイルの constraint type ごとの rmin/rmax を更新する。

既存の FNC ペア、neighbor index、constraint type は変更しない。
変更するのはヘッダの rmin/rmax のみである。

### `get_initial_bin_shift(self)`

24 行目（initial bin shift）を取得する。

Note:
    - g(r) 等のヒストグラム初期シフト値。
      0 はシフトなし。

Returns:
    int: 初期ビンシフト。

### `set_initial_bin_shift(self, value: int, *, auto_write: Optional[bool]=None)`

24 行目（initial bin shift）を設定する。

### `get_xmax_used(self)`

25 行目（xmax used in the run）を取得する。

Note:
    - g(r) 等の計算に用いる最大 r 値。
      スケール因子的に使われることもある。

Returns:
    float: xmax の値。

### `set_xmax_used(self, value: float, *, auto_write: Optional[bool]=None)`

25 行目（xmax used in the run）を設定する。

### `get_num_atoms_per_move(self)`

26 行目（number of atoms moved in a single move）を取得する。

Note:
    - 1 回の move 操作で同時に動かす原子の数。
      通常は 1。

Returns:
    int: 移動させる原子数。

### `set_num_atoms_per_move(self, value: int, *, auto_write: Optional[bool]=None)`

26 行目（number of atoms moved）を設定する。

### `get_history_buffer_size(self)`

27 行目（size of the history buffer）を取得する。

Note:
    - 受理率など過去情報を保持する履歴バッファサイズ。
      統計の平滑化に使用される。

Returns:
    int: バッファサイズ。

### `set_history_buffer_size(self, value: int, *, auto_write: Optional[bool]=None)`

27 行目（history buffer size）を設定する。

### `get_display_update_interval(self)`

28 行目（number of display updates between each history buffering）を取得する。

Returns:
    int: 表示更新の間隔。

### `set_display_update_interval(self, value: int, *, auto_write: Optional[bool]=None)`

28 行目（display update interval）を設定する。

### `get_custom_move_flag(self)`

29 行目（indicator of custom move）を取得する。

Returns:
    int: カスタムムーブ使用フラグ（0/1）。

### `set_custom_move_flag(self, value: int, *, auto_write: Optional[bool]=None)`

29 行目（custom move flag）を設定する。

### `get_load_histogram_flag(self)`

30 行目（whether to load the histogram from file）を取得する。

Returns:
    int: 0 ならロードしない、1 ならロードする。

### `set_load_histogram_flag(self, value: int, *, auto_write: Optional[bool]=None)`

30 行目（load histogram flag）を設定する。

### `get_max_atoms_per_cell(self)`

31 行目（maximum number of atoms in a gridcell）を取得する。

Returns:
    int: グリッドセル内最大原子数。

### `set_max_atoms_per_cell(self, value: int, *, auto_write: Optional[bool]=None)`

31 行目（max atoms per gridcell）を設定する。

### `get_swap_settings(self)`

32 行目（fraction of swaps, allow flag）を取得する。

Returns:
    tuple[int, int]: (swap_fraction, allow_flag)

### `set_swap_settings(self, fraction: int, allow_flag: int, *, auto_write: Optional[bool]=None)`

32 行目（swap fraction と許可フラグ）を設定する。

### `get_thread_count(self)`

33 行目（total number of threads to use）を取得する。

Returns:
    int: 使用スレッド数。

### `set_thread_count(self, value: int, *, auto_write: Optional[bool]=None)`

33 行目（スレッド数）を設定する。

### `get_local_invariance(self, line_no_1based: int)`

_LOCAL_INV 有効時の fixed-format local invariance 行を読む。

### `set_local_invariance(self, line_no_1based: int, sigma_values: Sequence[Union[int, float]], ratios: Sequence[Union[int, float]], *, mode: int=1, auto_write: Optional[bool]=None)`

_LOCAL_INV 有効時の fixed-format local invariance 行を設定する。

### `get_non_periodic(self, line_no_1based: int)`

_NO_PERIODIC 有効時の fixed-format spherical sample 行を読む。

### `set_non_periodic(self, line_no_1based: int, sample_radius: Union[int, float], *, recentre: bool=False, auto_write: Optional[bool]=None)`

_NO_PERIODIC 有効時の fixed-format spherical sample 行を設定する。

### `get_vibrational_amplitudes(self, line_no_1based: int)`

_VIBR_AMP 有効時の fixed-format sigma 行を読む。

### `set_vibrational_amplitudes(self, line_no_1based: int, sigma_values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=None)`

_VIBR_AMP 有効時の fixed-format sigma 行を設定する。

## `main()`

固定形式 DAT の基本設定を書き込む利用例。


## 実装に基づく API 一覧


### `RmcPotDatFixed` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 82 | config インスタンスを与えると、_cfg_name はいらない |
| `set_cfg_name()` | 184 | 読み書き対象の構成名を変更する。 |
| `create_dat_file()` | 193 | 与えられたベース名から <basename>.dat を作成し、 |
| `load()` | 260 | ファイルを読み込んで内部行リストを構築。 |
| `write()` | 292 | 現在の内容を書き出す (.dat は自動付加される) |
| `get_line()` | 311 | 任意行の値部分を返す（コメントは含めない） |
| `set_line()` | 325 | 任意行の値部分を更新（コメントは保持）。 |
| `insert_line()` | 355 | fixed format の指定物理行へ1行挿入する。 |
| `remove_line()` | 379 | fixed format の指定物理行を削除する。 |
| `set_element_info()` | 444 | 固定形式には元素記号を保持する欄がないため設定できない。 |
| `get_comment()` | 460 | 1 行目 comment を str で返す。 |
| `set_comment()` | 464 | 1 行目 comment を更新。 |
| `get_density()` | 475 | 2 行目 density を float で返す。 |
| `set_density()` | 500 | 2 行目 density を更新。 |
| `get_cutoffs()` | 511 | 3 行目 cut offs を (c1, c2, c3) で返す。 |
| `set_cutoffs()` | 530 | 3 行目 cut offs を更新。可変長対応。 |
| `get_max_moves()` | 613 | 4 行目 maximum moves を (m1, m2) で返す。 |
| `set_maximum_moves()` | 631 | 4 行目 maximum moves を可変長で更新する。 |
| `get_r_spacing()` | 660 | 5 行目 r spacing を float で返す。i |
| `set_r_spacing()` | 688 | 5 行目 r spacing を更新。 |
| `get_moveout_option()` | 699 | 6 行目（whether to use moveout option）を取得する。 |
| `set_moveout_option()` | 745 | 6 行目（whether to use moveout option）を更新する。 |
| `get_num_config_to_collect()` | 781 | 7 行目（number of configuration to collect）を取得する。 |
| `set_num_config_to_collect()` | 822 | 7 行目（number of configuration to collect）を更新する。 |
| `get_print_interval()` | 860 | 8 行目（step for printing）を取得する。 |
| `set_print_interval()` | 896 | 8 行目（step for printing）を更新する。 |
| `get_time_and_save()` | 927 | 9 行目（time limit, step for saving）を取得する。 |
| `set_time_and_save()` | 964 | 9 行目（time limit, step for saving）を更新する。 |
| `get_data_flags()` | 1010 | 10 行目（g(r), neutron, x-ray, EXAFS の出力フラグ）を取得する。 |
| `set_data_flags()` | 1051 | 10 行目（g(r), neutron, x-ray, EXAFS の出力フラグ）を更新する。 |
| `get_exp_filename()` | 1098 | 11 行目（実験データファイル名）を返す（旧来固定フォーマット）。 |
| `set_exp_filename()` | 1160 | 11 行目（実験データファイル名）を更新する（旧来固定フォーマット）。 |
| `get_exp_range()` | 1193 | 12 行目（実験データの読み込み範囲）を取得する。 |
| `set_exp_range()` | 1239 | 12 行目（実験データの読み込み範囲）を更新する。 |
| `get_scale_factor()` | 1270 | 13 行目（scale factor）を取得する。 |
| `set_scale_factor()` | 1284 | 13 行目（scale factor）を設定する。 |
| `get_sigma_factor()` | 1299 | 14 行目（standard deviation / temperature factor）を取得する。 |
| `set_sigma_factor()` | 1327 | 14 行目（standard deviation / temperature factor）を設定する。 |
| `get_flag_15()` | 1343 | 15 行目（boolean flag 1）を取得する。 |
| `set_flag_15()` | 1356 | 15 行目（boolean flag 1）を設定する。 |
| `get_flag_16()` | 1365 | 16 行目（boolean flag 2）を取得する。 |
| `set_flag_16()` | 1378 | 16 行目（boolean flag 2）を設定する。 |
| `get_flag_17()` | 1387 | 17 行目（boolean flag 3）を取得する。 |
| `set_flag_17()` | 1400 | 17 行目（boolean flag 3）を設定する。 |
| `get_flag_18()` | 1409 | 18 行目（boolean flag 4）を取得する。 |
| `set_flag_18()` | 1422 | 18 行目（boolean flag 4）を設定する。 |
| `get_angle_constraint_count()` | 1431 | 19 行目（number of cos. distr of bond angles constraint）を取得する。 |
| `set_angle_constraint_count()` | 1444 | 19 行目（角度制約数）を設定する。 |
| `get_coord_constraint_count()` | 1453 | 20 行目（number of coordination constraints）を取得する。 |
| `set_coord_constraint_count()` | 1466 | 20 行目（配位数制約数）を設定する。 |
| `get_avg_coord_constraint_count()` | 1475 | 21 行目（number of average coordination constraints）を取得する。 |
| `set_avg_coord_constraint_count()` | 1488 | 21 行目（平均配位数制約数）を設定する。 |
| `get_potential_flag()` | 1497 | 22 行目（potential flag）を取得する。 |
| `set_potential_flag()` | 1510 | 22 行目（ポテンシャルフラグ）を設定する。 |
| `get_fnc_switch()` | 1519 | 23 行目（FNC switch）の先頭番号を取得する。 |
| `get_fnc_options()` | 1535 | 23 行目（FNC switch）の先頭番号以降のオプションを取得する。 |
| `set_fnc_switch()` | 1580 | 23 行目（FNC switch）を設定する。 |
| `get_fnc_distance_ranges()` | 1654 | FNC ファイルの constraint type ごとの rmin/rmax を取得する。 |
| `set_fnc_distance_ranges()` | 1705 | FNC ファイルの constraint type ごとの rmin/rmax を更新する。 |
| `get_initial_bin_shift()` | 1776 | 24 行目（initial bin shift）を取得する。 |
| `set_initial_bin_shift()` | 1789 | 24 行目（initial bin shift）を設定する。 |
| `get_xmax_used()` | 1798 | 25 行目（xmax used in the run）を取得する。 |
| `set_xmax_used()` | 1811 | 25 行目（xmax used in the run）を設定する。 |
| `get_num_atoms_per_move()` | 1820 | 26 行目（number of atoms moved in a single move）を取得する。 |
| `set_num_atoms_per_move()` | 1843 | 26 行目（number of atoms moved）を設定する。 |
| `get_history_buffer_size()` | 1853 | 27 行目（size of the history buffer）を取得する。 |
| `set_history_buffer_size()` | 1866 | 27 行目（history buffer size）を設定する。 |
| `get_display_update_interval()` | 1875 | 28 行目（number of display updates between each history buffering）を取得する。 |
| `set_display_update_interval()` | 1884 | 28 行目（display update interval）を設定する。 |
| `get_custom_move_flag()` | 1893 | 29 行目（indicator of custom move）を取得する。 |
| `set_custom_move_flag()` | 1902 | 29 行目（custom move flag）を設定する。 |
| `get_load_histogram_flag()` | 1911 | 30 行目（whether to load the histogram from file）を取得する。 |
| `set_load_histogram_flag()` | 1920 | 30 行目（load histogram flag）を設定する。 |
| `get_max_atoms_per_cell()` | 1929 | 31 行目（maximum number of atoms in a gridcell）を取得する。 |
| `set_max_atoms_per_cell()` | 1938 | 31 行目（max atoms per gridcell）を設定する。 |
| `get_swap_settings()` | 1947 | 32 行目（fraction of swaps, allow flag）を取得する。 |
| `set_swap_settings()` | 1959 | 32 行目（swap fraction と許可フラグ）を設定する。 |
| `get_thread_count()` | 1969 | 33 行目（total number of threads to use）を取得する。 |
| `set_thread_count()` | 1978 | 33 行目（スレッド数）を設定する。 |
| `get_local_invariance()` | 1987 | _LOCAL_INV 有効時の fixed-format local invariance 行を読む。 |
| `set_local_invariance()` | 2002 | _LOCAL_INV 有効時の fixed-format local invariance 行を設定する。 |
| `get_non_periodic()` | 2026 | _NO_PERIODIC 有効時の fixed-format spherical sample 行を読む。 |
| `set_non_periodic()` | 2040 | _NO_PERIODIC 有効時の fixed-format spherical sample 行を設定する。 |
| `get_vibrational_amplitudes()` | 2057 | _VIBR_AMP 有効時の fixed-format sigma 行を読む。 |
| `set_vibrational_amplitudes()` | 2064 | _VIBR_AMP 有効時の fixed-format sigma 行を設定する。 |

### `_Line` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `render()` | 2093 | 現在の値とコメントから 1 行のテキストを生成する。 |

### モジュール関数 `main()`

- 定義位置：2103 行
- 説明：固定形式 DAT の基本設定を書き込む利用例。

## ソースコードに基づく引数・戻り値一覧


### `RmcPotDatFixed.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |
| `cfg_name` | `Optional[str]` |
| `auto_write` | `bool` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:82`。

### `RmcPotDatFixed.set_cfg_name`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:184`。

### `RmcPotDatFixed.create_dat_file`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `basename` | `str` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:193`。

### `RmcPotDatFixed.load`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:260`。

### `RmcPotDatFixed.write`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `out_name` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:292`。

### `RmcPotDatFixed.get_line`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_dat_fixed(10).py:311`。

### `RmcPotDatFixed.set_line`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |
| `value` | `Union[str, int, float, Sequence[Union[int, float]], bool]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:325`。

### `RmcPotDatFixed.insert_line`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |
| `value` | `Union[str, int, float, Sequence[Union[int, float]], bool]` |
| `comment` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:355`。

### `RmcPotDatFixed.remove_line`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:379`。

### `RmcPotDatFixed.set_element_info`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `element_info` | `Sequence[str]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:444`。

### `RmcPotDatFixed.get_comment`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_dat_fixed(10).py:460`。

### `RmcPotDatFixed.set_comment`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `comment` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:464`。

### `RmcPotDatFixed.get_density`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_fixed(10).py:475`。

### `RmcPotDatFixed.set_density`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `rho` | `Union[int, float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:500`。

### `RmcPotDatFixed.get_cutoffs`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Union[int, float]]`。定義位置: `rmc_pot_dat_fixed(10).py:511`。

### `RmcPotDatFixed.set_cutoffs`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `values` | `Sequence[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:530`。

### `RmcPotDatFixed.get_max_moves`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[float, float]`。定義位置: `rmc_pot_dat_fixed(10).py:613`。

### `RmcPotDatFixed.set_maximum_moves`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `values` | `Sequence[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:631`。

### `RmcPotDatFixed.get_r_spacing`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_fixed(10).py:660`。

### `RmcPotDatFixed.set_r_spacing`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `dr` | `Union[int, float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:688`。

### `RmcPotDatFixed.get_moveout_option`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:699`。

### `RmcPotDatFixed.set_moveout_option`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `use_moveout` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:745`。

### `RmcPotDatFixed.get_num_config_to_collect`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:781`。

### `RmcPotDatFixed.set_num_config_to_collect`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `num_config` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:822`。

### `RmcPotDatFixed.get_print_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:860`。

### `RmcPotDatFixed.set_print_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `interval_step` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:896`。

### `RmcPotDatFixed.get_time_and_save`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[float, int]`。定義位置: `rmc_pot_dat_fixed(10).py:927`。

### `RmcPotDatFixed.set_time_and_save`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `time_limit_min` | `float` |
| `save_interval_step` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:964`。

### `RmcPotDatFixed.get_data_flags`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[int, int, int, int]`。定義位置: `rmc_pot_dat_fixed(10).py:1010`。

### `RmcPotDatFixed.set_data_flags`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `flags` | `Sequence[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1051`。

### `RmcPotDatFixed.get_exp_filename`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_dat_fixed(10).py:1098`。

### `RmcPotDatFixed.set_exp_filename`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `path` | `Union[str, Path]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1160`。

### `RmcPotDatFixed.get_exp_range`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[int, int]`。定義位置: `rmc_pot_dat_fixed(10).py:1193`。

### `RmcPotDatFixed.set_exp_range`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `start` | `int` |
| `end` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1239`。

### `RmcPotDatFixed.get_scale_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_fixed(10).py:1270`。

### `RmcPotDatFixed.set_scale_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1284`。

### `RmcPotDatFixed.get_sigma_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_fixed(10).py:1299`。

### `RmcPotDatFixed.set_sigma_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `sigma` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1327`。

### `RmcPotDatFixed.get_flag_15`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:1343`。

### `RmcPotDatFixed.set_flag_15`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1356`。

### `RmcPotDatFixed.get_flag_16`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:1365`。

### `RmcPotDatFixed.set_flag_16`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1378`。

### `RmcPotDatFixed.get_flag_17`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:1387`。

### `RmcPotDatFixed.set_flag_17`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1400`。

### `RmcPotDatFixed.get_flag_18`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_fixed(10).py:1409`。

### `RmcPotDatFixed.set_flag_18`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1422`。

### `RmcPotDatFixed.get_angle_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1431`。

### `RmcPotDatFixed.set_angle_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1444`。

### `RmcPotDatFixed.get_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1453`。

### `RmcPotDatFixed.set_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1466`。

### `RmcPotDatFixed.get_avg_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1475`。

### `RmcPotDatFixed.set_avg_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1488`。

### `RmcPotDatFixed.get_potential_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1497`。

### `RmcPotDatFixed.set_potential_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1510`。

### `RmcPotDatFixed.get_fnc_switch`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1519`。

### `RmcPotDatFixed.get_fnc_options`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[str]`。定義位置: `rmc_pot_dat_fixed(10).py:1535`。

### `RmcPotDatFixed.set_fnc_switch`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `Union[bool, int]` |
| `opt` | `Optional[Union[str, Sequence[str]]]` |
| `keep_existing_opt` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1580`。

### `RmcPotDatFixed.get_fnc_distance_ranges`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `fnc_name` | `Optional[str]` |

戻り値の型注釈: `Dict[int, Tuple[float, float]]`。定義位置: `rmc_pot_dat_fixed(10).py:1654`。

### `RmcPotDatFixed.set_fnc_distance_ranges`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `ranges` | `Dict[int, Tuple[float, float]]` |
| `fnc_name` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1705`。

### `RmcPotDatFixed.get_initial_bin_shift`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1776`。

### `RmcPotDatFixed.set_initial_bin_shift`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1789`。

### `RmcPotDatFixed.get_xmax_used`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_fixed(10).py:1798`。

### `RmcPotDatFixed.set_xmax_used`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1811`。

### `RmcPotDatFixed.get_num_atoms_per_move`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1820`。

### `RmcPotDatFixed.set_num_atoms_per_move`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1843`。

### `RmcPotDatFixed.get_history_buffer_size`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1853`。

### `RmcPotDatFixed.set_history_buffer_size`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1866`。

### `RmcPotDatFixed.get_display_update_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1875`。

### `RmcPotDatFixed.set_display_update_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1884`。

### `RmcPotDatFixed.get_custom_move_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1893`。

### `RmcPotDatFixed.set_custom_move_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1902`。

### `RmcPotDatFixed.get_load_histogram_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1911`。

### `RmcPotDatFixed.set_load_histogram_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1920`。

### `RmcPotDatFixed.get_max_atoms_per_cell`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1929`。

### `RmcPotDatFixed.set_max_atoms_per_cell`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1938`。

### `RmcPotDatFixed.get_swap_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[int, int]`。定義位置: `rmc_pot_dat_fixed(10).py:1947`。

### `RmcPotDatFixed.set_swap_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `fraction` | `int` |
| `allow_flag` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1959`。

### `RmcPotDatFixed.get_thread_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_fixed(10).py:1969`。

### `RmcPotDatFixed.set_thread_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:1978`。

### `RmcPotDatFixed.get_local_invariance`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |

戻り値の型注釈: `Tuple[int, List[float], int, List[float]]`。定義位置: `rmc_pot_dat_fixed(10).py:1987`。

### `RmcPotDatFixed.set_local_invariance`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |
| `sigma_values` | `Sequence[Union[int, float]]` |
| `ratios` | `Sequence[Union[int, float]]` |
| `mode` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:2002`。

### `RmcPotDatFixed.get_non_periodic`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |

戻り値の型注釈: `Tuple[float, bool]`。定義位置: `rmc_pot_dat_fixed(10).py:2026`。

### `RmcPotDatFixed.set_non_periodic`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |
| `sample_radius` | `Union[int, float]` |
| `recentre` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:2040`。

### `RmcPotDatFixed.get_vibrational_amplitudes`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |

戻り値の型注釈: `List[float]`。定義位置: `rmc_pot_dat_fixed(10).py:2057`。

### `RmcPotDatFixed.set_vibrational_amplitudes`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line_no_1based` | `int` |
| `sigma_values` | `Sequence[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:2064`。

### `_Line.render`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_dat_fixed(10).py:2093`。

### `main`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_fixed(10).py:2103`。

