from __future__ import annotations

import logging
import sys

import coloredlogs
import requests
# import time

logger = logging.getLogger(__name__)
format = '%(asctime)s: %(message)s'
coloredlogs.install()


def test_api(WEBSITE_URL):
    try:
        response = requests.get(WEBSITE_URL, timeout=10)  # , verify=False
        # print(response)
        # print(SITE_URL)
        # print(response.status_code)

        if response.status_code == 200:
            logger.info('API Call Successful, Website is Reachable')
            test_status = 'Pass'
            return test_status
        else:
            logger.error('API Call Unsuccessful, Website is NOT Reachable, Killing Run')
            exit()
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


if __name__ == '__main__':
    help(sys.modules['__main__'])
    logger.info('End of File')
    sys.exit()
