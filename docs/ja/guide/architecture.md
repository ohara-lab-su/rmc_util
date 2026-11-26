# ソフトウェア構成と責務

RMC_UTIL は RMC_POT 本体を置き換えるものではなく、入力ファイルの編集、実行の制御、出力ファイルの解析を Python から行うためのライブラリです。

| レイヤー | モジュール | 責務 |
|---|---|---|
| 計算条件 | `rmc_pot_dat.py` | 固定形式・自由形式の `.dat` を共通 API で操作 |
| 形式別入力 | `rmc_pot_dat_fixed.py`、`rmc_pot_dat_free.py` | 各形式の `.dat` の読み書き |
| 追加の入力 | `rmc_pot_dat_fnc.py`、`rmc_pot_dat_top.py`、`rmc_pot_snc.py` | FNC、topology、構造制約関連の操作 |
| 実行 | `rmc_pot.py`、`runners/run_rmc.py` | 実行前検査、RMC_POT 起動、結果処理、反復処理 |
| 出力解析 | `rmc_pot_log.py`、`rmc_pot_hst.py`、`rmc_pot_fit.py`、`rmc_pot_ppcf.py` | ログ、履歴、フィット、部分相関データの処理 |
| ファイル変換 | `util/` | CFG・POSCAR・topology 等の変換と補助処理 |
| 配布ファイル | `install.py`、`scripts/rmc.py`、`scripts/rmc_init.py`、`scripts/config.yml` | 作業ディレクトリへの雛形の展開と起動 |

## 計算ディレクトリとパッケージの分離

`rmc_util install` が展開する `rmc.py` は起動用、`rmc_init.py` は計算条件の編集用、`config.yml` は起動時の設定ファイルです。結果作図用の `plot_*.py` も同じコマンドで展開します。実行処理の本体はインストールされた `rmc_util.runners.run_rmc` 側にあります。パッケージの更新は展開済みのファイルを自動変更しません。

## `.dat` の形式と初期化

`RmcPotDat` はコンストラクタだけでは `.dat` を読み込みません。`init(prefer_existing=True)` で既存ファイルを優先し、新規生成時は `use_free_format` で形式を指定します。既存ファイルがある場合の形式と新規生成時の指定を混同しないでください。

## 関連ページ

[基本的な利用方法](software.md) / [チュートリアル](../tutorial/index.md) / [API リファレンス](../api/index.md)
