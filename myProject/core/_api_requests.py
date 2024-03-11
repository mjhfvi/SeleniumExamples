from __future__ import annotations

import requests
from termcolor import colored


def test_api(SITE_URL):
    try:
        response = requests.get(SITE_URL, timeout=10)  # , verify=False
        # print(response)
        # print(SITE_URL)
        # print(response.status_code)

        if response.status_code == 200:
            print(colored('API Call Successful, Website is Reachable, Starting Tests',
                  'green', attrs=['bold'],))
            test_status = 'Pass'
            return test_status
        else:
            print(colored('API Call Unsuccessful, Website is NOT Reachable, Killing Run\n',
                  'red', attrs=['bold'],))
            exit()
    except NameError:
        print('Variable x is not defined')
