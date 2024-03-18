''' Main Python File, TBD '''
# --------------- imports   --------------- #
from __future__ import annotations

import logging
import sys

import coloredlogs
from core import _api_requests
from core import _print_dividers
from core._chrome_driver_settings import _driver
# from tests import _tests  # , _tests, _unitests
# import time
# import threading
# from selenium.webdriver.common.by import By

__author__ = 'Tzahi Cohen <mjhfvi@gmail.com>'

coloredlogs.install()
logger = logging.getLogger(name=__name__)
format = '[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s'  # "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%H:%M:%S', filename='logging.log', filemode='a')

# --------------- Main Function   --------------- #
SITE_URL = 'https://www.google.com/'  # 'https://www.google.com/' 'http://localhost:8080/login?from=%2F'


def main_script_driver():
    try:
        logger.info('Running Main Script Driver')
        # print(type(_driver()))

        # CHROME_DRIVER = _driver()  # Create Chrome Driver
        # print(CHROME_DRIVER)
        # from selenium import webdriver
        # CHROME_DRIVER = webdriver.Chrome()
        CHROME_DRIVER = _driver()
        # CHROME_DRIVER.get(SITE_URL)  # Navigate to the url

        # Get page title
        # CHROME_TITLE = CHROME_DRIVER.title
        # print('Chrome Title is:', CHROME_TITLE)

        # Find the search field element by its ID
        # CHROME_ELEMENT_NAME = 'SIvCob'  # FOR GOOGLE 'SIvCob', FOR JENKINS 'main-panel'
        # CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME)
        # CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME).text == "Google"

        # Find the search field element by its NAME
        # WEB_ELEMENT_NAME = 'q'
        # CHROME_ELEMENT = WEB_DRIVER.find_element(By.NAME, WEB_ELEMENT_NAME)

        main_script_run(CHROME_DRIVER, SITE_URL=SITE_URL)
        # main_script_run(CHROME_DRIVER=CHROME_DRIVER, CHROME_ELEMENT=CHROME_ELEMENT,
        # CHROME_ELEMENT_NAME=CHROME_ELEMENT_NAME, SITE_URL=SITE_URL)
    except Exception as ERROR:
        logger.error('An Unexpected error occurred', ERROR)


# def main_script_run(CHROME_DRIVER: str,
# CHROME_ELEMENT: str, CHROME_ELEMENT_NAME: str, SITE_URL):
def main_script_run(CHROME_DRIVER: object, SITE_URL):  # CHROME_ELEMENT: object, CHROME_ELEMENT_NAME: str,
    try:
        # Clearing the screen
        # os.system('cls')

        # running tests
        _print_dividers.main_start_dividers()

        # test website api
        _api_requests.test_api(SITE_URL)

        # run unitests class
        # _unitests._run_test_class(CHROME_DRIVER, SITE_URL)
        # _run_unitests = _unitests.SeleniumTest4Cases()
        # _run_unitests.setUp(CHROME_DRIVER=CHROME_DRIVER, SITE_URL=SITE_URL)
        # _unitests.SeleniumTestCases().runall(CHROME_DRIVER=CHROME_DRIVER, SITE_URL=SITE_URL)

        # _tests.SeleniumTestCases().__enter__(CHROME_DRIVER=CHROME_DRIVER, SITE_URL=SITE_URL)

        # test = _tests.SeleniumTestCases(SITE_URL=SITE_URL, CHROME_DRIVER=CHROME_DRIVER)
        # print(test.test_search_page_title)

        _print_dividers.main_end_dividers()
    except Exception as ERROR:
        logger.debug('An Unexpected error occurred', ERROR)
    finally:
        CHROME_DRIVER.quit()  # type: ignore


if __name__ == '__main__':
    try:
        main_script_driver()
        # _run_test_class()
        # help(sys.modules['__main__'])
    except Exception as ERROR:
        logger.debug('An Unexpected error occurred', ERROR)
    finally:
        print('======  End of Program  ======')
        logging.shutdown()
        sys.exit()
        # CHROME_DRIVER.quit()
