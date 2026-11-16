# 1. Installation and preparation of execution scripts

The PyPI distribution name is `rmc-util`, while the Python import name is `rmc_util`.

```bash
pip install rmc-util
rmc_util install
```

`rmc_util install` places `rmc.py` and `rmc_init.py` in the working directory. Existing files are not overwritten; to explicitly overwrite them, use `rmc_util install --force`. Edit `rmc_init.py`, prepare the required initial structure and input data, and then execute:

```bash
python rmc.py
```

Execution is handled by `rmc_util.runners.run_rmc` within the package. Updating the package does not automatically update changes made to an already deployed `rmc_init.py`.

See the [User Guide](../guide/software.md) for details.
