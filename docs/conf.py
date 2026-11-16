"""RMC_UTIL Sphinx documentation configuration."""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
project = "RMC_UTIL"
master_doc = "index"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
autosummary_generate = True
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = True
myst_enable_extensions = ["colon_fence", "dollarmath", "amsmath"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {"navigation_depth": 4, "titles_only": False}
exclude_patterns = ["_build", "_generated", "**/.DS_Store"]
