#!/usr/bin/env bash
set -euo pipefail
DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DOCS_DIR/.." && pwd)"
export PYTHONPATH="$ROOT_DIR/src:${PYTHONPATH:-}"
mkdir -p "$DOCS_DIR/api"
sphinx-apidoc --force --module-first -o "$DOCS_DIR/api" "$ROOT_DIR/src/rmc_util"
sphinx-build -b html "$DOCS_DIR" "$DOCS_DIR/_build/html"
