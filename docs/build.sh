#!/usr/bin/env bash
set -euo pipefail
DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DOCS_DIR/.." && pwd)"
PKG_DIR="$ROOT_DIR/src/rmc_util"
export PYTHONPATH="$ROOT_DIR/src${PYTHONPATH:+:$PYTHONPATH}"
if [ ! -d "$PKG_DIR" ]; then
    echo "Package source not found: $PKG_DIR" >&2
    exit 1
fi
for lang in en ja; do
    API_DIR="$DOCS_DIR/$lang/api/generated"
    mkdir -p "$API_DIR"
    find "$API_DIR" -maxdepth 1 -type f -name '*.rst' -delete
    sphinx-apidoc --force --module-first --separate --output-dir "$API_DIR" "$PKG_DIR"
    RMC_DOC_LANGUAGE="$lang" sphinx-build -b html -c "$DOCS_DIR" "$DOCS_DIR/$lang" "$DOCS_DIR/_build/html/$lang"
done
cp -a "$DOCS_DIR/_build/html/en/." "$DOCS_DIR/_build/html/"
touch "$DOCS_DIR/_build/html/.nojekyll"
