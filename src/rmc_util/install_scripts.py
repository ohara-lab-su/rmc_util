"""インストール済みの雛形をカレントディレクトリに配置する。"""

from __future__ import annotations

import shutil
import sys
import sysconfig
from importlib import metadata
from pathlib import Path


DESTINATION_DIRECTORY: Path = Path.cwd()
DISTRIBUTION_NAME: str = "rmc-util"
SCRIPTS_RELATIVE_DIRECTORY: Path = Path("share/rmc_util/scripts")


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
    if installed_files is not None:
        for file in installed_files:
            relative_path = Path(str(file))
            if relative_path.parent.parts[-len(SCRIPTS_RELATIVE_DIRECTORY.parts):] != SCRIPTS_RELATIVE_DIRECTORY.parts:
                continue
            source = Path(distribution.locate_file(file))
            if source.is_file() and source.name not in sources_by_name:
                sources_by_name[source.name] = source

    return [sources_by_name[name] for name in sorted(sources_by_name)]


def install_scripts(
    destination: Path,
    *,
    force: bool = False,
) -> tuple[int, int]:
    """雛形を配置する。forceが真のときだけ既存ファイルを上書きする。"""
    sources = find_installed_scripts()
    if not sources:
        raise RuntimeError(
            "インストール済みの雛形が見つかりません。"
            "pipでインストールした環境のshare/rmc_util/scriptsを確認してください。"
        )

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
        if existed:
            print(f"上書き: {target.name}")
        else:
            print(f"コピー: {target.name}")
        copied += 1
    return copied, skipped


def main() -> None:
    """--force指定時のみ既存の雛形を上書きする。"""
    arguments = sys.argv[1:]
    if arguments == ["--force"]:
        force = True
    elif not arguments:
        force = False
    else:
        print("使用方法: rmc_util-install [--force]", file=sys.stderr)
        raise SystemExit(2)

    copied, skipped = install_scripts(DESTINATION_DIRECTORY, force=force)
    print(f"完了: コピー {copied} 件、スキップ {skipped} 件")


if __name__ == "__main__":
    main()
