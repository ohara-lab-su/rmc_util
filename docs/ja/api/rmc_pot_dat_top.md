# `rmc_util.rmc_pot_dat_top`

ソース: `src/rmc_util/rmc_pot_dat_top.py`

## クラス `TopologySection`

TOP/ITP 内の 1 セクションを保持する。

Attributes:
    name: 角括弧を除いたセクション名。
    lines: セクション内部のデータ行。

## クラス `RmcPotDatTop`

RMC_POT TOP/ITP ファイルを生成・編集する独立クラス。

低水準のセクション操作に加え、atoms、bonds、angles、dihedrals などを
明示的に追加するメソッドを提供する。規則的な分子テンプレートと、セル全体を
1 分子として列挙する不規則ネットワークの両方を扱う。

### `__init__(self, name: str, *, auto_write: bool=True, logger: Optional[XLogger]=None)`

インスタンスを初期化する。

Args:
    name: name に指定する値。
    auto_write: auto_write に指定する値。
    logger: logger に指定する値。

### `path(self)`

現在の入出力パスを返す。

Returns:
    処理結果。

### `clear(self, *, auto_write: Optional[bool]=None)`

保持している内容を消去する。

Args:
    auto_write: auto_write に指定する値。

### `load(self)`

既存ファイルを読み込む。
        

### `write(self, out_name: Optional[str]=None)`

現在の内部状態をファイルへ書き出す。

Args:
    out_name: out_name に指定する値。

### `add_raw_line(self, line: str='', *, auto_write: Optional[bool]=None)`

raw line を追加する。

Args:
    line: line に指定する値。
    auto_write: auto_write に指定する値。

### `add_comment(self, comment: str, *, auto_write: Optional[bool]=None)`

comment を追加する。

Args:
    comment: comment に指定する値。
    auto_write: auto_write に指定する値。

### `add_include(self, filename: str, *, auto_write: Optional[bool]=None)`

include を追加する。

Args:
    filename: filename に指定する値。
    auto_write: auto_write に指定する値。

### `add_ifdef(self, symbol: str, *, auto_write: Optional[bool]=None)`

ifdef を追加する。

Args:
    symbol: symbol に指定する値。
    auto_write: auto_write に指定する値。

### `add_ifndef(self, symbol: str, *, auto_write: Optional[bool]=None)`

ifndef を追加する。

Args:
    symbol: symbol に指定する値。
    auto_write: auto_write に指定する値。

### `add_else(self, *, auto_write: Optional[bool]=None)`

else を追加する。

Args:
    auto_write: auto_write に指定する値。

### `add_endif(self, *, auto_write: Optional[bool]=None)`

endif を追加する。

Args:
    auto_write: auto_write に指定する値。

### `add_section(self, name: str, *, auto_write: Optional[bool]=None)`

section を追加する。

Args:
    name: name に指定する値。
    auto_write: auto_write に指定する値。

Returns:
    処理結果。

### `get_sections(self, name: Optional[str]=None)`

sections を取得する。

Args:
    name: name に指定する値。

Returns:
    処理結果。

### `get_last_section(self, name: str)`

last section を取得する。

Args:
    name: name に指定する値。

Returns:
    処理結果。

### `add_section_line(self, section_name: str, line: str, *, create: bool=True, auto_write: Optional[bool]=None)`

section line を追加する。

Args:
    section_name: section_name に指定する値。
    line: line に指定する値。
    create: create に指定する値。
    auto_write: auto_write に指定する値。

### `remove_sections(self, name: str, *, auto_write: Optional[bool]=None)`

sections を削除する。

Args:
    name: name に指定する値。
    auto_write: auto_write に指定する値。

### `begin_molecule_type(self, name: str, exclusions: int, *, index_offset: Optional[int]=None, auto_write: Optional[bool]=None)`

begin molecule type を実行する。

Args:
    name: name に指定する値。
    exclusions: exclusions に指定する値。
    index_offset: index_offset に指定する値。
    auto_write: auto_write に指定する値。

### `add_atom(self, serial: int, atom_type: str, residue_number: int, residue_name: str, atom_name: str, charge_group: int, charge: float, mass: Optional[float], first_rmc_index: int, second_rmc_index: int, *, auto_write: Optional[bool]=None)`

atom を追加する。

Args:
    serial: serial に指定する値。
    atom_type: atom_type に指定する値。
    residue_number: residue_number に指定する値。
    residue_name: residue_name に指定する値。
    atom_name: atom_name に指定する値。
    charge_group: charge_group に指定する値。
    charge: charge に指定する値。
    mass: mass に指定する値。
    first_rmc_index: first_rmc_index に指定する値。
    second_rmc_index: second_rmc_index に指定する値。
    auto_write: auto_write に指定する値。

### `add_virtual_atom(self, serial: int, atom_type: str, residue_number: int, residue_name: str, atom_name: str, charge_group: int, charge: float, *, mass: float=0.0, auto_write: Optional[bool]=None)`

virtual atom を追加する。

Args:
    serial: serial に指定する値。
    atom_type: atom_type に指定する値。
    residue_number: residue_number に指定する値。
    residue_name: residue_name に指定する値。
    atom_name: atom_name に指定する値。
    charge_group: charge_group に指定する値。
    charge: charge に指定する値。
    mass: mass に指定する値。
    auto_write: auto_write に指定する値。

### `add_pair(self, atom_i: int, atom_j: int, *, function_type: int=1, v_parameter: Optional[float]=None, w_parameter: Optional[float]=None, auto_write: Optional[bool]=None)`

pair を追加する。

Args:
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    function_type: function_type に指定する値。
    v_parameter: v_parameter に指定する値。
    w_parameter: w_parameter に指定する値。
    auto_write: auto_write に指定する値。

### `add_bond(self, atom_i: int, atom_j: int, equilibrium_nm: float, force_constant: float, sigma: Optional[float]=None, *, function_type: int=1, rmc_parameters_after_semicolon: bool=False, auto_write: Optional[bool]=None)`

bond を追加する。

Args:
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    equilibrium_nm: equilibrium_nm に指定する値。
    force_constant: force_constant に指定する値。
    sigma: sigma に指定する値。
    function_type: function_type に指定する値。
    rmc_parameters_after_semicolon: rmc_parameters_after_semicolon に指定する値。
    auto_write: auto_write に指定する値。

### `add_angle(self, atom_i: int, atom_j: int, atom_k: int, equilibrium_degree: float, force_constant: float, sigma: Optional[float]=None, *, function_type: int=1, rmc_parameters_after_semicolon: bool=False, auto_write: Optional[bool]=None)`

angle を追加する。

Args:
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    atom_k: atom_k に指定する値。
    equilibrium_degree: equilibrium_degree に指定する値。
    force_constant: force_constant に指定する値。
    sigma: sigma に指定する値。
    function_type: function_type に指定する値。
    rmc_parameters_after_semicolon: rmc_parameters_after_semicolon に指定する値。
    auto_write: auto_write に指定する値。

### `add_periodic_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, equilibrium_degree: float, force_constant: float, multiplicity: int, sigma: Optional[float]=None, *, auto_write: Optional[bool]=None)`

periodic dihedral を追加する。

Args:
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    atom_k: atom_k に指定する値。
    atom_l: atom_l に指定する値。
    equilibrium_degree: equilibrium_degree に指定する値。
    force_constant: force_constant に指定する値。
    multiplicity: multiplicity に指定する値。
    sigma: sigma に指定する値。
    auto_write: auto_write に指定する値。

### `add_harmonic_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, equilibrium_degree: float, force_constant: float, sigma: Optional[float]=None, *, auto_write: Optional[bool]=None)`

harmonic dihedral を追加する。

Args:
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    atom_k: atom_k に指定する値。
    atom_l: atom_l に指定する値。
    equilibrium_degree: equilibrium_degree に指定する値。
    force_constant: force_constant に指定する値。
    sigma: sigma に指定する値。
    auto_write: auto_write に指定する値。

### `add_rb_dihedral(self, atom_i: int, atom_j: int, atom_k: int, atom_l: int, coefficients: Sequence[float], sigma: Optional[float]=None, *, auto_write: Optional[bool]=None)`

rb dihedral を追加する。

Args:
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    atom_k: atom_k に指定する値。
    atom_l: atom_l に指定する値。
    coefficients: coefficients に指定する値。
    sigma: sigma に指定する値。
    auto_write: auto_write に指定する値。

### `add_exclusion(self, centre_atom: int, excluded_atoms: Sequence[int], *, auto_write: Optional[bool]=None)`

exclusion を追加する。

Args:
    centre_atom: centre_atom に指定する値。
    excluded_atoms: excluded_atoms に指定する値。
    auto_write: auto_write に指定する値。

### `add_virtual_site2(self, site: int, atom_i: int, atom_j: int, a: float, *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None)`

virtual site2 を追加する。

Args:
    site: site に指定する値。
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    a: a に指定する値。
    host_atom: host_atom に指定する値。
    auto_write: auto_write に指定する値。

### `add_virtual_site3(self, site: int, atom_i: int, atom_j: int, atom_k: int, function_type: int, parameters: Sequence[float], *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None)`

virtual site3 を追加する。

Args:
    site: site に指定する値。
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    atom_k: atom_k に指定する値。
    function_type: function_type に指定する値。
    parameters: parameters に指定する値。
    host_atom: host_atom に指定する値。
    auto_write: auto_write に指定する値。

### `add_virtual_site4(self, site: int, atom_i: int, atom_j: int, atom_k: int, atom_l: int, a: float, b: float, c_nm: float, *, host_atom: Optional[int]=None, auto_write: Optional[bool]=None)`

virtual site4 を追加する。

Args:
    site: site に指定する値。
    atom_i: atom_i に指定する値。
    atom_j: atom_j に指定する値。
    atom_k: atom_k に指定する値。
    atom_l: atom_l に指定する値。
    a: a に指定する値。
    b: b に指定する値。
    c_nm: c_nm に指定する値。
    host_atom: host_atom に指定する値。
    auto_write: auto_write に指定する値。

### `set_system(self, name: str, *, auto_write: Optional[bool]=None)`

system を設定する。

Args:
    name: name に指定する値。
    auto_write: auto_write に指定する値。

### `set_molecules(self, molecules: Sequence[Tuple[str, int]], *, auto_write: Optional[bool]=None)`

molecules を設定する。

Args:
    molecules: molecules に指定する値。
    auto_write: auto_write に指定する値。

### `add_molecule_template(self, molecule_name: str, atoms: Sequence[Mapping[str, object]], first_instance_indices: Mapping[int, int], second_instance_indices: Mapping[int, int], *, exclusions: int=3, index_offset: Optional[int]=None, bonds: Sequence[Mapping[str, object]]=(), angles: Sequence[Mapping[str, object]]=(), periodic_dihedrals: Sequence[Mapping[str, object]]=(), harmonic_dihedrals: Sequence[Mapping[str, object]]=(), rb_dihedrals: Sequence[Mapping[str, object]]=(), pairs: Sequence[Mapping[str, object]]=(), explicit_exclusions: Sequence[Tuple[int, Sequence[int]]]=(), auto_write: Optional[bool]=None)`

再利用可能な 1 分子タイプを追加する。

Args:
    molecule_name: ``[ moleculetype ]`` に書く分子名。
    atoms: 分子内原子の辞書列。``serial`` と ``atom_type`` は必須。
    first_instance_indices: 1番目の分子に対する local serial と RMC index。
    second_instance_indices: 2番目の分子に対する local serial と RMC index。
    exclusions: GROMACS の nrexcl。
    index_offset: RMC_POT 用の明示的 index offset。
    bonds: ``add_bond()`` へ渡す辞書列。
    angles: ``add_angle()`` へ渡す辞書列。
    periodic_dihedrals: 周期 dihedral の辞書列。
    harmonic_dihedrals: harmonic dihedral の辞書列。
    rb_dihedrals: Ryckaert--Bellemans dihedral の辞書列。
    pairs: ``add_pair()`` へ渡す辞書列。
    explicit_exclusions: 中心原子と除外原子列の組。
    auto_write: 追加後に自動保存するか。

### `add_explicit_network_molecule(self, molecule_name: str, atoms: Sequence[Mapping[str, object]], *, exclusions: int=2, bonds: Sequence[Mapping[str, object]]=(), angles: Sequence[Mapping[str, object]]=(), periodic_dihedrals: Sequence[Mapping[str, object]]=(), harmonic_dihedrals: Sequence[Mapping[str, object]]=(), rb_dihedrals: Sequence[Mapping[str, object]]=(), auto_write: Optional[bool]=None)`

任意のセル内ネットワークを 1 個の巨大分子として追加する。

各 local serial を最終 RMC index へ直接対応付ける。分子インスタンスは
1 個だけなので、``[ atoms ]`` に記録する第1・第2 RMC index は同じ値に
する。規則的な繰り返しでは表現できない Qn ネットワークに使用する。

### `validate_rmc_index_progression(first_instance: Mapping[int, int], second_instance: Mapping[int, int], all_instances: Sequence[Mapping[int, int]])`

Check that later instances follow the first/second index progression.

### `validate(self)`

現在の設定内容を検証する。
        

## クラス `RmcPotDatItp`

Explicit class name for include-topology files.

## `main()`

RMC_POT マニュアルの SnI4 配置例から ``sample.top`` を生成する。

この例の目的は、``[ atoms ]`` の末尾に書く ``first index`` と
``second index`` の対応を示すことである。結合ポテンシャルのパラメータは
マニュアルの index 配置例からは決まらないため、``[ bonds ]`` などは
生成しない。

マニュアルの第1表現では、1000 個の SnI4 分子について、Sn 原子を
RMC index 1--1000、4種類の I 原子をそれぞれ 1001--2000、
2001--3000、3001--4000、4001--5000 のブロックへ配置する。
したがって、最初と2番目の分子の対応は次のようになる。

* Sn: 1, 2
* I1: 1001, 1005
* I2: 1002, 1006
* I3: 1003, 1007
* I4: 1004, 1008

この規則により、任意の分子番号について各原子の RMC index を計算できる。


## 実装に基づく API 一覧

この一覧は提供された `rmc_pot_dat_top(10).py` の関数定義から作成しています。既存の説明は上に保持し、引数・戻り値の型や副作用が明示されていないものは推測していません。

### `TopologySection` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### `RmcPotDatTop` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| `__init__()` | 56 | インスタンスを初期化する。 |
| `path()` | 93 | 現在の入出力パスを返す。 |
| `clear()` | 101 | 保持している内容を消去する。 |
| `load()` | 110 | 既存ファイルを読み込む。 |
| `write()` | 130 | 現在の内部状態をファイルへ書き出す。 |
| `add_raw_line()` | 149 | raw line を追加する。 |
| `add_comment()` | 159 | comment を追加する。 |
| `add_include()` | 171 | include を追加する。 |
| `add_ifdef()` | 180 | ifdef を追加する。 |
| `add_ifndef()` | 189 | ifndef を追加する。 |
| `add_else()` | 198 | else を追加する。 |
| `add_endif()` | 206 | endif を追加する。 |
| `add_section()` | 214 | section を追加する。 |
| `get_sections()` | 234 | sections を取得する。 |
| `get_last_section()` | 249 | last section を取得する。 |
| `add_section_line()` | 263 | section line を追加する。 |
| `remove_sections()` | 289 | sections を削除する。 |
| `begin_molecule_type()` | 303 | begin molecule type を実行する。 |
| `add_atom()` | 326 | atom を追加する。 |
| `add_virtual_atom()` | 368 | virtual atom を追加する。 |
| `add_pair()` | 399 | pair を追加する。 |
| `add_bond()` | 426 | bond を追加する。 |
| `add_angle()` | 457 | angle を追加する。 |
| `add_periodic_dihedral()` | 490 | periodic dihedral を追加する。 |
| `add_harmonic_dihedral()` | 524 | harmonic dihedral を追加する。 |
| `add_rb_dihedral()` | 556 | rb dihedral を追加する。 |
| `add_exclusion()` | 586 | exclusion を追加する。 |
| `add_virtual_site2()` | 608 | virtual site2 を追加する。 |
| `add_virtual_site3()` | 634 | virtual site3 を追加する。 |
| `add_virtual_site4()` | 669 | virtual site4 を追加する。 |
| `set_system()` | 702 | system を設定する。 |
| `set_molecules()` | 714 | molecules を設定する。 |
| `add_molecule_template()` | 734 | 再利用可能な 1 分子タイプを追加する。 |
| `add_explicit_network_molecule()` | 807 | 任意のセル内ネットワークを 1 個の巨大分子として追加する。 |
| `validate_rmc_index_progression()` | 848 | Check that later instances follow the first/second index progression. |
| `validate()` | 871 | 現在の設定内容を検証する。 |

### `RmcPotDatItp` のメソッド

| メソッド | 定義位置 | 説明（docstring 冒頭） |
|---|---:|---|
| （公開メソッドなし） | — | — |

### モジュール関数 `main()`

- 定義位置：1077 行
- 説明：RMC_POT マニュアルの SnI4 配置例から ``sample.top`` を生成する。

## ソースコードに基づく引数・戻り値一覧

この節は提供された実装の関数宣言と型注釈を直接確認した一覧です。型注釈のない引数・戻り値は「指定なし」と記載しています。実行時の戻り値が `None` であることを意味しません。

### `RmcPotDatTop.__init__`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `auto_write` | `bool` |
| `logger` | `Optional[XLogger]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:56`。

### `RmcPotDatTop.path`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `Path`。定義位置: `rmc_pot_dat_top(10).py:93`。

### `RmcPotDatTop.clear`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:101`。

### `RmcPotDatTop.load`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:110`。

### `RmcPotDatTop.write`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `out_name` | `Optional[str]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:130`。

### `RmcPotDatTop.add_raw_line`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `line` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:149`。

### `RmcPotDatTop.add_comment`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `comment` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:159`。

### `RmcPotDatTop.add_include`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `filename` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:171`。

### `RmcPotDatTop.add_ifdef`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `symbol` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:180`。

### `RmcPotDatTop.add_ifndef`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `symbol` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:189`。

### `RmcPotDatTop.add_else`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:198`。

### `RmcPotDatTop.add_endif`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:206`。

### `RmcPotDatTop.add_section`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `TopologySection`。定義位置: `rmc_pot_dat_top(10).py:214`。

### `RmcPotDatTop.get_sections`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `Optional[str]` |

戻り値の型注釈: `List[TopologySection]`。定義位置: `rmc_pot_dat_top(10).py:234`。

### `RmcPotDatTop.get_last_section`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |

戻り値の型注釈: `TopologySection`。定義位置: `rmc_pot_dat_top(10).py:249`。

### `RmcPotDatTop.add_section_line`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `section_name` | `str` |
| `line` | `str` |
| `create` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:263`。

### `RmcPotDatTop.remove_sections`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:289`。

### `RmcPotDatTop.begin_molecule_type`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `exclusions` | `int` |
| `index_offset` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:303`。

### `RmcPotDatTop.add_atom`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `serial` | `int` |
| `atom_type` | `str` |
| `residue_number` | `int` |
| `residue_name` | `str` |
| `atom_name` | `str` |
| `charge_group` | `int` |
| `charge` | `float` |
| `mass` | `Optional[float]` |
| `first_rmc_index` | `int` |
| `second_rmc_index` | `int` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:326`。

### `RmcPotDatTop.add_virtual_atom`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `serial` | `int` |
| `atom_type` | `str` |
| `residue_number` | `int` |
| `residue_name` | `str` |
| `atom_name` | `str` |
| `charge_group` | `int` |
| `charge` | `float` |
| `mass` | `float` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:368`。

### `RmcPotDatTop.add_pair`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `function_type` | `int` |
| `v_parameter` | `Optional[float]` |
| `w_parameter` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:399`。

### `RmcPotDatTop.add_bond`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `equilibrium_nm` | `float` |
| `force_constant` | `float` |
| `sigma` | `Optional[float]` |
| `function_type` | `int` |
| `rmc_parameters_after_semicolon` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:426`。

### `RmcPotDatTop.add_angle`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `equilibrium_degree` | `float` |
| `force_constant` | `float` |
| `sigma` | `Optional[float]` |
| `function_type` | `int` |
| `rmc_parameters_after_semicolon` | `bool` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:457`。

### `RmcPotDatTop.add_periodic_dihedral`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `equilibrium_degree` | `float` |
| `force_constant` | `float` |
| `multiplicity` | `int` |
| `sigma` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:490`。

### `RmcPotDatTop.add_harmonic_dihedral`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `equilibrium_degree` | `float` |
| `force_constant` | `float` |
| `sigma` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:524`。

### `RmcPotDatTop.add_rb_dihedral`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `coefficients` | `Sequence[float]` |
| `sigma` | `Optional[float]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:556`。

### `RmcPotDatTop.add_exclusion`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `centre_atom` | `int` |
| `excluded_atoms` | `Sequence[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:586`。

### `RmcPotDatTop.add_virtual_site2`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `site` | `int` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `a` | `float` |
| `host_atom` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:608`。

### `RmcPotDatTop.add_virtual_site3`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `site` | `int` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `function_type` | `int` |
| `parameters` | `Sequence[float]` |
| `host_atom` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:634`。

### `RmcPotDatTop.add_virtual_site4`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `site` | `int` |
| `atom_i` | `int` |
| `atom_j` | `int` |
| `atom_k` | `int` |
| `atom_l` | `int` |
| `a` | `float` |
| `b` | `float` |
| `c_nm` | `float` |
| `host_atom` | `Optional[int]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:669`。

### `RmcPotDatTop.set_system`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `name` | `str` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:702`。

### `RmcPotDatTop.set_molecules`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `molecules` | `Sequence[Tuple[str, int]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:714`。

### `RmcPotDatTop.add_molecule_template`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `molecule_name` | `str` |
| `atoms` | `Sequence[Mapping[str, object]]` |
| `first_instance_indices` | `Mapping[int, int]` |
| `second_instance_indices` | `Mapping[int, int]` |
| `exclusions` | `int` |
| `index_offset` | `Optional[int]` |
| `bonds` | `Sequence[Mapping[str, object]]` |
| `angles` | `Sequence[Mapping[str, object]]` |
| `periodic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `harmonic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `rb_dihedrals` | `Sequence[Mapping[str, object]]` |
| `pairs` | `Sequence[Mapping[str, object]]` |
| `explicit_exclusions` | `Sequence[Tuple[int, Sequence[int]]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:734`。

### `RmcPotDatTop.add_explicit_network_molecule`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |
| `molecule_name` | `str` |
| `atoms` | `Sequence[Mapping[str, object]]` |
| `exclusions` | `int` |
| `bonds` | `Sequence[Mapping[str, object]]` |
| `angles` | `Sequence[Mapping[str, object]]` |
| `periodic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `harmonic_dihedrals` | `Sequence[Mapping[str, object]]` |
| `rb_dihedrals` | `Sequence[Mapping[str, object]]` |
| `auto_write` | `Optional[bool]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:807`。

### `RmcPotDatTop.validate_rmc_index_progression`

| 引数 | 型注釈 |
|---|---|
| `first_instance` | `Mapping[int, int]` |
| `second_instance` | `Mapping[int, int]` |
| `all_instances` | `Sequence[Mapping[int, int]]` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:848`。

### `RmcPotDatTop.validate`

| 引数 | 型注釈 |
|---|---|
| `self` | `指定なし` |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:871`。

### `main`

| 引数 | 型注釈 |
|---|---|
| （なし） | — |

戻り値の型注釈: `None`。定義位置: `rmc_pot_dat_top(10).py:1077`。

