#!/usr/bin/env python3
"""RMC計算の起動スクリプト。計算条件は rmc_init.py で編集する。"""

import sys

from x_logger import XLogger

from rmc_util import Config, RmcPotDat, RmcPotLog
from rmc_util.runners.run_rmc import run_rmc
from rmc_init import run_rmc_init

if __name__ == "__main__":
    logger = XLogger(
        log_level="debug",
        logger_name="rmc.py",
    )
    config = Config("config.yml")
    msg = None

    # 初期構造を作成する場合は、必要に応じてここに処理を追加する。
    # shutil.copy("POSCAR0", "POSCAR")
    # poscar2cfg(cfg_name=config.cfg_name)

    rmc_log = RmcPotLog(
        cfg_name=config.cfg_name,
        logger=logger,
    )
    rmc_dat = RmcPotDat(
        config=config,
        logger=logger,
    )

    # 作業ディレクトリの編集可能な計算条件を適用する。
    run_rmc_init(
        config=config,
        rmc_dat=rmc_dat,
        logger=logger,
    )

    try:
        run_rmc(
            config=config,
            rmc_log=rmc_log,
            rmc_dat=rmc_dat,
            rmc_pot=None,
            auto_converge=False,
            postprocess=True,
            msg=msg,
            logger=logger,
        )
    except KeyboardInterrupt:
        logger.warning("[rmc] Exit by Ctrl+C.")
        sys.exit(130)
