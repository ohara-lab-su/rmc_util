"""インストール済みの雛形をカレントディレクトリに配置する。"""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import sysconfig
from importlib import metadata
from pathlib import Path


DESTINATION_DIRECTORY: Path = Path.cwd()
DISTRIBUTION_NAME: str = "rmc-util"
SCRIPTS_RELATIVE_DIRECTORY: Path = Path("share/rmc_util/scripts")

_SCRIPT_DESCRIPTIONS = {
    "config.yml": "RMC_POT の実行設定テンプレート",
    "plot_fit.py": ".fit の計算値と実験値の S(Q) を比較",
    "plot_hst.py": ".hst の χ² の推移を表示",
    "plot_ppcf.py": ".ppcf の原子種ペア別の g(r) を重ねて表示",
    "plot_ppcf2.py": ".ppcf の原子種ペア別の g(r) を個別のパネルに表示",
    "rmc.py": "RMC 計算を起動",
    "rmc_init.py": "RMC の計算条件を設定",
}


def find_installed_scripts() -> list[Path]:
    """インストール先と配布記録を調べ、同名の雛形を一度だけ取得する。"""
    sources_by_name: dict[str, Path] = {}
    data_directory = Path(sysconfig.get_path("data"))
    installed_directory = data_directory / SCRIPTS_RELATIVE_DIRECTORY
    if installed_directory.is_dir():
        for source in sorted(installed_directory.iterdir()):
            if source.is_file():
                sources_by_name[source.name] = source
    distribution = metadata.distribution(DISTRIBUTION_NAME)
    installed_files = distribution.files
    script_directory_parts = SCRIPTS_RELATIVE_DIRECTORY.parts
    if installed_files is not None:
        for file in installed_files:
            relative_path = Path(str(file))
            parent_parts = relative_path.parent.parts[-len(script_directory_parts) :]
            if parent_parts != script_directory_parts:
                continue
            source = Path(distribution.locate_file(file))
            if source.is_file() and source.name not in sources_by_name:
                sources_by_name[source.name] = source
    return [sources_by_name[name] for name in sorted(sources_by_name)]


def install_scripts(
    destination: Path,
    *,
    force: bool = False,
    script_name: str | None = None,
) -> tuple[int, int]:
    """全雛形、または指定した名前の雛形を配置する。

    Args:
        destination: 雛形を配置するディレクトリ。
        force: 真の場合に既存ファイルを上書きする。
        script_name: 一つだけ配置するファイル名。.py と .yml は省略可能。
            None なら全ファイル。

    Returns:
        コピー件数とスキップ件数。

    Raises:
        ValueError: 指定したファイルが配布物に含まれていない。
        RuntimeError: 配布済みの雛形が見つからない。
    """
    sources = find_installed_scripts()
    if not sources:
        raise RuntimeError(
            "インストール済みの雛形が見つかりません。"
            "pipでインストールした環境のshare/rmc_util/scriptsを確認してください。"
        )
    if script_name is not None:
        sources_by_name = {source.name: source for source in sources}
        selected = sources_by_name.get(script_name)
        if selected is None:
            selected = sources_by_name.get(f"{script_name}.py")
        if selected is None:
            selected = sources_by_name.get(f"{script_name}.yml")
        if selected is None:
            raise ValueError(f"指定されたファイルが見つかりません: {script_name}")
        sources = [selected]

    destination.mkdir(parents=True, exist_ok=True)
    copied = 0
    skipped = 0
    for source in sources:
        target = destination / source.name
        if target.exists() and not force:
            print(f"既存のためスキップ: {target.name}")
            skipped += 1
            continue
        if target.is_dir():
            raise IsADirectoryError(f"コピー先がディレクトリです: {target}")
        existed = target.exists()
        shutil.copy2(source, target)
        if os.name == "posix" and target.name == "rmc.py":
            target.chmod(target.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        if existed:
            print(f"上書き: {target.name}")
        else:
            print(f"コピー: {target.name}")
        copied += 1
    return copied, skipped


def main() -> None:
    """利用可能なファイルを一覧表示するか、作業ディレクトリに配置する。"""
    parser = argparse.ArgumentParser(prog="rmc_util")
    commands = parser.add_subparsers(dest="command", required=True)
    installer = commands.add_parser("install", help="作業ディレクトリにファイルを配置")
    installer.add_argument("target", nargs="?", default="all", metavar="all|script|NAME")
    installer.add_argument("--force", action="store_true", help="既存ファイルを上書き")
    commands.add_parser("list", help="配置できるファイルと用途を表示")
    args = parser.parse_args()

    if args.command == "list":
        names = [source.name for source in find_installed_scripts()]
        header = "NAME"
        width = max(map(len, [header, *names]))
        print(f"{header:<{width}}  DESCRIPTION")
        for name in names:
            description = _SCRIPT_DESCRIPTIONS.get(name, "作業ディレクトリ用の配布ファイル")
            print(f"{name:<{width}}  {description}")
        return

    script_name = args.target
    if script_name in ("all", "script"):
        script_name = None
    try:
        copied, skipped = install_scripts(
            DESTINATION_DIRECTORY,
            force=args.force,
            script_name=script_name,
        )
    except ValueError as error:
        installer.error(f"{error}。rmc_util list で一覧を確認してください。")
    print(f"完了: コピー {copied} 件、スキップ {skipped} 件")


if __name__ == "__main__":
    main()
