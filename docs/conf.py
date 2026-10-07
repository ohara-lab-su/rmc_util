from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

project = "rmc_util"
language = "ja"
root_doc = "index"
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autosummary_generate = True
myst_enable_extensions = ["colon_fence", "dollarmath", "amsmath"]
html_theme = "sphinx_rtd_theme"
exclude_patterns = ["_build", "_generated"]
