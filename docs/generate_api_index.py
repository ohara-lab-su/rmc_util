"""Generate MyST API navigation from sphinx-apidoc module pages."""
from pathlib import Path
import sys

API_DIR: Path = Path(sys.argv[1])
LANGUAGE: str = sys.argv[2]


def main() -> None:
    pages: list[str] = sorted(path.stem for path in API_DIR.glob('*.rst') if path.stem not in {'index', 'modules'})
    heading: str = 'APIリファレンス' if LANGUAGE == 'ja' else 'API Reference'
    lines: list[str] = [f'# {heading}', '', '```{toctree}', ':maxdepth: 2', '']
    lines.extend(pages)
    lines.extend(['```', ''])
    (API_DIR / 'index.md').write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    main()
