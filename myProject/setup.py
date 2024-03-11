''' Main Python File, TBD '''
# --------------- imports   --------------- #
from __future__ import annotations

from core import api_requests
from core import chrome_driver_settings as driver
from core import find_elements
from core import print_dividers
from selenium.webdriver.common.by import By
# from tests import tests
# import sys

# --------------- constants --------------- #

SITE_URL = 'https://www.google.com/'
CHROME_DRIVER = driver._driver()

# Navigate to the url
CHROME_DRIVER.get(SITE_URL)

# Find the search field element by its ID
CHROME_ELEMENT_NAME = 'SIvCob'
CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME)

# Find the search field element by its NAME
# CHROME_ELEMENT_NAME = 'q'
# CHROME_ELEMENT = CHROME_DRIVER.find_element(By.NAME, CHROME_ELEMENT_NAME)

# Get page title
# CHROME_TITLE = CHROME_DRIVER.title

# --------------- print tests --------------- #

print_dividers.main_start_dividers()

api_requests.test_api(SITE_URL)
# tests.run_tests()

print_dividers.test_start_dividers(test_number='01')
test_status = find_elements.find_text(search_text='Google', find_element=CHROME_ELEMENT,
                                      element_name=CHROME_ELEMENT_NAME)
print_dividers.test_end_dividers(test_status)

print_dividers.test_start_dividers(test_number='02')
test_status = find_elements.find_title(title_name='Google', find_element=CHROME_ELEMENT)
print_dividers.test_end_dividers(test_status)

# print_dividers.test_start_dividers(test_number='03')
# test_status = find_elements.find_text(search_text='Google', find_element=CHROME_ELEMENT,
#                                       element_name=CHROME_ELEMENT_NAME)
# print_dividers.test_end_dividers(test_status)

# print_dividers.test_start_dividers(test_number='04')
# test_status = find_elements.find_text(search_text='Welcome!', find_element=CHROME_ELEMENT,
#                                       element_name=CHROME_ELEMENT_NAME)
# print_dividers.test_end_dividers(test_status)

# print_dividers.test_start_dividers(test_number='05')
# test_status = find_elements.find_title(title_name='Google', find_element=CHROME_ELEMENT)
# print_dividers.test_end_dividers(test_status)

# print_dividers.test_start_dividers(test_number='06')
# test_status = find_elements.find_title(title_name='Walla', find_element=CHROME_ELEMENT)
# print_dividers.test_end_dividers(test_status)


# --------------- end --------------- #
# if __name__ == '__main__':
#     help(sys.modules['__main__'])

# sleep(1)
print_dividers.main_end_dividers()
CHROME_DRIVER.quit()
