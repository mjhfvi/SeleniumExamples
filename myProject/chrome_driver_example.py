"""TBD"""
from __future__ import annotations

from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
print('\n============================================\nSelenium Starting Tests at: ', current_time,
      '\n============================================\n')

chrome_options = Options()

chrome_service = Service('C:/repository/SeleniumExamples/chromedriver.exe')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--remote-debugging-pipe')
# chrome_options.add_argument("--headless=new")  # disable starting browser
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')  # disabling extensions
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
chrome_options.add_argument('--disable-default-apps')
chrome_options.add_argument('--no-default-browser-check')
chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--profile-directory=Default")
# chrome_options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")
chrome_options.page_load_strategy = 'normal'

chrome_driver = webdriver.Chrome(
    options=chrome_options, service=chrome_service)
chrome_driver.refresh()
chrome_driver.minimize_window()

# Close the driver
print('\n\n============================================\nSelenium Tests Are Done at: ',
      current_time, '\nExiting....\n============================================\n')
sleep(2)
chrome_driver.quit()
