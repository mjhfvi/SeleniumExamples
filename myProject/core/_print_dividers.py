from __future__ import annotations

import sys
from datetime import datetime

from colorist import Color
# from time import sleep

# --------------- imports   --------------- #

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
# --------------- constants --------------- #


def main_start_dividers():
    try:
        print('=' * 30 + ' Selenium Started at: ', current_time, '=' * 30)
    except NameError:
        print('An Unexpected error occurred', NameError)


def main_end_dividers():
    try:
        print('=' * 30 + ' Selenium Ended at: ', current_time, '=' * 30)
    except NameError:
        print('An Unexpected error occurred', NameError)


def test_start_dividers(test_number='--'):
    try:
        print('\n' + '=' * 20, 'Test:', test_number, '=' * 20)
        print('Test Started at:', current_time, '\n' + '=' * 50)
    except NameError:
        print('An Unexpected error occurred', NameError)


def test_end_dividers(run_status='', test_number='--'):
    try:
        if run_status == 'Pass':
            print('\n' + '=' * 50)
            print(f'Test Ended with Status {Color.GREEN}{run_status}{Color.OFF} at: {current_time}')
            print('=' * 10, 'Test ' + test_number + ' Done, Exiting . . . ', '=' * 10)
        elif run_status == 'Failed':
            print('\n' + '=' * 50)
            print(f'Test Ended with Status {Color.RED}{run_status}{Color.OFF} at: {current_time}')
            print('=' * 10, 'Test ' + test_number + ' Done, Exiting . . . ', '=' * 10 + '\n')
        else:
            print('\n\n' + '=' * 50)
            print(f'{Color.RED}Tests Failed Unexpected at: {current_time}{Color.OFF}')
            print('=' * 50 + '\n')
    except NameError:
        print('An Unexpected error occurred', NameError)


if __name__ == '__main__':
    help(sys.modules['__main__'])
