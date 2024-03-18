''' define elements and find them '''
from __future__ import annotations

import logging
import sys

import coloredlogs
# import time

coloredlogs.install()
logger = logging.getLogger(name=__name__)
# format = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"  # "%(asctime)s: %(message)s"
# logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S", filename='logging.log', filemode='a')


def find_text(search_text: str, find_element: str, element_name: str):
    try:
        if search_text in find_element.text:  # type: ignore
            logger.info(f"The Element: {element_name}, Contains the Text: {search_text}.")
            run_status = 'Pass'
            return run_status
        else:
            logger.info(f"The Element: {element_name}, Does Not Contain the Text: {search_text}.")
            run_status = 'Failed'
            return run_status
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


def find_title(title_name: str, find_element: str):
    try:
        if title_name in find_element.text:  # type: ignore
            logger.info(f"The Title Name Contains the Text: {title_name}.")
            run_status = 'Pass'
            return run_status
        else:
            logger.info(f"The Title Name Does Not Contain the Text: {title_name}.")
            run_status = 'Failed'
            return run_status
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


if __name__ == '__main__':
    help(sys.modules['__main__'])
    logger.info('End of File')
    sys.exit()
