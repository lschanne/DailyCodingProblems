'''
June 16, 2019

Given a string, return whether it represents a number. Here are the different
kinds of numbers:
* "10", a positive integer
* "-10", a negative integer
* "10.1", a positive real number
* "-10.1", a negative real number
* "1e5", a number in scientific notation

And here are examples of non-numbers:
* "a"
* "x 1"
* "a -2"
* "-"
'''

import re

NUMBER_REGEX = re.compile(
    r'^(-?\d+(\.\d+)?)|(\de\d+)$'
)
def string_is_number(string):
    return bool(re.match(NUMBER_REGEX, string))

if __name__ == '__main__':
    import sys
    for string in sys.argv[1:]:
        print('string: "{}"'.format(string))
        print('is number: {}'.format(string_is_number(string)))
        print('--------------------------')
