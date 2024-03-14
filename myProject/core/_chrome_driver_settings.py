''' chrome driver folder, TBD '''
from __future__ import annotations

import sys

from colorist import Color
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# --------------- imports   --------------- #

# CHROME_PATH = 'C:/repository/SeleniumExamples/chromedriver.exe'
CHROME_PATH = 'C:/repository/SeleniumExamples/myProject/tools/chromedriver.exe'
USER_DATA_DIR = 'C:/Temp/SeleniumChromeProfile'
# --------------- constants --------------- #


def _driver():
    ''' Help chrome_driver Module: no arg yet, TBD ...'''
    print(f"{Color.BLUE}{'DEBUG:'}{Color.OFF} Building Chrome Driver: {
          Color.BLUE}{__name__}{Color.OFF}")
    # from selenium import webdriver
    chrome_options = Options()
    chrome_service = Service(CHROME_PATH)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument('--disable-dev-shm-usage')  # disable shared memory, for Linux
    # chrome_options.add_argument('--remote-debugging-pipe=chrome_pipe')  #  debug Chrome remotely
    # chrome_options.add_argument('--remote-debugging-port=9222')  #  debug Chrome remotely
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
    # disable the default browser check on startup
    chrome_options.add_argument('--no-default-browser-check')
    # bypass certificate errors to HTTPS or self-signed cert
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--disable-extensions')  # disabling extensions
    chrome_options.add_argument('--disable-plugins')
    # disable the default apps that are bundled with Chrome
    chrome_options.add_argument('--disable-default-apps')
    # specify the directory where user profiles are stored
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--lang=en-US')
    # chrome_options.add_argument('--user-data-dir=C:\\Temp\\SeleniumChromeProfile')
    chrome_options.add_argument('--profile-directory=Profile 1')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--headless=new')  # disable starting browser
    # normal(default), eager, none(Does not block WebDriver at all)
    chrome_options.page_load_strategy = 'none'

    chrome_driver = webdriver.Chrome(
        options=chrome_options, service=chrome_service, keep_alive=False)
    chrome_driver.refresh()
    chrome_driver.minimize_window()
    chrome_driver.implicitly_wait(10)
    return chrome_driver


if __name__ == '__main__':
    help(sys.modules['__main__'])
    print(f"End of File:  {Color.BLUE}{__name__}{Color.OFF}")
    sys.exit()
