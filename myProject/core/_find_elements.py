''' define elements and find them '''
from __future__ import annotations

from termcolor import colored


def find_text(search_text, find_element, element_name):
    try:
        if search_text in find_element.text:
            print(colored(f"The Element {element_name} Contains the Text: {
                  search_text}.", 'green', attrs=['bold'],))
            run_status = 'Pass'
            return run_status
        else:
            print(colored(f"The Element {element_name} Does Not Contain the Text: {
                  search_text}.", 'red', attrs=['bold'],))
            run_status = 'Failed'
            return run_status
    except NameError:
        print('An Unexpected error occurred', NameError)


def find_title(title_name, find_element):
    try:
        if title_name in find_element.text:
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
        print('An Unexpected error occurred', NameError)
