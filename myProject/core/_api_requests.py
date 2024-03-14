from __future__ import annotations

import sys

import requests
from termcolor import colored


def test_api(WEBSITE_URL):
    try:
        response = requests.get(WEBSITE_URL, timeout=10)  # , verify=False
        # print(response)
        # print(SITE_URL)
        # print(response.status_code)

        if response.status_code == 200:
            print(colored('API Call Successful, Website is Reachable, Starting Tests\n',
                  'green', attrs=['bold'],))
            test_status = 'Pass'
            return test_status
        else:
            print(colored('API Call Unsuccessful, Website is NOT Reachable, Killing Run\n',
                  'red', attrs=['bold'],))
            exit()
    except NameError:
        print('An Unexpected error occurred in', __name__, 'page, with error:', NameError)


if __name__ == '__main__':
    help(sys.modules['__main__'])
    print('End of File:', __name__)
    sys.exit()
