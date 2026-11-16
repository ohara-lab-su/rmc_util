# インストールと計算スクリプトの準備

## パッケージの導入

```bash
pip install rmc-util
```

開発用のリポジトリを取得している場合は、リポジトリのルートで `pip install .` を使用します。PyPI の配布名は `rmc-util`、Python の import 名は `rmc_util` です。

## 計算ディレクトリへのスクリプト展開

```bash
rmc_util install
```

このコマンドで `rmc.py` と `rmc_init.py` を作業ディレクトリに展開します。既存の同名ファイルは上書きしません。上書きを明示する場合は次のとおりです。

```bash
rmc_util install --force
```

`rmc_init.py` の計算条件を編集し、必要な RMC_POT の入力データと実行環境を準備した後、次のコマンドで起動します。

```bash
python rmc.py
```

RMC_POT 本体、実験データ、初期構造の準備は `pip install` のみでは完了しません。必要な入力については [RMC_POT 入力形式](../reference/rmcpot_input_explained.md)を参照してください。
