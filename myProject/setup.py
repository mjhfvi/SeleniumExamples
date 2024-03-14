''' Main Python File, TBD '''
# --------------- imports   --------------- #
from __future__ import annotations

import sys

from colorist import Color
from core import _api_requests
from core import _print_dividers
from core._chrome_driver_settings import _driver
from selenium.webdriver.common.by import By
from tests import _unitests  # , _tests, _unitests
# import os
# from selenium.webdriver.support.wait import WebDriverWait


def main_script_driver() -> None:
    try:
        # 'https://www.google.com/' 'http://localhost:8080/login?from=%2F'
        SITE_URL = 'https://www.google.com/'
        CHROME_DRIVER = _driver()  # Create Chrome Driver
        CHROME_DRIVER.get(SITE_URL)  # Navigate to the url

        # Get page title
        # CHROME_TITLE = CHROME_DRIVER.title
        # print('CHROME_TITLE:', CHROME_TITLE)

        # Find the search field element by its ID
        CHROME_ELEMENT_NAME = 'SIvCob'  # FOR GOOGLE 'SIvCob', FOR JENKINS 'main-panel'
        CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME)
        # CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME).text == "Google"

        # Find the search field element by its NAME
        # WEB_ELEMENT_NAME = 'q'
        # CHROME_ELEMENT = WEB_DRIVER.find_element(By.NAME, WEB_ELEMENT_NAME)

        # main_script_run(CHROME_DRIVER, CHROME_ELEMENT='none',
        #                 CHROME_ELEMENT_NAME='none', SITE_URL=SITE_URL)
        main_script_run(CHROME_DRIVER=CHROME_DRIVER, CHROME_ELEMENT=CHROME_ELEMENT,
                        CHROME_ELEMENT_NAME=CHROME_ELEMENT_NAME, SITE_URL=SITE_URL)
    except Exception as ERROR:
        print(f"{Color.BLUE}{'DEBUG:'}{Color.OFF} An Unexpected error occurred, Folder: {
              Color.BLUE}{__name__}{Color.OFF},", ERROR)


# def main_script_run(CHROME_DRIVER: str,
# CHROME_ELEMENT: str, CHROME_ELEMENT_NAME: str, SITE_URL):
def main_script_run(CHROME_DRIVER: object, CHROME_ELEMENT: object, CHROME_ELEMENT_NAME: str, SITE_URL: object):
    try:
        # Clearing the screen
        # os.system('cls')

        # running tests
        _print_dividers.main_start_dividers()

        # test website api
        _api_requests.test_api(SITE_URL)

        # run unitests class
        # _unitests._run_test_class(CHROME_DRIVER, SITE_URL)
        # _run_unitests = _unitests.SeleniumTestCases()
        # _run_unitests.setUp(CHROME_DRIVER=CHROME_DRIVER, SITE_URL=SITE_URL)
        _unitests.SeleniumTestCases().runall(CHROME_DRIVER=CHROME_DRIVER, SITE_URL=SITE_URL)

        # _tests.run_tests(test_number='01', search_text='Jenkins', find_element=CHROME_ELEMENT,
        #                  element_name=CHROME_ELEMENT_NAME)
        # _tests.run_tests(test_number='02', search_text='Welcome!', find_element=CHROME_ELEMENT,
        #                  element_name=CHROME_ELEMENT_NAME)
        # _tests.run_tests(test_number='03', title_name='Google', find_element=CHROME_ELEMENT)
        # _tests.run_tests(test_number='04', title_name='Walla', find_element=CHROME_ELEMENT)
        # _tests._run_test_class(site_urls=SITE_URL)
        _print_dividers.main_end_dividers()
    except Exception as ERROR:
        print(f"{Color.BLUE}{'DEBUG:'}{Color.OFF} An Unexpected error occurred, Folder: {
              Color.BLUE}{__name__}{Color.OFF},", ERROR)
    finally:
        CHROME_DRIVER.quit()  # type: ignore


if __name__ == '__main__':
    main_script_driver()
    # _run_test_class()
    # help(sys.modules['__main__'])
    print('=== End of Program ===')
    sys.exit()
