# Installation and working scripts

Install the published package:

```bash
pip install rmc-util
```

The PyPI distribution is named `rmc-util`; its Python import name is `rmc_util`.

```python
from rmc_util import RmcPot, RmcPotDat, RmcPotHst
```

To install a local checkout, run `pip install .` at the repository root.

To place the editable working scripts in the current directory:

```bash
rmc_util install
```

The command copies `rmc.py` and `rmc_init.py` without overwriting existing files. Use `rmc_util install --force` to request replacement. The installed scripts are not automatically updated when the Python package is upgraded.

The supplied source includes `install.py` but not the contents of the two distributed scripts. Consult those scripts in your checkout for their exact parameters.
