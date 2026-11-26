# 1. Installation and preparation of execution scripts

The PyPI distribution name is `rmc-util`, while the Python import name is `rmc_util`.

```bash
pip install rmc-util
rmc_util install
```

`rmc_util install` places `rmc.py`, `rmc_init.py`, `config.yml`, and the plotting scripts in the working directory. Existing files are not overwritten; to explicitly overwrite them, use `rmc_util install --force`. Edit `config.yml` and `rmc_init.py` for your calculation, prepare the required initial structure and input data, and then execute:

```bash
python rmc.py
```

Execution is handled by `rmc_util.runners.run_rmc` within the package. Updating the package does not automatically replace files already deployed to the working directory.

See the [User Guide](../guide/software.md) for details.
