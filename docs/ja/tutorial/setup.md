# 1. インストールと実行スクリプトの準備

PyPI の配布名は `rmc-util`、import 名は `rmc_util` です。

```bash
pip install rmc-util
rmc_util install
```

`rmc_util install` は作業ディレクトリに `rmc.py`、`rmc_init.py`、`config.yml` を配置します。既存ファイルは上書きせず、明示的な上書きは `rmc_util install --force` です。`config.yml` と `rmc_init.py` を計算に合わせて編集し、必要な初期構造・入力データを準備した後に実行します。

```bash
python rmc.py
```

実行処理はパッケージ内の `rmc_util.runners.run_rmc` が担当します。パッケージ更新によって配置済みファイルの編集内容が自動更新されることはありません。

詳しくは [利用ガイド](../guide/software.md) を参照してください。
