'''this is the tools folder, TBD'''
from __future__ import annotations

import logging

import coloredlogs

format = '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt=format)  # DEBUG, INFO, WARNING, ERROR, CRITICAL


logger.info(f"Initializing {__name__} Packages ...")
