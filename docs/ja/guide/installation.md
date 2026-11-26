# インストールと計算ディレクトリの準備

## パッケージと実行プログラム

Pythonパッケージの配布名は `rmc-util`、インポート名は `rmc_util` です。

```bash
pip install rmc-util
```

ソースツリーからインストールする場合は、リポジトリのルートで `pip install .` を実行します。RMC_UTILはRMC_POTの入力・実行・解析を扱うPythonライブラリです。**RMC_POTの計算実行ファイルそのものをインストールするコマンドではありません。** 計算には別途、RMC_POT実行ファイルと実験データ、初期原子配置などを準備します。

## `rmc_util install` の役割

指定なしの `rmc_util install`、`rmc_util install all`、`rmc_util install script` はいずれも、`rmc.py`、`rmc_init.py`、`config.yml` と4本の plot スクリプトをカレントディレクトリに配置します。

```bash
rmc_util install
rmc_util list
rmc_util install plot_fit.py
rmc_util install config
```

`rmc_util list` は配置可能なファイル名と用途を表示します。個別指定では `.py` と `.yml` を省略できます。たとえば `plot_fit` と `plot_fit.py`、`config` と `config.yml` はそれぞれ同じファイルを指定します。

作図するには、対象の結果ファイルがあるディレクトリで、たとえば `python plot_fit.py aaa` を実行します。引数の `aaa` は結果ファイルの基底名です。

計算を起動するには、`config.yml` で RMC_POT の実行ファイル、実験データ、入力ファイルの基底名などを指定し、`rmc_init.py` で計算条件を編集します。

配置先に同名ファイルが存在すると、既定ではそのファイルをスキップします。既存ファイルを置き換える場合だけ、次を実行します。

```bash
rmc_util install --force
```

`--force` は一括・個別配置のどちらにも指定でき、配置対象の同名ファイルを上書きします。パッケージの更新だけでは、計算ディレクトリに配置済みのファイルは自動更新されません。

## 配置元とコピー処理

`rmc_util.install.find_installed_scripts()` は、Pythonのインストール先にある `share/rmc_util/scripts` と、インストール済み配布物のファイル記録から雛形を探します。同名ファイルは重複してコピーしません。雛形が見つからない場合はエラーになります。

`rmc_util.install.install_scripts(destination, force=False, script_name=None)` はコピー件数とスキップ件数を返します。`rmc.py` についてはPOSIX環境で実行権限を付加します。

## 計算の開始と設定の分離

```bash
python rmc.py
```

起動スクリプト `rmc.py` は `config.yml` を読み込み、ログ・入力条件を準備し、作業ディレクトリの `rmc_init.py` にある `run_rmc_init()` で計算条件を適用してから `rmc_util.runners.run_rmc.run_rmc()` を呼び出します。計算の反復処理はパッケージ側に置き、物質系ごとの条件を `rmc_init.py` で管理する構成です。

`.dat` の固定形式・自由形式は `RmcPotDat` の共通メソッドから操作できます。具体的な設定例は [入力条件の編集](../tutorial/configure.md)、構造制約は [制約の設定](../tutorial/constraints.md)、ファイル仕様は [RMC_POT入力形式](../reference/rmcpot_input_explained.md)を参照してください。

## Python APIからの利用

```python
from pathlib import Path
from rmc_util.install import install_scripts

copied, skipped = install_scripts(Path.cwd(), force=False)
```

この API はスクリプトと設定ファイルを配置します。計算条件の編集やRMC計算の開始は別の操作です。関数の詳細は [インストールAPI](../api/install.md)を参照してください。
