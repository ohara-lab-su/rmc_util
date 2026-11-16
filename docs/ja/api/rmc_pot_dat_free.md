# `rmc_util.rmc_pot_dat_free`

ソース: `src/rmc_util/rmc_pot_dat_free.py`

## クラス `RmcPotDatFree`

RMC_POT 自由形式 ``*.dat`` をセクション／キーワード単位で扱う。

# 実行バイナリが _ADVANCED_GEOM_CONST を有効に置く必要がある
# make AGC=0
# が必要となる

Attributes:
    直接公開する属性はない。設定値は既存の getter/setter または
    自由形式固有の ``get()``, ``set()``, ``add()`` を通して操作する。

Notes:
    ファイル上の実体である ``[ SECTION ]`` と ``KEY = VALUE`` を
    そのまま内部表現として保持する。

### `__init__(self, config: Optional[Config]=None, logger: Optional[XLogger]=None, *, cfg_name: Optional[str]=None, auto_write: bool=True, version: str='#003')`

自由形式 RMC_POT 入力ファイル編集クラスを初期化する。

Args:
    config: RMC_DFT 全体設定。省略時は新しい ``Config`` を使用する。
    logger: ログ出力に使用する ``XLogger``。省略時は新規作成する。
    cfg_name: 読み書きする ``*.dat`` の拡張子を除いた名前。
        省略時は ``config.cfg_name`` を使用する。
    auto_write: setter 実行後に自動保存する既定動作。
    version: 自由形式ファイル先頭へ書く形式識別子。
        ``#002`` または ``#003`` を想定する。

Notes:
    自由形式のセクション名とキーワードを直接読み書きする。

    ``<cfg_name>.dat`` が存在する場合は、その自由形式ファイルを読み込み、
    先頭行の ``#002`` または ``#003`` を以後の出力形式として維持する。
    ファイルが存在しない場合だけ、``version`` で指定した形式の
    デフォルト ``*.dat`` を新規作成する。

    ``auto_write=True`` の場合、各 setter は更新直後に ``*.dat`` へ
    反映する。複数設定をまとめて反映したい場合だけ、
    インスタンスまたは各メソッドで ``auto_write=False`` を指定する。

### `create_dat_file(self, basename: str)`

自由形式の初期 ``*.dat`` ファイルを作成する。

Args:
    basename: 出力ファイル名から ``.dat`` を除いた部分。

Returns:
    新規作成した場合は ``True``。同名ファイルが既に存在する場合は
    上書きせず ``False`` を返す。

Notes:
    初期値は ``[ GENERAL ]`` セクションへ自由形式のキーとして設定する。
    物理的な行配置には依存しない。

    初期状態では ``FNC-TYPE = NONE`` とし、``[ BPOT ]`` を作成しない。
    したがって ``set_fnc_switch()`` を呼ばなければ、FNC も topology も
   使用しない自由形式 ``*.dat`` になる。

### `load(self)`

現在の ``cfg_name`` に対応する自由形式ファイルを読み込む。

Returns:
    ファイルを読み込めた場合は ``True``。対象ファイルが存在しない場合は
    ``False`` を返す。

Raises:
    ValueError: ファイルが空、形式識別子が不正、またはセクション外に
        キー値が記述されている場合。

Notes:
    ``[ SECTION ]`` と ``KEY = VALUE`` を解析し、同一キーの複数出現を
    値リストとして保持する。継続行は直前のキー値へ連結する。

### `write(self, out_name: Optional[str]=None)`

保持している自由形式データを ``*.dat`` へ書き出す。

Args:
    out_name: 出力ファイル名から ``.dat`` を除いた部分。
        省略時は現在の ``cfg_name`` を使用する。

Notes:
    セクションの並び、キーの並び、同一キーの値順を内部表現の順序どおり
    出力する。

### `set(self, section: str, key: str, value: Any, index: int=0)`

自由形式の指定キーを単一値で設定する。

Args:
    section: セクション名。
    key: キー名。
    value: 設定する値。
    index: 同名セクションが複数ある場合の 0 始まり位置。

Notes:
    指定位置までセクションが存在しない場合は必要数を追加する。
    既存の同一キー値は置き換える。

### `add(self, section: str, key: str, value: Any, index: int=0)`

自由形式の指定キーへ値を追加する。

Args:
    section: セクション名。
    key: キー名。
    value: 追加する値。
    index: 同名セクションが複数ある場合の 0 始まり位置。

Notes:
    既存値は保持し、同じキーの値リスト末尾へ追加する。

### `get(self, section: str, key: str, index: int=0, default: Optional[str]=None)`

自由形式の指定キーから最初の値を取得する。

Args:
    section: セクション名。
    key: キー名。
    index: 同名セクションが複数ある場合の 0 始まり位置。
    default: セクションまたはキーが存在しない場合の戻り値。

Returns:
    最初の値、または ``default``。

### `get_all(self, section: str, key: str, index: int=0)`

自由形式の指定キーに登録された全値を取得する。

Args:
    section: セクション名。
    key: キー名。
    index: 同名セクションが複数ある場合の 0 始まり位置。

Returns:
    登録順を維持した値リスト。対象が存在しない場合は空リスト。

### `initialize_sections(self, section: str, *, auto_write: Optional[bool]=None)`

指定名のセクションをすべて削除して未設定状態へ戻す。

Args:
    section: 初期化するセクション名。
    auto_write: 初期化後に ``*.dat`` を保存するかどうか。
        ``None`` の場合はインスタンスの ``auto_write`` 設定を使う。

Notes:
    ``[ SNC ]``、``[ EXP ]``、``[ COS ]`` など、同じ名前の
    セクションを複数記述できる項目を作り直す前に使用する。

    空のセクションは作成しない。既存の同名セクションをすべて削除し、
    次の高水準 setter または add メソッドが完全なセクションを
    一つずつ追加できる状態にする。

### `initialize_qn_constraints(self, *, auto_write: Optional[bool]=None)`

【後方互換専用】旧 Qn/SNC 初期化API。

旧バージョンの ``initialize_qn_constraints()`` を使用するスクリプトの
互換性維持のためだけに残す。新規コードでは通常使用しない。

実際の削除処理は現行API ``clear_qn_constraints()`` に委譲する。
このメソッド自身には SNC の削除処理を重複実装しない。

### `add_section(self, section: str)`

空の自由形式セクションを末尾へ追加する。

Args:
    section: 追加するセクション名。

Returns:
    追加した同名セクションの 0 始まり位置。

Notes:
    内部構築用の低水準メソッドであり、自動書き込みは行わない。
    必須キーを持たない空セクションを一時的に作るためである。
    通常の制約設定では直接使用せず、``set_*_constraint(index=...)`` を使う。

### `remove_section(self, section: str, index: int=0)`

指定位置の自由形式セクションを削除する。

Args:
    section: セクション名。
    index: 同名セクションが複数ある場合の 0 始まり位置。

Raises:
    IndexError: 指定したセクション位置が存在しない場合。

### `remove(self, section: str, key: str, index: int=0)`

指定セクションからキーと全値を削除する。

Args:
    section: セクション名。
    key: 削除するキー名。
    index: 同名セクションが複数ある場合の 0 始まり位置。

Notes:
    対象セクションまたはキーが存在しない場合は何も変更しない。

### `section_count(self, section: str)`

指定名の自由形式セクション数を返す。

Args:
    section: セクション名。

Returns:
    同名セクションの件数。

### `set_cfg_name(self, cfg_name: str)`

読み書き対象の構成名を変更する。

Args:
    cfg_name: ``.dat`` を除いた新しい構成名。

Notes:
    クラス内部の名前と ``Config.cfg_name`` を同時に更新する。

### `set_element_info(self, element_info: Sequence[str], *, auto_write: Optional[bool]=None)`

原子タイプ順の元素記号を設定する。

### `get_comment(self)`

``[ GENERAL ]`` の ``TITLE`` を返す。

### `set_comment(self, comment: str, *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``TITLE`` を設定する。

### `get_density(self)`

``[ GENERAL ]`` の ``NDENS`` を返す。

### `set_density(self, rho: Union[int, float], *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``NDENS`` を設定する。

### `get_cutoffs(self)`

``[ GENERAL ]`` の ``CUT-OFF`` を RMC 順で返す。

``CUT-OFF`` は数値列のほか、自由形式で認められる ``MIN`` または
``MIN-ALL`` を取れる。

### `set_cutoffs(self, values: Union[str, Sequence[Union[int, float]]], *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``CUT-OFF`` を設定する。

数値列は RMC 順で指定する。自由形式固有の自動決定を使う場合は
``"MIN"`` または ``"MIN-ALL"`` を指定する。

### `get_max_moves(self)`

``[ GENERAL ]`` の ``MAX-MOVES`` を返す。

### `set_maximum_moves(self, values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``MAX-MOVES`` を設定する。

### `get_r_spacing(self)`

``[ GENERAL ]`` の ``R-SPACING`` を返す。

### `set_r_spacing(self, dr: Union[int, float], *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``R-SPACING`` を設定する。

### `get_moveout_option(self)`

``[ GENERAL ]`` の ``MOVEOUT`` を返す。

### `set_moveout_option(self, use_moveout: bool, *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``MOVEOUT`` を設定する。

### `get_num_config_to_collect(self)`

``[ GENERAL ]`` の ``COLL-NUMBER`` を返す。

### `set_num_config_to_collect(self, num_config: int, *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``COLL-NUMBER`` を設定する。

固定形式の同名メソッドと同じ ``num_config`` キーワード引数を受け取る。

### `get_print_interval(self)`

``[ GENERAL ]`` の ``PRINT-STEP`` を返す。

### `set_print_interval(self, interval_step: int, *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``PRINT-STEP`` を設定する。

固定形式の同名メソッドと同じ ``interval_step`` キーワード引数を受け取る。

### `get_time_and_save(self)`

``[ GENERAL ]`` の ``RUN-TIME`` と ``SAVE-TIME`` を返す。

### `set_time_and_save(self, time_limit_min: float, save_interval_step: float, *, auto_write: Optional[bool]=True)`

``[ GENERAL ]`` の ``RUN-TIME`` と ``SAVE-TIME`` を設定する。

### `get_data_flags(self)`

``[ EXP ]`` の ``TYPE`` からデータ種別ごとの件数を返す。

戻り値の順序は ``GR``, ``ND``, ``XRD``, ``EXAFS``。

### `set_data_flags(self, flags: Sequence[int], *, auto_write: Optional[bool]=True)`

指定されたデータ種別の ``[ EXP ]`` セクションを残す。

新しい ``[ EXP ]`` は ``TYPE`` だけを持つ。``DATAFILE`` などの必須値を
空文字やダミー値で補完しない。

### `get_exp_filename(self)`

最初の [ EXP ] セクションに設定された実験データファイル名を取得します。

Returns:
    str:
        [ EXP ] セクションの DATAFILE に設定された実験データファイル名。
    bool:
        False（[ EXP ] セクションが存在しない、DATAFILE が存在しない、
        または DATAFILE が空の場合）。

Notes:
    - 自由形式 (*.dat) では実験データは [ EXP ] セクションで定義されます。
    - DATAFILE キーには実験データファイル名を指定します。
    - このメソッドは最初の [ EXP ] セクションだけを対象とします。
    - 実験データファイル自体の形式は RMC_POT の仕様に従います。
      g(r)、neutron S(Q)、X-ray F(Q)、EXAFS χ(k) など、
      TYPE の指定に応じたデータファイルを参照します。

### `set_exp_filename(self, path: Union[str, Path], *, auto_write: Optional[bool]=None)`

最初の ``[ EXP ]`` の ``DATAFILE`` を設定する。

### `get_exp_range(self)`

最初の ``[ EXP ]`` の ``POINT-RANGE`` を返す。

### `set_exp_range(self, start: int, end: int, *, auto_write: Optional[bool]=None)`

最初の ``[ EXP ]`` の ``POINT-RANGE`` を設定する。

### `get_scale_factor(self)`

固定形式13行目に対応する ``CONST-SUBTRACT`` を返す。

### `set_scale_factor(self, value: float, *, auto_write: Optional[bool]=None)`

固定形式13行目に対応する ``CONST-SUBTRACT`` を設定する。

### `get_sigma_factor(self)`

最初の ``[ EXP ]`` の ``SIGMA`` を返す。

### `set_sigma_factor(self, sigma: float, *, auto_write: Optional[bool]=None)`

最初の ``[ EXP ]`` の ``SIGMA`` を設定する。

### `get_flag_15(self)`

固定形式15行目に対応する ``RENORM`` を返す。

### `set_flag_15(self, value: bool, *, auto_write: Optional[bool]=None)`

固定形式15行目に対応する ``RENORM`` を設定する。

### `get_flag_16(self)`

固定形式16行目に対応する定数項補正フラグを返す。

### `set_flag_16(self, value: bool, *, auto_write: Optional[bool]=None)`

固定形式16行目に対応する定数項補正フラグを設定する。

### `get_flag_17(self)`

固定形式17行目に対応する一次項補正フラグを返す。

### `set_flag_17(self, value: bool, *, auto_write: Optional[bool]=None)`

固定形式17行目に対応する一次項補正フラグを設定する。

### `get_flag_18(self)`

固定形式18行目に対応する二次項補正フラグを返す。

### `set_flag_18(self, value: bool, *, auto_write: Optional[bool]=None)`

固定形式18行目に対応する二次項補正フラグを設定する。

### `get_angle_constraint_count(self)`

``[ COS ]`` セクション数を返す。

### `set_angle_constraint_count(self, value: int, *, auto_write: Optional[bool]=None)`

固定形式互換で角度制約数を設定する。

``0`` は全 ``[ COS ]`` セクションの削除として扱う。正の値は、
既存セクション数と一致する場合だけ受理し、内容のない制約を捏造しない。

### `get_coord_constraint_count(self)`

``[ COORD ]`` セクション数を返す。

### `set_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None)`

固定形式互換で配位数制約数を設定する。

``0`` は全 ``[ COORD ]`` セクションの削除として扱う。正の値は、
既存セクション数と一致する場合だけ受理する。

### `get_avg_coord_constraint_count(self)`

``[ AVCOORD ]`` セクション数を返す。

### `set_avg_coord_constraint_count(self, value: int, *, auto_write: Optional[bool]=None)`

固定形式互換で平均配位数制約数を設定する。

``0`` は全 ``[ AVCOORD ]`` セクションの削除として扱う。正の値は、
既存セクション数と一致する場合だけ受理する。

### `get_potential_flag(self)`

potential セクションが存在する場合に ``1``、なければ ``0`` を返す。

### `set_potential_flag(self, value: int, *, auto_write: Optional[bool]=None)`

固定形式互換でpotentialの無効化または既存状態の確認を行う。

``0`` はpotential関連セクションをすべて削除する。正の値だけから
potential種別やパラメータは生成できないため、既存設定がある場合だけ受理する。

### `get_fnc_switch(self)`

FNC または ``[ BPOT ]`` の状態を数値で取得する。

Returns:
    0 から 4 の状態番号。

    - 0: FNC なし、かつ ``[ BPOT ]`` なし
    - 1: ``FNC-TYPE = NORMAL``
    - 2: ``FNC-TYPE = ADJUST``
    - 3: ``FNC-TYPE = MOVE-IN``
    - 4: ``[ BPOT ]`` による flexible molecule / topology mode

Notes:
    ``FNC-TYPE`` が存在しない場合も ``NONE`` として扱う。
    ``[ BPOT ]`` が存在しない場合は topology mode ではない。

    自由形式では ``FNC-TYPE`` に 4 または ``FLEXIBLE`` は存在しない。
    topology を使う flexible molecule mode は ``[ BPOT ]`` の存在で判定する。

### `get_fnc_options(self)`

FNC / topology option を取得する。

Returns:
    FNC 1～3 では ``FNC-TYPE`` の追加トークンを返す。
    topology mode では ``[ BPOT ]`` の ``COMP-OPTION`` を返す。

### `set_fnc_switch(self, value: Union[bool, int], *, opt: Optional[Union[str, Sequence[str]]]=None, keep_existing_opt: bool=True, auto_write: Optional[bool]=None)`

FNC または topology mode を設定する。

Args:
    value: ``False``/``True`` または 0～4 の状態番号。
    opt: FNC の追加トークン、または mode 4 の ``COMP-OPTION``。
    keep_existing_opt: ``opt`` 省略時に既存 option を保持するか。
    auto_write: 設定後に直ちに保存するか。

Raises:
    ValueError: FNC 1～3 と ``[ BPOT ]`` を同時指定した場合。

Notes:
    自由形式では FNC 1～3 は ``[ GENERAL ]`` の ``FNC-TYPE`` で指定する。
    flexible molecule mode は
    ``FNC-TYPE`` ではなく ``[ BPOT ]`` の存在で指定する。

### `validate_mode_configuration(self, *, check_input_files: bool=False)`

自由形式の mode 指定と入力ファイルを検証する。

Args:
    check_input_files: ``True`` の場合、mode が要求する
        ``*.fnc`` または ``*.top`` の存在も確認する。

Raises:
    ValueError: 排他的な mode が同時に設定されている場合。
    FileNotFoundError: 必要な外部入力ファイルが存在しない場合。

Notes:
    ``[ SNC ]`` は ``*.dat`` 内の制約セクションであり、
    外部 ``*.snc`` 入力ファイルを選択する mode ではない。

### `get_fnc_distance_ranges(self, fnc_name: Optional[str]=None)`

FNC ファイルの constraint type ごとの rmin/rmax を取得する。

### `set_fnc_distance_ranges(self, ranges: Dict[int, Tuple[float, float]], fnc_name: Optional[str]=None)`

FNC ファイルの constraint type ごとの rmin/rmax を更新する。

既存の FNC ペア、neighbor index、constraint type は変更しない。
変更するのはヘッダの rmin/rmax のみである。

### `get_initial_bin_shift(self)`

``[ GENERAL ]`` の ``BIN-SHIFT`` を返す。

### `set_initial_bin_shift(self, value: int, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``BIN-SHIFT`` を設定する。

### `get_xmax_used(self)`

``[ GENERAL ]`` の ``XMAX-FACTOR`` を返す。

### `set_xmax_used(self, value: float, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``XMAX-FACTOR`` を設定する。

### `get_num_atoms_per_move(self)`

1回の move で動かす原子数を返す。

通常の atomic move では常に1を返す。``[ CUSTMOVE ]`` が存在する場合は、
同セクションの ``NMOVED-ATOMS`` を返す。

### `set_num_atoms_per_move(self, value: int, *, auto_write: Optional[bool]=None)`

1回の custom move で動かす原子数を設定する。

``value=1`` かつ ``[ CUSTMOVE ]`` が存在しない場合は、通常の
atomic move の既定値として保持し、セクションは作成しない。
2以上を指定した場合は ``[ CUSTMOVE ]`` を作成して
``NMOVED-ATOMS`` を設定する。

### `get_history_buffer_size(self)`

``[ GENERAL ]`` の ``HST_BUFFSIZE`` を返す。

### `set_history_buffer_size(self, value: int, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``HST_BUFFSIZE`` を設定する。

### `get_display_update_interval(self)`

``[ GENERAL ]`` の ``HST-STEP-FACTOR`` を返す。

### `set_display_update_interval(self, value: int, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``HST-STEP-FACTOR`` を設定する。

### `get_custom_move_flag(self)`

``[ CUSTMOVE ]`` が存在する場合に1、存在しない場合に0を返す。

### `set_custom_move_flag(self, value: int, *, auto_write: Optional[bool]=None)`

custom move の有効・無効を ``[ CUSTMOVE ]`` の有無で設定する。

有効化時は、現在の ``get_num_atoms_per_move()`` の値を
``NMOVED-ATOMS`` に設定する。具体的な custom move パラメータは
``CUSTOM-LINE`` として別途追加する。

### `get_load_histogram_flag(self)`

``[ GENERAL ]`` の ``RELOAD`` を返す。

### `set_load_histogram_flag(self, value: int, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``RELOAD`` を設定する。

### `get_max_atoms_per_cell(self)`

``[ GENERAL ]`` の ``ATOMS-IN-GRIDCELL`` を返す。

### `set_max_atoms_per_cell(self, value: int, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``ATOMS-IN-GRIDCELL`` を設定する。

### `get_swap_settings(self)`

``[ SWAP ]`` の交換割合と有効状態を返す。

Returns:
    ``(FRACT, enabled)``。``[ SWAP ]`` が存在しない場合は
    固定形式の既定値に対応する ``(0.0, 0)`` を返す。

### `set_swap_settings(self, fraction: float, allow_flag: int, *, auto_write: Optional[bool]=None)`

固定形式互換のswap設定を自由形式の ``[ SWAP ]`` へ反映する。

``allow_flag=0`` または ``fraction=0`` の場合は ``[ SWAP ]`` を削除する。
有効化する場合は ``FRACT`` と ``PAIRS = ALL`` を設定する。
個別の原子種pairを指定する場合は ``set()`` または ``add()`` で
``[ SWAP ]`` の ``PAIRS`` を設定する。

### `get_thread_count(self)`

``[ GENERAL ]`` の ``THREADS`` を返す。

### `set_thread_count(self, value: int, *, auto_write: Optional[bool]=None)`

``[ GENERAL ]`` の ``THREADS`` を設定する。

### `get_angle_constraints(self)`

自由形式 ``[ COS ]`` の結合角（cosine distribution）制約を取得する。

RMC_POT 2023.1 の free-format ``[ COS ]`` に対応する。

### `set_angle_constraint(self, central_type: int, neighbor1: Tuple[int, Union[int, float], Union[int, float]], neighbor2: Tuple[int, Union[int, float], Union[int, float]], *, distribution_type: str='GAUSSIAN', angle_degrees: Optional[Union[int, float]]=None, distribution_width: Optional[Union[int, float]]=None, dcosth: Optional[Union[int, float]]=None, sigma: Union[int, float], sigma_mode: str='normal', index: int=0, auto_write: Optional[bool]=None)`

結合角 ``[ COS ]`` 制約を設定する。

指定 ``index`` が存在すれば置換し、存在しなければ作成する。
事前の初期化は不要で、同じ index への繰り返し実行でも重複しない。

RMC_POT free-format syntax:
    DISTRIB-TYPE
    DISTRIB-DEGREES
    DISTRIB-WIDTH
    DCOSTH
    CENT-TYPE
    NEIGH-TYPE_FROM_TO  (2 行)
    SIGMA / SIGMA-MASTER / SIGMA-SCALABLE

### `remove_angle_constraint(self, index: int, *, auto_write: Optional[bool]=None)`

指定した ``[ COS ]`` 制約を削除する。

### `clear_angle_constraints(self, *, auto_write: Optional[bool]=None)`

すべての ``[ COS ]`` 制約を削除する。

### `get_coord_constraints(self)`

自由形式 ``[ COORD ]`` の通常配位数制約を取得する。

Returns:
    制約ごとの辞書を格納したリスト。各辞書は ``central_type``、
    ``neighbors``、``subconstraints``、``write_cnc_detail`` を含む。

Notes:
    RMC_POT マニュアルの自由形式 ``[ COORD ]`` に従い、1つの制約に
    複数の ``NEIGH-TYPE_FROM_TO`` と複数の
    ``COORDNUM_FRACT_SIGMA`` 系サブ制約を保持できる。

### `add_coord_constraint(self, central_type: int, neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], subconstraints: Sequence[Tuple[int, Union[int, float], Union[int, float]]], *, sigma_mode: str='normal', write_cnc_detail: bool=False, auto_write: Optional[bool]=None)`

【後方互換専用】旧 ``add_coord_constraint()`` API。

このメソッドは旧バージョンのスクリプトをそのまま実行するためだけに残す。
新規コードでは使用せず、``set_coord_constraint(index=...)`` を使用すること。

旧仕様どおり、現在の ``[ COORD ]`` セクション数を新しい ``index`` として
採用し、実際の設定処理は ``set_coord_constraint()`` に委譲する。
したがって COORD の生成・検証・書き込み処理の実体は新API側にのみ存在する。

注意:
    この旧APIは呼ぶたびに末尾へ新しい ``[ COORD ]`` を作る。
    同じ旧スクリプトを既存 dat に対して繰り返し実行すると重複し得る。
    旧式運用で作り直す場合は、事前に ``clear_coord_constraints()`` を
    明示的に呼び出すこと。

### `set_coord_constraint(self, central_type: int, neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], subconstraints: Sequence[Tuple[int, Union[int, float], Union[int, float]]], *, index: int=0, sigma_mode: str='normal', write_cnc_detail: bool=False, auto_write: Optional[bool]=None)`

通常配位数 ``[ COORD ]`` 制約を設定する。

指定 ``index`` の ``[ COORD ]`` が存在すればその内容を置き換え、
存在しなければ必要な位置まで ``[ COORD ]`` を追加して設定する。
事前の初期化処理は不要で、同じ ``index`` に対して繰り返し実行しても
制約は重複しない。

Args:
    central_type: 中心原子の RMC タイプ番号。
    neighbors: ``(atom_type, minimum, maximum)`` の列。距離単位は Å。
    subconstraints: ``(coordination_number, fraction, sigma)`` の列。
        同じ中心/近接定義に複数の目標配位数を与える場合は、
        1つの ``[ COORD ]`` 内に複数指定する。
    index: 設定対象の ``[ COORD ]`` セクション番号。既定値は 0。
    sigma_mode: ``normal``、``master``、``scalable`` のいずれか。
    write_cnc_detail: ``WRITE-CNC-DETAIL = 1`` を出力するか。
    auto_write: 更新後に ``*.dat`` を保存するか。

Returns:
    設定した ``[ COORD ]`` セクションの 0 始まりインデックス。

### `remove_coord_constraint(self, index: int, *, auto_write: Optional[bool]=None)`

指定した通常配位数 ``[ COORD ]`` 制約を削除する。

### `clear_coord_constraints(self, *, auto_write: Optional[bool]=None)`

すべての通常配位数 ``[ COORD ]`` 制約を削除する。

### `get_qn_constraints(self)`

自由形式 ``[ SNC ]`` の Qn 制約を取得する。

Returns:
    Qn 制約ごとの辞書を格納したリスト。各辞書は次を含む。

    - ``central_type``: 中心原子の RMC タイプ番号
    - ``first_neighbor_type``: 第一近接原子の RMC タイプ番号
    - ``first_neighbor_range``: 第一近接距離範囲 ``(min, max)`` [Å]
    - ``second_neighbors``: 第二近接タイプと距離範囲のリスト
    - ``coordination_number``: 目標 Qn の n
    - ``fraction``: 制約を満たす中心原子の目標割合
    - ``sigma``: 重みパラメータ
    - ``sigma_mode``: ``normal``、``master``、``scalable``

Raises:
    ValueError: 必須キーワードが欠落している場合、または値の個数が
        マニュアルの ``[ SNC ]`` 形式と一致しない場合。

Notes:
    Qn 制約は第二近接制約である。中心タイプ ``i`` が第一近接タイプ
    ``j`` を n 個持ち、各第一近接を介して指定タイプの第二近接が
    存在する状態を、指定割合の中心原子へ課す。

### `remove_qn_constraint(self, index: int, *, auto_write: Optional[bool]=None)`

指定した Qn 第二近接制約を削除する。

Args:
    index: 削除対象の ``[ SNC ]`` セクション番号。
    auto_write: 更新後に保存するかどうか。

### `add_qn_constraint(self, central_type: int, first_neighbor_type: int, first_neighbor_minimum: Union[int, float], first_neighbor_maximum: Union[int, float], second_neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], coordination_number: int, fraction: Union[int, float], sigma: Union[int, float], *, sigma_mode: str='normal', auto_write: Optional[bool]=None)`

【後方互換専用】旧 ``add_qn_constraint()`` API。

このメソッドは旧バージョンのスクリプトをそのまま実行するためだけに残す。
新規コードでは使用せず、``set_qn_constraint(index=...)`` を使用すること。

旧仕様どおり、現在の ``[ SNC ]`` セクション数を新しい ``index`` として
採用し、実際の設定処理は ``set_qn_constraint()`` に委譲する。
SNC の生成・検証・書き込み処理の実体は新API側にのみ存在する。

注意:
    この旧APIは呼ぶたびに末尾へ新しい ``[ SNC ]`` を作る。
    同じ旧スクリプトを既存 dat に対して繰り返し実行すると重複し得る。
    旧式運用では、従来どおり事前に ``initialize_qn_constraints()`` を
    呼び出してから ``add_qn_constraint()`` を使用すること。

### `set_qn_constraint(self, central_type: int, first_neighbor_type: int, first_neighbor_minimum: Union[int, float], first_neighbor_maximum: Union[int, float], second_neighbors: Sequence[Tuple[int, Union[int, float], Union[int, float]]], coordination_number: int, fraction: Union[int, float], sigma: Union[int, float], *, index: int=0, sigma_mode: str='normal', auto_write: Optional[bool]=None)`

Qn / ``[ SNC ]`` 制約を指定 index に設定する。

``index`` は複数存在できる ``[ SNC ]`` のどのセクションを操作するかを
指定する。指定 index が存在すれば、そのセクションの内容だけを今回の
指定値で置き換える。存在しなければ、必要な位置まで ``[ SNC ]`` を
作成して設定する。

同じ index に同じ設定を繰り返してもセクション数は増えない。
他 index の ``[ SNC ]`` には触れない。

### `clear_qn_constraints(self, *, auto_write: Optional[bool]=None)`

すべての ``[ SNC ]`` を明示的に削除する。

通常の設定更新には使用しない。既存 ``[ SNC ]`` を意図的に全削除する
場合だけ呼び出す。

### `get_bvs_constraints(self)`

自由形式 ``[ BVS ]`` の bond valence sum 制約を取得する。

RMC_POT 2023.1 の ``[ BVS ]`` に対応する。BVS は
``_ADVANCED_GEOM_CONST`` 付き実行バイナリかつ自由形式 ``*.dat`` でのみ
使用できる。

### `set_bvs_constraint(self, central_type: int, neighbors: Sequence[Tuple[int, Union[int, float], Optional[Union[int, float]], Optional[Union[int, float]], Optional[int]]], valence: Union[int, float], sigma: Union[int, float], *, central_charge: Optional[int]=None, sigma_mode: str='normal', index: int=0, auto_write: Optional[bool]=None)`

Bond Valence Sum ``[ BVS ]`` 制約を設定する。

Args:
    central_type: 中心原子の RMC type (1 始まり)。
    neighbors: 各近接原子について
        ``(atom_type, rmax, r0, b, charge)`` を指定する。
        ``r0`` / ``b`` に ``None`` を指定した場合は RMC_POT の既定値を
        使用するため ``-1`` を出力する。既定 ``R0`` を使う場合は
        酸化数判定のため ``central_charge`` と neighbour ``charge`` が必要。
    valence: 中心原子に期待する bond valence sum。
    sigma: BVS の重みパラメータ。
    central_charge: 中心原子の形式電荷。既定 R0/B を使う場合に必要。
    sigma_mode: ``normal`` / ``master`` / ``scalable``。
    index: 複数 ``[ BVS ]`` の 0 始まり index。
    auto_write: 更新後に保存するか。

Notes:
    BVS は atomic system 用で、localized bond を持つ FNC / BPOT とは
    併用しない。非結合 pair potential はマニュアル上併用可能。

### `remove_bvs_constraint(self, index: int, *, auto_write: Optional[bool]=None)`

指定 ``[ BVS ]`` 制約を削除する。

### `clear_bvs_constraints(self, *, auto_write: Optional[bool]=None)`

すべての ``[ BVS ]`` 制約を削除する。

### `get_pair_potential_settings(self)`

``[ NBPOT ] NB-TYPE = TABULATED`` の pair potential 設定を取得する。

### `set_pair_potential(self, partials: Sequence[Tuple[int, str, Union[int, float, str], str]], *, cutoff: Optional[Union[int, float]]=None, temperature: Union[int, float]=298.0, auto_write: Optional[bool]=None)`

距離依存の tabulated pair potential を ``[ NBPOT ]`` に設定する。

Args:
    partials: ``(partial_index, filename, sigma, sigma_mode)`` の列。
        ``partial_index`` は RMC partial の 1 始まり index。
        ``sigma_mode`` は ``normal`` / ``master`` / ``scalable``。
        ``sigma`` は数値、または potential 用の ``m`` / ``s`` / ``ms``
        prefix を含む文字列（例: ``"ms0.5"``）を指定できる。
    cutoff: tabulated potential cutoff [Å]。省略時は RMC_POT 既定値。
    temperature: K。マニュアル上、U/kT 表示用でアルゴリズム上の意味はない。
    auto_write: 更新後に保存するか。

Notes:
    RMC_POT の tabulated potential は atomic system 向けで、FNC=1..3 と
    併用できない。flexible molecule (BPOT) との併用はマニュアルで
    強く非推奨のため、この API では拒否する。ANN potential とは併用しない。

### `clear_pair_potential(self, *, auto_write: Optional[bool]=None)`

TABULATED ``[ NBPOT ]`` pair potential を削除する。

### `write_pair_potential_file(cls, filename: Union[str, Path], points: Sequence[Tuple[Union[int, float], Union[int, float]]], *, comment: str='')`

RMC_POT tabulated potential ファイルを作成する。

``r [Å] - U(r) [kJ]`` を等間隔 r で出力する。1 行目は点数、2 行目は
コメント、3 行目以降は ``r U(r)`` とする。

### `get_cos_constraints(self)`

``get_angle_constraints()`` の RMC_POT ``COS`` 名 alias。

### `set_cos_constraint(self, *args: Any, **kwargs: Any)`

``set_angle_constraint()`` の RMC_POT ``COS`` 名 alias。

### `get_snc_constraints(self)`

``get_qn_constraints()`` の RMC_POT ``SNC`` 名 alias。

### `set_snc_constraint(self, *args: Any, **kwargs: Any)`

``set_qn_constraint()`` の RMC_POT ``SNC`` 名 alias。

### `get_lj_potential(self)`

``[ NBPOT ]`` の Lennard-Jones 非結合ポテンシャル設定を返す。

### `set_lj_potential(self, ngr_types: int, lj_sigma: Sequence[Union[int, float]], lj_epsilon: Sequence[Union[int, float]], *, cutoff_vdw: Union[int, float]=1.0, cutoff_coul: Optional[Union[int, float]]=None, vdw_sigma: Union[int, float, str]=1.0, coul_sigma: Optional[Union[int, float, str]]=None, lj_power: int=12, scale_14_vdw: Union[int, float]=1.0, scale_14_coul: Optional[Union[int, float]]=None, chi_lowlimit_ratio: Optional[Union[int, float]]=None, auto_write: Optional[bool]=None)`

マニュアルの ``[ NBPOT ] / NB-TYPE=LJ`` を設定する。

### `get_custom_move(self)`

``[ CUSTMOVE ]`` の分子 move 設定を返す。

### `set_custom_move(self, nmoved_atoms: int, custom_lines: Sequence[Union[str, int, float]], *, auto_write: Optional[bool]=None)`

マニュアルの ``[ CUSTMOVE ]`` を設定する。

### `get_local_invariance(self)`

``[ LOCINV ]`` をマニュアルの区間表現のまま返す。

### `set_local_invariance(self, mode: str, intervals: Sequence[Tuple[Union[int, float], Union[int, float, str], str]], *, r_spacing: Optional[Union[int, float]]=None, end: Optional[Union[int, float]]=None, auto_write: Optional[bool]=None)`

マニュアルの ``[ LOCINV ]`` を設定する。

intervals は ``(開始値, sigma, sigma_mode)``。sigma_mode は
``normal`` / ``master`` / ``scalable``。

### `get_non_periodic(self)`

``[ NOPER ]`` の sample radius と recentre flag を返す。

### `set_non_periodic(self, sample_radius: Union[int, float], *, recentre: bool=False, auto_write: Optional[bool]=None)`

マニュアルの ``[ NOPER ]`` を設定する。

### `get_vibrational_amplitudes(self)`

``[ VIBRAMP ] / GAUSSIAN-SIGMA`` を返す。

### `set_vibrational_amplitudes(self, sigma_values: Sequence[Union[int, float]], *, auto_write: Optional[bool]=None)`

マニュアルの ``[ VIBRAMP ]`` を設定する。

### `get_common_neighbor_constraints(self)`

advanced geometric constraint の ``[ CONC ]`` を返す。

### `set_common_neighbor_constraint(self, index: int, primary_type1: int, primary_type2: int, primary_minimum: Union[int, float], primary_maximum: Union[int, float], secondary: Sequence[Tuple[int, Union[int, float], Union[int, float], Union[int, float], Union[int, float]]], coordination_number: int, fraction: Union[int, float], sigma: Union[int, float, str], *, sigma_mode: str='normal', auto_write: Optional[bool]=None)`

マニュアルの advanced ``[ CONC ]`` を1件設定する。

### `get_ann_potential_settings(self)`

``get_aenet_settings()`` の ANN 名 alias。

### `set_ann_potential(self, *args: Any, **kwargs: Any)`

``set_aenet_potential()`` の ANN 名 alias。

### `get_aenet_settings(self)`

自由形式 ``[ AENET ]`` の ANN ポテンシャル設定を取得する。

Returns:
    ``[ AENET ]`` が存在しない場合は ``None``。存在する場合は、
    potential ファイル、cutoff、原子別エネルギー出力、計算間隔、
    sigma 指定を格納した辞書。

Raises:
    ValueError: 必須 ``IND_ANN-FILE_TYPE-NAME`` または sigma 指定が
        欠落している場合。

### `set_aenet_potential(self, potentials: Sequence[Tuple[int, str, Optional[str]]], sigma: Union[int, float], *, sigma_mode: str='normal', cutoff: Optional[Union[int, float]]=None, write_atomic_energy: bool=False, aenet_step: int=5, auto_write: Optional[bool]=None)`

AENET の ANN ポテンシャル設定を作成または置換する。

Args:
    potentials: 原子タイプごとの
        ``(atom_type, filename, type_name)``。
        ``type_name`` を省略する場合は ``None`` を指定する。
    sigma: ANN potential の chi-square 寄与を重み付けする sigma。
    sigma_mode: ``normal``、``master``、``scalable`` のいずれか。
    cutoff: ANN potential の cutoff [Å]。``None`` の場合は
        potential ファイルに格納された値を使用する。
    write_atomic_energy: 個々の原子エネルギーを ``*.en`` へ出力するか。
    aenet_step: ANN potential を再計算するシミュレーション間隔。
        マニュアル記載の既定値は 5。
    auto_write: 更新後に保存するかどうか。

Raises:
    ValueError: potential 指定が空、値が不正、または AENET と共存不可の
        セクションが存在する場合。

Notes:
    ``IND_ANN-FILE_TYPE-NAME`` は原子タイプごとに複数行出力する。
    ``type_name`` を ``None`` にした場合、RMC_POT は
    ``[ GENERAL ]`` の ``CHEMICAL-SYMBOLS`` から元素記号を抽出する。

### `add_aenet_potential_file(self, atom_type: int, filename: str, type_name: Optional[str]=None, *, auto_write: Optional[bool]=None)`

既存の ``[ AENET ]`` へ原子タイプ別 potential ファイルを追加する。

Args:
    atom_type: 1 始まりの RMC 原子タイプ番号。
    filename: AENET で学習済みの ANN potential ファイル名。
    type_name: AENET へ渡す原子タイプ名または元素記号。
        ``None`` の場合は ``CHEMICAL-SYMBOLS`` から抽出させる。
    auto_write: 更新後に保存するかどうか。

Raises:
    ValueError: ``[ AENET ]`` が未設定、原子タイプが重複、
        または値が不正な場合。

### `remove_aenet_potential_file(self, atom_type: int, *, auto_write: Optional[bool]=None)`

指定原子タイプの AENET potential ファイル設定を削除する。

Args:
    atom_type: 削除する RMC 原子タイプ番号。
    auto_write: 更新後に保存するかどうか。

Raises:
    ValueError: ``[ AENET ]`` が未設定、対象原子タイプが存在しない、
        または削除により必須設定が空になる場合。

### `clear_aenet_potential(self, *, auto_write: Optional[bool]=None)`

``[ AENET ]`` セクションと ANN potential 設定を削除する。

Args:
    auto_write: 更新後に保存するかどうか。

## `main()`

自由形式 DAT と SNC セクションを設定する利用例。

Notes:
    SNC は独立ファイルではなく、自由形式 DAT 内の ``[ SNC ]``
    セクションとして従来の ``RmcPotDatFree`` が管理する。


## 実装に基づく API 一覧

この一覧は提供された `rmc_pot_dat_free(20261116-081310).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `RmcPotDatFree` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 77 | 自由形式 RMC_POT 入力ファイル編集クラスを初期化する。 |
| `create_dat_file()` | 174 | 自由形式の初期 \`\`*.dat\`\` ファイルを作成する。 |
| `load()` | 255 | 現在の \`\`cfg_name\`\` に対応する自由形式ファイルを読み込む。 |
| `write()` | 313 | 保持している自由形式データを \`\`*.dat\`\` へ書き出す。 |
| `set()` | 516 | 自由形式の指定キーを単一値で設定する。 |
| `add()` | 536 | 自由形式の指定キーへ値を追加する。 |
| `get()` | 555 | 自由形式の指定キーから最初の値を取得する。 |
| `get_all()` | 577 | 自由形式の指定キーに登録された全値を取得する。 |
| `initialize_sections()` | 597 | 指定名のセクションをすべて削除して未設定状態へ戻す。 |
| `initialize_qn_constraints()` | 637 | 【後方互換専用】旧 Qn/SNC 初期化API。 |
| `add_section()` | 652 | 空の自由形式セクションを末尾へ追加する。 |
| `remove_section()` | 670 | 指定位置の自由形式セクションを削除する。 |
| `remove()` | 689 | 指定セクションからキーと全値を削除する。 |
| `section_count()` | 705 | 指定名の自由形式セクション数を返す。 |
| `set_cfg_name()` | 716 | 読み書き対象の構成名を変更する。 |
| `set_element_info()` | 728 | 原子タイプ順の元素記号を設定する。 |
| `get_comment()` | 827 | \`\`[ GENERAL ]\`\` の \`\`TITLE\`\` を返す。 |
| `set_comment()` | 831 | \`\`[ GENERAL ]\`\` の \`\`TITLE\`\` を設定する。 |
| `get_density()` | 844 | \`\`[ GENERAL ]\`\` の \`\`NDENS\`\` を返す。 |
| `set_density()` | 858 | \`\`[ GENERAL ]\`\` の \`\`NDENS\`\` を設定する。 |
| `get_cutoffs()` | 871 | \`\`[ GENERAL ]\`\` の \`\`CUT-OFF\`\` を RMC 順で返す。 |
| `set_cutoffs()` | 893 | \`\`[ GENERAL ]\`\` の \`\`CUT-OFF\`\` を設定する。 |
| `get_max_moves()` | 914 | \`\`[ GENERAL ]\`\` の \`\`MAX-MOVES\`\` を返す。 |
| `set_maximum_moves()` | 925 | \`\`[ GENERAL ]\`\` の \`\`MAX-MOVES\`\` を設定する。 |
| `get_r_spacing()` | 938 | \`\`[ GENERAL ]\`\` の \`\`R-SPACING\`\` を返す。 |
| `set_r_spacing()` | 943 | \`\`[ GENERAL ]\`\` の \`\`R-SPACING\`\` を設定する。 |
| `get_moveout_option()` | 952 | \`\`[ GENERAL ]\`\` の \`\`MOVEOUT\`\` を返す。 |
| `set_moveout_option()` | 957 | \`\`[ GENERAL ]\`\` の \`\`MOVEOUT\`\` を設定する。 |
| `get_num_config_to_collect()` | 966 | \`\`[ GENERAL ]\`\` の \`\`COLL-NUMBER\`\` を返す。 |
| `set_num_config_to_collect()` | 971 | \`\`[ GENERAL ]\`\` の \`\`COLL-NUMBER\`\` を設定する。 |
| `get_print_interval()` | 982 | \`\`[ GENERAL ]\`\` の \`\`PRINT-STEP\`\` を返す。 |
| `set_print_interval()` | 987 | \`\`[ GENERAL ]\`\` の \`\`PRINT-STEP\`\` を設定する。 |
| `get_time_and_save()` | 998 | \`\`[ GENERAL ]\`\` の \`\`RUN-TIME\`\` と \`\`SAVE-TIME\`\` を返す。 |
| `set_time_and_save()` | 1004 | \`\`[ GENERAL ]\`\` の \`\`RUN-TIME\`\` と \`\`SAVE-TIME\`\` を設定する。 |
| `get_data_flags()` | 1021 | \`\`[ EXP ]\`\` の \`\`TYPE\`\` からデータ種別ごとの件数を返す。 |
| `set_data_flags()` | 1028 | 指定されたデータ種別の \`\`[ EXP ]\`\` セクションを残す。 |
| `get_exp_filename()` | 1071 | 最初の [ EXP ] セクションに設定された実験データファイル名を取得します。 |
| `set_exp_filename()` | 1112 | 最初の \`\`[ EXP ]\`\` の \`\`DATAFILE\`\` を設定する。 |
| `get_exp_range()` | 1127 | 最初の \`\`[ EXP ]\`\` の \`\`POINT-RANGE\`\` を返す。 |
| `set_exp_range()` | 1151 | 最初の \`\`[ EXP ]\`\` の \`\`POINT-RANGE\`\` を設定する。 |
| `get_scale_factor()` | 1170 | 固定形式13行目に対応する \`\`CONST-SUBTRACT\`\` を返す。 |
| `set_scale_factor()` | 1184 | 固定形式13行目に対応する \`\`CONST-SUBTRACT\`\` を設定する。 |
| `get_sigma_factor()` | 1197 | 最初の \`\`[ EXP ]\`\` の \`\`SIGMA\`\` を返す。 |
| `set_sigma_factor()` | 1211 | 最初の \`\`[ EXP ]\`\` の \`\`SIGMA\`\` を設定する。 |
| `get_flag_15()` | 1261 | 固定形式15行目に対応する \`\`RENORM\`\` を返す。 |
| `set_flag_15()` | 1269 | 固定形式15行目に対応する \`\`RENORM\`\` を設定する。 |
| `get_flag_16()` | 1280 | 固定形式16行目に対応する定数項補正フラグを返す。 |
| `set_flag_16()` | 1284 | 固定形式16行目に対応する定数項補正フラグを設定する。 |
| `get_flag_17()` | 1288 | 固定形式17行目に対応する一次項補正フラグを返す。 |
| `set_flag_17()` | 1292 | 固定形式17行目に対応する一次項補正フラグを設定する。 |
| `get_flag_18()` | 1296 | 固定形式18行目に対応する二次項補正フラグを返す。 |
| `set_flag_18()` | 1300 | 固定形式18行目に対応する二次項補正フラグを設定する。 |
| `get_angle_constraint_count()` | 1304 | \`\`[ COS ]\`\` セクション数を返す。 |
| `set_angle_constraint_count()` | 1308 | 固定形式互換で角度制約数を設定する。 |
| `get_coord_constraint_count()` | 1335 | \`\`[ COORD ]\`\` セクション数を返す。 |
| `set_coord_constraint_count()` | 1339 | 固定形式互換で配位数制約数を設定する。 |
| `get_avg_coord_constraint_count()` | 1366 | \`\`[ AVCOORD ]\`\` セクション数を返す。 |
| `set_avg_coord_constraint_count()` | 1370 | 固定形式互換で平均配位数制約数を設定する。 |
| `get_potential_flag()` | 1399 | potential セクションが存在する場合に \`\`1\`\`、なければ \`\`0\`\` を返す。 |
| `set_potential_flag()` | 1406 | 固定形式互換でpotentialの無効化または既存状態の確認を行う。 |
| `get_fnc_switch()` | 1435 | FNC または \`\`[ BPOT ]\`\` の状態を数値で取得する。 |
| `get_fnc_options()` | 1471 | FNC / topology option を取得する。 |
| `set_fnc_switch()` | 1534 | FNC または topology mode を設定する。 |
| `validate_mode_configuration()` | 1614 | 自由形式の mode 指定と入力ファイルを検証する。 |
| `get_fnc_distance_ranges()` | 1714 | FNC ファイルの constraint type ごとの rmin/rmax を取得する。 |
| `set_fnc_distance_ranges()` | 1765 | FNC ファイルの constraint type ごとの rmin/rmax を更新する。 |
| `get_initial_bin_shift()` | 1836 | \`\`[ GENERAL ]\`\` の \`\`BIN-SHIFT\`\` を返す。 |
| `set_initial_bin_shift()` | 1841 | \`\`[ GENERAL ]\`\` の \`\`BIN-SHIFT\`\` を設定する。 |
| `get_xmax_used()` | 1849 | \`\`[ GENERAL ]\`\` の \`\`XMAX-FACTOR\`\` を返す。 |
| `set_xmax_used()` | 1854 | \`\`[ GENERAL ]\`\` の \`\`XMAX-FACTOR\`\` を設定する。 |
| `get_num_atoms_per_move()` | 1860 | 1回の move で動かす原子数を返す。 |
| `set_num_atoms_per_move()` | 1872 | 1回の custom move で動かす原子数を設定する。 |
| `get_history_buffer_size()` | 1896 | \`\`[ GENERAL ]\`\` の \`\`HST_BUFFSIZE\`\` を返す。 |
| `set_history_buffer_size()` | 1901 | \`\`[ GENERAL ]\`\` の \`\`HST_BUFFSIZE\`\` を設定する。 |
| `get_display_update_interval()` | 1909 | \`\`[ GENERAL ]\`\` の \`\`HST-STEP-FACTOR\`\` を返す。 |
| `set_display_update_interval()` | 1914 | \`\`[ GENERAL ]\`\` の \`\`HST-STEP-FACTOR\`\` を設定する。 |
| `get_custom_move_flag()` | 1922 | \`\`[ CUSTMOVE ]\`\` が存在する場合に1、存在しない場合に0を返す。 |
| `set_custom_move_flag()` | 1928 | custom move の有効・無効を \`\`[ CUSTMOVE ]\`\` の有無で設定する。 |
| `get_load_histogram_flag()` | 1956 | \`\`[ GENERAL ]\`\` の \`\`RELOAD\`\` を返す。 |
| `set_load_histogram_flag()` | 1961 | \`\`[ GENERAL ]\`\` の \`\`RELOAD\`\` を設定する。 |
| `get_max_atoms_per_cell()` | 1969 | \`\`[ GENERAL ]\`\` の \`\`ATOMS-IN-GRIDCELL\`\` を返す。 |
| `set_max_atoms_per_cell()` | 1974 | \`\`[ GENERAL ]\`\` の \`\`ATOMS-IN-GRIDCELL\`\` を設定する。 |
| `get_swap_settings()` | 1986 | \`\`[ SWAP ]\`\` の交換割合と有効状態を返す。 |
| `set_swap_settings()` | 1999 | 固定形式互換のswap設定を自由形式の \`\`[ SWAP ]\`\` へ反映する。 |
| `get_thread_count()` | 2028 | \`\`[ GENERAL ]\`\` の \`\`THREADS\`\` を返す。 |
| `set_thread_count()` | 2033 | \`\`[ GENERAL ]\`\` の \`\`THREADS\`\` を設定する。 |
| `get_angle_constraints()` | 2169 | 自由形式 \`\`[ COS ]\`\` の結合角（cosine distribution）制約を取得する。 |
| `set_angle_constraint()` | 2282 | 結合角 \`\`[ COS ]\`\` 制約を設定する。 |
| `remove_angle_constraint()` | 2415 | 指定した \`\`[ COS ]\`\` 制約を削除する。 |
| `clear_angle_constraints()` | 2427 | すべての \`\`[ COS ]\`\` 制約を削除する。 |
| `get_coord_constraints()` | 2440 | 自由形式 \`\`[ COORD ]\`\` の通常配位数制約を取得する。 |
| `add_coord_constraint()` | 2530 | 【後方互換専用】旧 \`\`add_coord_constraint()\`\` API。 |
| `set_coord_constraint()` | 2566 | 通常配位数 \`\`[ COORD ]\`\` 制約を設定する。 |
| `remove_coord_constraint()` | 2680 | 指定した通常配位数 \`\`[ COORD ]\`\` 制約を削除する。 |
| `clear_coord_constraints()` | 2692 | すべての通常配位数 \`\`[ COORD ]\`\` 制約を削除する。 |
| `get_qn_constraints()` | 2705 | 自由形式 \`\`[ SNC ]\`\` の Qn 制約を取得する。 |
| `remove_qn_constraint()` | 2823 | 指定した Qn 第二近接制約を削除する。 |
| `add_qn_constraint()` | 2840 | 【後方互換専用】旧 \`\`add_qn_constraint()\`\` API。 |
| `set_qn_constraint()` | 2884 | Qn / \`\`[ SNC ]\`\` 制約を指定 index に設定する。 |
| `clear_qn_constraints()` | 3003 | すべての \`\`[ SNC ]\`\` を明示的に削除する。 |
| `get_bvs_constraints()` | 3018 | 自由形式 \`\`[ BVS ]\`\` の bond valence sum 制約を取得する。 |
| `set_bvs_constraint()` | 3109 | Bond Valence Sum \`\`[ BVS ]\`\` 制約を設定する。 |
| `remove_bvs_constraint()` | 3252 | 指定 \`\`[ BVS ]\`\` 制約を削除する。 |
| `clear_bvs_constraints()` | 3263 | すべての \`\`[ BVS ]\`\` 制約を削除する。 |
| `get_pair_potential_settings()` | 3271 | \`\`[ NBPOT ] NB-TYPE = TABULATED\`\` の pair potential 設定を取得する。 |
| `set_pair_potential()` | 3338 | 距離依存の tabulated pair potential を \`\`[ NBPOT ]\`\` に設定する。 |
| `clear_pair_potential()` | 3449 | TABULATED \`\`[ NBPOT ]\`\` pair potential を削除する。 |
| `write_pair_potential_file()` | 3470 | RMC_POT tabulated potential ファイルを作成する。 |
| `get_cos_constraints()` | 3505 | \`\`get_angle_constraints()\`\` の RMC_POT \`\`COS\`\` 名 alias。 |
| `set_cos_constraint()` | 3509 | \`\`set_angle_constraint()\`\` の RMC_POT \`\`COS\`\` 名 alias。 |
| `get_snc_constraints()` | 3513 | \`\`get_qn_constraints()\`\` の RMC_POT \`\`SNC\`\` 名 alias。 |
| `set_snc_constraint()` | 3517 | \`\`set_qn_constraint()\`\` の RMC_POT \`\`SNC\`\` 名 alias。 |
| `get_lj_potential()` | 3521 | \`\`[ NBPOT ]\`\` の Lennard-Jones 非結合ポテンシャル設定を返す。 |
| `set_lj_potential()` | 3535 | マニュアルの \`\`[ NBPOT ] / NB-TYPE=LJ\`\` を設定する。 |
| `get_custom_move()` | 3593 | \`\`[ CUSTMOVE ]\`\` の分子 move 設定を返す。 |
| `set_custom_move()` | 3603 | マニュアルの \`\`[ CUSTMOVE ]\`\` を設定する。 |
| `get_local_invariance()` | 3625 | \`\`[ LOCINV ]\`\` をマニュアルの区間表現のまま返す。 |
| `set_local_invariance()` | 3646 | マニュアルの \`\`[ LOCINV ]\`\` を設定する。 |
| `get_non_periodic()` | 3685 | \`\`[ NOPER ]\`\` の sample radius と recentre flag を返す。 |
| `set_non_periodic()` | 3695 | マニュアルの \`\`[ NOPER ]\`\` を設定する。 |
| `get_vibrational_amplitudes()` | 3714 | \`\`[ VIBRAMP ] / GAUSSIAN-SIGMA\`\` を返す。 |
| `set_vibrational_amplitudes()` | 3724 | マニュアルの \`\`[ VIBRAMP ]\`\` を設定する。 |
| `get_common_neighbor_constraints()` | 3740 | advanced geometric constraint の \`\`[ CONC ]\`\` を返す。 |
| `set_common_neighbor_constraint()` | 3750 | マニュアルの advanced \`\`[ CONC ]\`\` を1件設定する。 |
| `get_ann_potential_settings()` | 3798 | \`\`get_aenet_settings()\`\` の ANN 名 alias。 |
| `set_ann_potential()` | 3802 | \`\`set_aenet_potential()\`\` の ANN 名 alias。 |
| `get_aenet_settings()` | 3835 | 自由形式 \`\`[ AENET ]\`\` の ANN ポテンシャル設定を取得する。 |
| `set_aenet_potential()` | 3923 | AENET の ANN ポテンシャル設定を作成または置換する。 |
| `add_aenet_potential_file()` | 4038 | 既存の \`\`[ AENET ]\`\` へ原子タイプ別 potential ファイルを追加する。 |
| `remove_aenet_potential_file()` | 4100 | 指定原子タイプの AENET potential ファイル設定を削除する。 |
| `clear_aenet_potential()` | 4150 | \`\`[ AENET ]\`\` セクションと ANN potential 設定を削除する。 |

### モジュール関数 `main()`

- 定義位置：4172 行
- 説明：自由形式 DAT と SNC セクションを設定する利用例。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `RmcPotDatFree.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `config` | `Optional[Config]` |
| `logger` | `Optional[XLogger]` |
| `cfg_name` | `Optional[str]` |
| `auto_write` | `bool` |
| `version` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:77`。

### `RmcPotDatFree.create_dat_file`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `basename` | `str` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:174`。

### `RmcPotDatFree.load`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:255`。

### `RmcPotDatFree.write`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `out_name` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:313`。

### `RmcPotDatFree.set`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `key` | `str` |
| `value` | `Any` |
| `index` | `int` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:516`。

### `RmcPotDatFree.add`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `key` | `str` |
| `value` | `Any` |
| `index` | `int` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:536`。

### `RmcPotDatFree.get`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `key` | `str` |
| `index` | `int` |
| `default` | `Optional[str]` |

戻り値の型注釈: `Optional[str]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:555`。

### `RmcPotDatFree.get_all`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `key` | `str` |
| `index` | `int` |

戻り値の型注釈: `List[str]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:577`。

### `RmcPotDatFree.initialize_sections`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:597`。

### `RmcPotDatFree.initialize_qn_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:637`。

### `RmcPotDatFree.add_section`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:652`。

### `RmcPotDatFree.remove_section`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `index` | `int` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:670`。

### `RmcPotDatFree.remove`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |
| `key` | `str` |
| `index` | `int` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:689`。

### `RmcPotDatFree.section_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section` | `str` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:705`。

### `RmcPotDatFree.set_cfg_name`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `cfg_name` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:716`。

### `RmcPotDatFree.set_element_info`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `element_info` | `Sequence[str]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:728`。

### `RmcPotDatFree.get_comment`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `str`。定義位置: `rmc_pot_dat_free(20261116-081310).py:827`。

### `RmcPotDatFree.set_comment`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `comment` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:831`。

### `RmcPotDatFree.get_density`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Union[float, bool]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:844`。

### `RmcPotDatFree.set_density`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `rho` | `Union[int, float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:858`。

### `RmcPotDatFree.get_cutoffs`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Union[int, float, str]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:871`。

### `RmcPotDatFree.set_cutoffs`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `values` | `Union[str, Sequence[Union[int, float]]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:893`。

### `RmcPotDatFree.get_max_moves`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[float]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:914`。

### `RmcPotDatFree.set_maximum_moves`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `values` | `Sequence[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:925`。

### `RmcPotDatFree.get_r_spacing`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_free(20261116-081310).py:938`。

### `RmcPotDatFree.set_r_spacing`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `dr` | `Union[int, float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:943`。

### `RmcPotDatFree.get_moveout_option`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:952`。

### `RmcPotDatFree.set_moveout_option`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `use_moveout` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:957`。

### `RmcPotDatFree.get_num_config_to_collect`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:966`。

### `RmcPotDatFree.set_num_config_to_collect`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `num_config` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:971`。

### `RmcPotDatFree.get_print_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:982`。

### `RmcPotDatFree.set_print_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `interval_step` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:987`。

### `RmcPotDatFree.get_time_and_save`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[float, int]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:998`。

### `RmcPotDatFree.set_time_and_save`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `time_limit_min` | `float` |
| `save_interval_step` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1004`。

### `RmcPotDatFree.get_data_flags`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[int, int, int, int]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1021`。

### `RmcPotDatFree.set_data_flags`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `flags` | `Sequence[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1028`。

### `RmcPotDatFree.get_exp_filename`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Union[str, bool]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1071`。

### `RmcPotDatFree.set_exp_filename`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `path` | `Union[str, Path]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1112`。

### `RmcPotDatFree.get_exp_range`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Union[Tuple[int, int], bool]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1127`。

### `RmcPotDatFree.set_exp_range`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `start` | `int` |
| `end` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1151`。

### `RmcPotDatFree.get_scale_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Union[float, bool]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1170`。

### `RmcPotDatFree.set_scale_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1184`。

### `RmcPotDatFree.get_sigma_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Union[float, bool]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1197`。

### `RmcPotDatFree.set_sigma_factor`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `sigma` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1211`。

### `RmcPotDatFree.get_flag_15`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1261`。

### `RmcPotDatFree.set_flag_15`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1269`。

### `RmcPotDatFree.get_flag_16`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1280`。

### `RmcPotDatFree.set_flag_16`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1284`。

### `RmcPotDatFree.get_flag_17`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1288`。

### `RmcPotDatFree.set_flag_17`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1292`。

### `RmcPotDatFree.get_flag_18`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1296`。

### `RmcPotDatFree.set_flag_18`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1300`。

### `RmcPotDatFree.get_angle_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1304`。

### `RmcPotDatFree.set_angle_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1308`。

### `RmcPotDatFree.get_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1335`。

### `RmcPotDatFree.set_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1339`。

### `RmcPotDatFree.get_avg_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1366`。

### `RmcPotDatFree.set_avg_coord_constraint_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1370`。

### `RmcPotDatFree.get_potential_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1399`。

### `RmcPotDatFree.set_potential_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1406`。

### `RmcPotDatFree.get_fnc_switch`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1435`。

### `RmcPotDatFree.get_fnc_options`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[str]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1471`。

### `RmcPotDatFree.set_fnc_switch`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `Union[bool, int]` |
| `opt` | `Optional[Union[str, Sequence[str]]]` |
| `keep_existing_opt` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1534`。

### `RmcPotDatFree.validate_mode_configuration`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `check_input_files` | `bool` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1614`。

### `RmcPotDatFree.get_fnc_distance_ranges`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `fnc_name` | `Optional[str]` |

戻り値の型注釈: `Dict[int, Tuple[float, float]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1714`。

### `RmcPotDatFree.set_fnc_distance_ranges`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `ranges` | `Dict[int, Tuple[float, float]]` |
| `fnc_name` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1765`。

### `RmcPotDatFree.get_initial_bin_shift`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1836`。

### `RmcPotDatFree.set_initial_bin_shift`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1841`。

### `RmcPotDatFree.get_xmax_used`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `float`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1849`。

### `RmcPotDatFree.set_xmax_used`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1854`。

### `RmcPotDatFree.get_num_atoms_per_move`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1860`。

### `RmcPotDatFree.set_num_atoms_per_move`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1872`。

### `RmcPotDatFree.get_history_buffer_size`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1896`。

### `RmcPotDatFree.set_history_buffer_size`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1901`。

### `RmcPotDatFree.get_display_update_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1909`。

### `RmcPotDatFree.set_display_update_interval`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1914`。

### `RmcPotDatFree.get_custom_move_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1922`。

### `RmcPotDatFree.set_custom_move_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1928`。

### `RmcPotDatFree.get_load_histogram_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1956`。

### `RmcPotDatFree.set_load_histogram_flag`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1961`。

### `RmcPotDatFree.get_max_atoms_per_cell`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1969`。

### `RmcPotDatFree.set_max_atoms_per_cell`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `bool`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1974`。

### `RmcPotDatFree.get_swap_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Tuple[float, int]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1986`。

### `RmcPotDatFree.set_swap_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `fraction` | `float` |
| `allow_flag` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:1999`。

### `RmcPotDatFree.get_thread_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2028`。

### `RmcPotDatFree.set_thread_count`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `value` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2033`。

### `RmcPotDatFree.get_angle_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2169`。

### `RmcPotDatFree.set_angle_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `central_type` | `int` |
| `neighbor1` | `Tuple[int, Union[int, float], Union[int, float]]` |
| `neighbor2` | `Tuple[int, Union[int, float], Union[int, float]]` |
| `distribution_type` | `str` |
| `angle_degrees` | `Optional[Union[int, float]]` |
| `distribution_width` | `Optional[Union[int, float]]` |
| `dcosth` | `Optional[Union[int, float]]` |
| `sigma` | `Union[int, float]` |
| `sigma_mode` | `str` |
| `index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2282`。

### `RmcPotDatFree.remove_angle_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2415`。

### `RmcPotDatFree.clear_angle_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2427`。

### `RmcPotDatFree.get_coord_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2440`。

### `RmcPotDatFree.add_coord_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `central_type` | `int` |
| `neighbors` | `Sequence[Tuple[int, Union[int, float], Union[int, float]]]` |
| `subconstraints` | `Sequence[Tuple[int, Union[int, float], Union[int, float]]]` |
| `sigma_mode` | `str` |
| `write_cnc_detail` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2530`。

### `RmcPotDatFree.set_coord_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `central_type` | `int` |
| `neighbors` | `Sequence[Tuple[int, Union[int, float], Union[int, float]]]` |
| `subconstraints` | `Sequence[Tuple[int, Union[int, float], Union[int, float]]]` |
| `index` | `int` |
| `sigma_mode` | `str` |
| `write_cnc_detail` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2566`。

### `RmcPotDatFree.remove_coord_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2680`。

### `RmcPotDatFree.clear_coord_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2692`。

### `RmcPotDatFree.get_qn_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2705`。

### `RmcPotDatFree.remove_qn_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2823`。

### `RmcPotDatFree.add_qn_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `central_type` | `int` |
| `first_neighbor_type` | `int` |
| `first_neighbor_minimum` | `Union[int, float]` |
| `first_neighbor_maximum` | `Union[int, float]` |
| `second_neighbors` | `Sequence[Tuple[int, Union[int, float], Union[int, float]]]` |
| `coordination_number` | `int` |
| `fraction` | `Union[int, float]` |
| `sigma` | `Union[int, float]` |
| `sigma_mode` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2840`。

### `RmcPotDatFree.set_qn_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `central_type` | `int` |
| `first_neighbor_type` | `int` |
| `first_neighbor_minimum` | `Union[int, float]` |
| `first_neighbor_maximum` | `Union[int, float]` |
| `second_neighbors` | `Sequence[Tuple[int, Union[int, float], Union[int, float]]]` |
| `coordination_number` | `int` |
| `fraction` | `Union[int, float]` |
| `sigma` | `Union[int, float]` |
| `index` | `int` |
| `sigma_mode` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:2884`。

### `RmcPotDatFree.clear_qn_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3003`。

### `RmcPotDatFree.get_bvs_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3018`。

### `RmcPotDatFree.set_bvs_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `central_type` | `int` |
| `neighbors` | `Sequence[Tuple[int, Union[int, float], Optional[Union[int, float]], Optional[Union[int, float]], Optional[int]]]` |
| `valence` | `Union[int, float]` |
| `sigma` | `Union[int, float]` |
| `central_charge` | `Optional[int]` |
| `sigma_mode` | `str` |
| `index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3109`。

### `RmcPotDatFree.remove_bvs_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3252`。

### `RmcPotDatFree.clear_bvs_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3263`。

### `RmcPotDatFree.get_pair_potential_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3271`。

### `RmcPotDatFree.set_pair_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `partials` | `Sequence[Tuple[int, str, Union[int, float, str], str]]` |
| `cutoff` | `Optional[Union[int, float]]` |
| `temperature` | `Union[int, float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3338`。

### `RmcPotDatFree.clear_pair_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3449`。

### `RmcPotDatFree.write_pair_potential_file`

| 引数 | 型注釈 |
|---|---|
| `cls` | `指定なし` |
| `filename` | `Union[str, Path]` |
| `points` | `Sequence[Tuple[Union[int, float], Union[int, float]]]` |
| `comment` | `str` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3470`。

### `RmcPotDatFree.get_cos_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3505`。

### `RmcPotDatFree.set_cos_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `args` | `Any` |
| `kwargs` | `Any` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3509`。

### `RmcPotDatFree.get_snc_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3513`。

### `RmcPotDatFree.set_snc_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `args` | `Any` |
| `kwargs` | `Any` |

戻り値の型注釈: `int`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3517`。

### `RmcPotDatFree.get_lj_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3521`。

### `RmcPotDatFree.set_lj_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `ngr_types` | `int` |
| `lj_sigma` | `Sequence[Union[int, float]]` |
| `lj_epsilon` | `Sequence[Union[int, float]]` |
| `cutoff_vdw` | `Union[int, float]` |
| `cutoff_coul` | `Optional[Union[int, float]]` |
| `vdw_sigma` | `Union[int, float, str]` |
| `coul_sigma` | `Optional[Union[int, float, str]]` |
| `lj_power` | `int` |
| `scale_14_vdw` | `Union[int, float]` |
| `scale_14_coul` | `Optional[Union[int, float]]` |
| `chi_lowlimit_ratio` | `Optional[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3535`。

### `RmcPotDatFree.get_custom_move`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3593`。

### `RmcPotDatFree.set_custom_move`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `nmoved_atoms` | `int` |
| `custom_lines` | `Sequence[Union[str, int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3603`。

### `RmcPotDatFree.get_local_invariance`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3625`。

### `RmcPotDatFree.set_local_invariance`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `mode` | `str` |
| `intervals` | `Sequence[Tuple[Union[int, float], Union[int, float, str], str]]` |
| `r_spacing` | `Optional[Union[int, float]]` |
| `end` | `Optional[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3646`。

### `RmcPotDatFree.get_non_periodic`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Tuple[float, bool]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3685`。

### `RmcPotDatFree.set_non_periodic`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `sample_radius` | `Union[int, float]` |
| `recentre` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3695`。

### `RmcPotDatFree.get_vibrational_amplitudes`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[float]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3714`。

### `RmcPotDatFree.set_vibrational_amplitudes`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `sigma_values` | `Sequence[Union[int, float]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3724`。

### `RmcPotDatFree.get_common_neighbor_constraints`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `List[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3740`。

### `RmcPotDatFree.set_common_neighbor_constraint`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `index` | `int` |
| `primary_type1` | `int` |
| `primary_type2` | `int` |
| `primary_minimum` | `Union[int, float]` |
| `primary_maximum` | `Union[int, float]` |
| `secondary` | `Sequence[Tuple[int, Union[int, float], Union[int, float], Union[int, float], Union[int, float]]]` |
| `coordination_number` | `int` |
| `fraction` | `Union[int, float]` |
| `sigma` | `Union[int, float, str]` |
| `sigma_mode` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3750`。

### `RmcPotDatFree.get_ann_potential_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3798`。

### `RmcPotDatFree.set_ann_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `args` | `Any` |
| `kwargs` | `Any` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3802`。

### `RmcPotDatFree.get_aenet_settings`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Optional[Dict[str, Any]]`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3835`。

### `RmcPotDatFree.set_aenet_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `potentials` | `Sequence[Tuple[int, str, Optional[str]]]` |
| `sigma` | `Union[int, float]` |
| `sigma_mode` | `str` |
| `cutoff` | `Optional[Union[int, float]]` |
| `write_atomic_energy` | `bool` |
| `aenet_step` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:3923`。

### `RmcPotDatFree.add_aenet_potential_file`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_type` | `int` |
| `filename` | `str` |
| `type_name` | `Optional[str]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:4038`。

### `RmcPotDatFree.remove_aenet_potential_file`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_type` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:4100`。

### `RmcPotDatFree.clear_aenet_potential`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:4150`。

### `main`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_free(20261116-081310).py:4172`。

