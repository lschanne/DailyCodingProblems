'''
March 31, 2019

Given a string, find the longest palindromic contiguous substring. If there are
more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The
longest palindromic substring of "bananas" is "anana".
'''

def get_longest_palindromic_substring(string, substring='', result=''):
    if substring == substring[::-1] and len(substring) > len(result):
        result = substring

    if string:
        char = string[0]
        result = get_longest_palindromic_substring(
            string[1:],
            char,
            result
        )
        if substring:
            substring += char
            result = get_longest_palindromic_substring(
                string[1:],
                substring,
                result
            )

    return result

if __name__ == '__main__':
    import sys
    for string in sys.argv[1:]:
        print('input string: {}'.format(string))
        print('longest palindromic substring: {}'.format(
            get_longest_palindromic_substring(string)
        ))
        print('-------------------------------------------')
