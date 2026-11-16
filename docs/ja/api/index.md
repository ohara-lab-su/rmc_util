# API リファレンス

以下は提供された Python ソースコードから抽出した公開クラス・関数・メソッドです。引数の既定値はソースコードの宣言に従います。先頭 `_` の内部メソッドは原則として掲載しません。

```{toctree}
:maxdepth: 2

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

各モジュールのページには、ソースコードにあるシグネチャと docstring に加え、クラスごとの公開メソッド一覧および定義行を収録しています。定義行は今回提供されたソースファイルでの位置であり、将来のリリースでは変わる可能性があります。

まず `RmcPotDat` の初期化と入力操作、次に `RmcPot` の実行・前後処理、`run_rmc()` の反復処理を参照してください。結果解析は `RmcPotLog`、`RmcPotHst`、`RmcPotFit`、`RmcPotPpcf` の各ページから確認できます。

**注意：** `scripts/rmc.py`、`scripts/rmc_init.py`、パッケージの `__init__.py` は提供されていないため、それらの関数仕様は本リファレンスに含めていません。
