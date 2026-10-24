#!/usr/bin/env bash
set -euo pipefail

DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DOCS_DIR/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/src/rmc_util"
BUILD_DIR="$DOCS_DIR/_build"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "ERROR: Python package not found: $SOURCE_DIR" >&2
  exit 1
fi

export PYTHONPATH="$ROOT_DIR/src:${PYTHONPATH:-}"

# Generate API documentation separately for the English and Japanese sites.
sphinx-apidoc --force --module-first --no-toc -o "$DOCS_DIR/en/api/generated" "$SOURCE_DIR"
sphinx-apidoc --force --module-first --no-toc -o "$DOCS_DIR/ja/api/generated" "$SOURCE_DIR"

# Each language is a separate Sphinx project with its own index and sidebar.
sphinx-build -b html -c "$DOCS_DIR" -D language=en "$DOCS_DIR/en" "$BUILD_DIR/html/en"
sphinx-build -b html -c "$DOCS_DIR" -D language=ja "$DOCS_DIR/ja" "$BUILD_DIR/html/ja"

# Build the default English landing page from docs/index.md.
# The root document links to the two independently built language sites.
sphinx-build -b html -c "$DOCS_DIR" -D language=en "$DOCS_DIR" "$BUILD_DIR/root"
cp "$BUILD_DIR/root/index.html" "$BUILD_DIR/html/index.html"
