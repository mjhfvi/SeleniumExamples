''' define elements and find them '''
from __future__ import annotations

import sys

from termcolor import colored


def find_text(search_text: str, find_element: str, element_name: str):
    try:
        if search_text in find_element.text:  # type: ignore
            print(colored(f"The Element: {element_name}, Contains the Text: {
                  search_text}.", 'green', attrs=['bold'],))
            run_status = 'Pass'
            return run_status
        else:
            print(colored(f"The Element: {element_name}, Does Not Contain the Text: {
                  search_text}.", 'red', attrs=['bold'],))
            run_status = 'Failed'
            return run_status
    except NameError:
        print('An Unexpected error occurred in', __name__, 'page, with error:', NameError)


def find_title(title_name: str, find_element: str):
    try:
        if title_name in find_element.text:  # type: ignore
            print(colored(f"The Title Name Contains the Text: {
                  title_name}.", 'green', attrs=['bold'],))
            run_status = 'Pass'
            return run_status
        else:
            print(colored(f"The Title Name Does Not Contain the Text: {
                  title_name}.", 'red', attrs=['bold'],))
            run_status = 'Failed'
            return run_status
    except NameError:
        print('An Unexpected error occurred in', __name__, 'page, with error:', NameError)


if __name__ == '__main__':
    help(sys.modules['__main__'])
    print('End of File:', __name__)
    sys.exit()
