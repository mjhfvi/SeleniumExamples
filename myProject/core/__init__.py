'''this is the core folder, TBD'''
# https://docs.python.org/3/library/logging.html#logging-levels
from __future__ import annotations

import logging

import coloredlogs

coloredlogs.install()
logger = logging.getLogger(name=__name__)

logger.info(f"Initializing {__name__} Packages ...")

# logging.DEBUG
# Detailed information, typically only of interest to a developer trying to diagnose a problem.

# logging.INFO
# Confirmation that things are working as expected.

# logging.WARNING
# An indication that something unexpected happened,
# or that a problem might occur in the near future (e.g. ‘disk space low’).
# The software is still working as expected.

# logging.ERROR
# Due to a more serious problem, the software has not been able to perform some function.

# logging.CRITICAL
# A serious error, indicating that the program itself may be unable to continue running.
