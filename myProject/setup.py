''' Main Python File, TBD '''
# --------------- imports   --------------- #
from __future__ import annotations

import sys

from core import _api_requests
from core import _chrome_driver_settings
from core import _print_dividers
from selenium.webdriver.common.by import By
from tests import tests
# import os

# --------------- constants --------------- #
SITE_URL = 'http://localhost:8080/login?from=%2F'  # 'https://www.google.com/'
CHROME_DRIVER = _chrome_driver_settings._driver()
# Navigate to the url
CHROME_DRIVER.get(SITE_URL)

# Find the search field element by its ID
CHROME_ELEMENT_NAME = 'main-panel'  # FOR GOOGLE 'SIvCob'
CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME)

# Find the search field element by its NAME
# WEB_ELEMENT_NAME = 'q'
# CHROME_ELEMENT = WEB_DRIVER.find_element(By.NAME, WEB_ELEMENT_NAME)

# Get page title
# CHROME_TITLE = WEB_DRIVER.title

# --------------- print tests --------------- #
# Clearing the screen
# os.system('cls')
# print(CHROME_ELEMENT)

# running tests
_print_dividers.main_start_dividers()

_api_requests.test_api(SITE_URL)
# tests.run_tests()

tests.run_tests(test_number='01', search_text='Jenkins',
                find_element=CHROME_ELEMENT, element_name=CHROME_ELEMENT_NAME)
# tests.run_tests(test_number='02', search_text='Welcome!',
#                 find_element=CHROME_ELEMENT, element_name=CHROME_ELEMENT_NAME)

# tests.run_tests(test_number='03', title_name='Google', find_element=CHROME_ELEMENT)
# tests.run_tests(test_number='04', title_name='Walla', find_element=CHROME_ELEMENT)

# tests._run_test_class(site_urls=SITE_URL)
# --------------- end --------------- #

# sleep(1)
_print_dividers.main_end_dividers()
CHROME_DRIVER.quit()

if __name__ == '__main__':
    sys.exit()
