# API リファレンス

RMC_UTIL の公開クラス、関数、メソッドの仕様を示します。引数の既定値と型注釈は各 API の定義に従います。

```{toctree}
:maxdepth: 2

Generated Python API <generated/modules>

implementation_index

config
install
rmc_pot
rmc_pot_dat
rmc_pot_dat_fixed
rmc_pot_dat_free
rmc_pot_dat_fnc
rmc_pot_dat_top
rmc_pot_fit
rmc_pot_hst
rmc_pot_log
rmc_pot_ppcf
rmc_pot_snc
runners_run_rmc
util_zeolite
util_poscar2cfg
util_cfg2poscar
util_ensure_vasp5_format
util_find_next_log_index
util_gromacs_top_to_rmc_top
```

## API の読み方

各モジュールのページには、主要な公開メソッドとその引数、戻り値、処理内容を記載しています。正確なシグネチャとdocstringは自動生成APIから参照できます。

まず `RmcPotDat` の初期化と入力操作、次に `RmcPot` の実行・前後処理、`run_rmc()` の反復処理を参照してください。結果解析は `RmcPotLog`、`RmcPotHst`、`RmcPotFit`、`RmcPotPpcf` の各ページから確認できます。


