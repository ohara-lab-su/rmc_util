# 最初の RMC 計算

RMC_UTIL は、計算ディレクトリに配置した `rmc.py` と `rmc_init.py` を入口として RMC_POT を実行します。RMC_UTIL の Python パッケージと RMC_POT の実行ファイルは別に準備します。

## 1. パッケージをインストールする

```bash
pip install rmc-util
```

リポジトリから導入する場合は、リポジトリのルートで `pip install .` を実行します。配布名は `rmc-util`、Python のインポート名は `rmc_util` です。

## 2. 計算スクリプトを配置する

計算ディレクトリへ移動し、次を実行します。

```bash
rmc_util install
```

`rmc.py`（起動）、`rmc_init.py`（計算条件の編集）、`config.yml`（起動時の設定）を現在のディレクトリへ配置します。同名のファイルが既にある場合は、既定で上書きしません。`rmc_util install --force` は既存ファイルを上書きするため、編集済みの `rmc_init.py` と `config.yml` を保存してから使用してください。詳細は [インストールガイド](../guide/installation.md) を参照してください。

## 3. 入力と実行環境を準備する

配置した `config.yml` を計算に合わせて編集し、初期原子配置 `.cfg`、実験データ、RMC_POT 実行ファイルを準備します。構造制約を使用する場合は、対応する FNC やトポロジーなどの入力も確認します。

`rmc.py` の初期構造作成処理はコメントアウトされています。`python rmc.py` を実行しても、初期構造が自動的に作成されるわけではありません。`.cfg` と `.dat` の形式は [入力ファイル](../guide/input.md)、RMC_POT 側の仕様は [入力形式リファレンス](../reference/rmcpot_input_explained.md) を参照してください。

## 4. `rmc_init.py` で計算条件を指定する

`rmc_init.py` の `run_rmc_init()` は、`RmcPotDat` に計算条件を設定します。`rmc_dat.init()` で固定形式または自由形式の `.dat` を初期化し、数密度、cutoff、最大移動幅、構造制約などを同じ Python API から指定します。

`prefer_existing=True` は既存の `.dat` を優先して扱うための指定です。既存ファイルを再利用する場合は、その形式と計算条件を確認してください。物質系ごとの記述例は [計算条件の設定](configure.md)、[入力ファイルの編集](input_editing.md)、[構造制約の例](constraints.md) に示します。

## 5. 計算を実行する

```bash
python rmc.py
```

起動スクリプトは `Config("config.yml")` を読み込み、`RmcPotLog` と `RmcPotDat` を生成し、`run_rmc_init()` による設定後に `run_rmc()` を呼び出します。起動時の `auto_converge` と `postprocess` は、`.dat` のファイル形式とは独立した実行制御です。詳細は [実行ワークフロー](workflow.md) を参照してください。

## 6. 出力を確認する

ログの正常終了、試行・受理回数、評価関数の推移、実験データとの一致度、構造制約の充足を個別に確認します。正常終了は構造の収束を保証しません。出力ファイルは [結果解析](analysis.md) と [出力ガイド](../guide/output.md) を参照してください。
