#!/usr/bin/env bash
set -euo pipefail
DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DOCS_DIR/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/src/rmc_util"
OUTPUT_DIR="$DOCS_DIR/_build/html"
STAGING_DIR="$DOCS_DIR/_build/root_source"
if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "ERROR: Python package not found: $SOURCE_DIR" >&2
  exit 1
fi
export PYTHONPATH="$ROOT_DIR/src:${PYTHONPATH:-}"
rm -rf "$DOCS_DIR/_build"
for lang in en ja; do
  mkdir -p "$DOCS_DIR/$lang/api"
  find "$DOCS_DIR/$lang/api" -maxdepth 1 -name '*.rst' -delete
  sphinx-apidoc --force --module-first --no-toc -o "$DOCS_DIR/$lang/api" "$SOURCE_DIR"
  python "$DOCS_DIR/generate_api_index.py" "$DOCS_DIR/$lang/api" "$lang"
done
# Build the public root from docs/index.md with English content in a temporary source tree.
mkdir -p "$STAGING_DIR"
cp "$DOCS_DIR/index.md" "$STAGING_DIR/index.md"
cp -R "$DOCS_DIR/en/guide" "$DOCS_DIR/en/reference" "$DOCS_DIR/en/api" "$STAGING_DIR/"
sphinx-build -b html -D language=en -c "$DOCS_DIR" "$STAGING_DIR" "$OUTPUT_DIR"
for lang in en ja; do
  sphinx-build -b html -D language="$lang" -c "$DOCS_DIR" "$DOCS_DIR/$lang" "$OUTPUT_DIR/$lang"
done
