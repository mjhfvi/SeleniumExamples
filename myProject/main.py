"""TBD"""
from __future__ import annotations

from time import sleep

import chrome_driver_example
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

chrome_driver_example.chrome_driver.get('https://www.google.com/')
sleep(2)
chrome_driver_example.chrome_driver.quit()
print('Test is Done!!!\nExiting...')
