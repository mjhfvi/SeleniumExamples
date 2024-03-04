'''
Source:
https://pythonexamples.org/python-selenium-check-if-element-has-specific-text/
'''
from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup chrome driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-9.html')

# Get the element
element = driver.find_element(By.ID, 'msg')


def find_text(search_text):
    if search_text in element.text:
        print(f"The element contains the {search_text}.")
    else:
        print(f"The element does not contain the search text: {search_text}.")


print('printing the full element: ', element.text, '\n')

find_text('paragraph')
find_text('Welcome!')

# Close the driver
driver.quit()
