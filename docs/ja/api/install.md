# `rmc_util.install`

インストール済みパッケージに含まれる計算用スクリプトと設定テンプレートを、指定したディレクトリへ配置するモジュールです。CLIの使用方法は [インストールガイド](../guide/installation.md)を参照してください。

## `find_installed_scripts() -> list[Path]`

Pythonの `sysconfig.get_path("data")` で得られるディレクトリ内の `share/rmc_util/scripts` と、`importlib.metadata.distribution("rmc-util")` のファイル記録を調べます。同名の雛形は一度だけ取得し、名前順の `Path` リストを返します。

## `install_scripts(destination: Path, *, force: bool = False, script_name: str | None = None) -> tuple[int, int]`

`destination` に雛形をコピーします。`script_name=None` で全ファイル、ファイル名を指定すると1ファイルを配置します。`.py` と `.yml` は省略でき、指定名が見つからなければ `ValueError` になります。既存の同名ファイルは `force=False` ではスキップし、`force=True` では上書きします。コピー先がディレクトリであれば `IsADirectoryError` が発生します。戻り値は `(コピー件数, スキップ件数)` です。POSIXでは `rmc.py` に実行権限を付加します。雛形が見つからない場合は `RuntimeError` が発生します。

```python
from pathlib import Path
from rmc_util.install import install_scripts

copied, skipped = install_scripts(Path.cwd(), force=False)
```

## `main() -> None`

CLI のエントリーポイントです。`rmc_util list` でファイル名と用途を表示します。`rmc_util install [all|script|ファイル名] [--force]` で配置し、コピー・スキップ件数を表示します。不正な引数や未知のファイル名は終了コード 2 です。
