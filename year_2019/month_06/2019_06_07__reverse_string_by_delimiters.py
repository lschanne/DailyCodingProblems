'''
June 7, 2019

Given a string and a set of delimiters, reverse the words in the string while
maintaining the relative order of the delimiters.

For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases:
    "hello/world:here/"
    "hello//world:here"
'''

import re

REGEX = re.compile(r'\W')

# the name is a little awkward, but I feel like this task is hard to summarize
# in a short name
# Also, the "Follow-up" section isn't very clearly defined. What is the
# expected result? Should "hello//world:here" treat "//" as a single
# delimiter or should it be split into two "/" delimiters? Right now I'm doing
# the latter. I feel like that makes more sense (maybe)
def reverse_string_by_delimiters(string):
    reversed_words = list(reversed(re.split(REGEX, string)))
    delimiters = re.findall(REGEX, string)
    result = reversed_words[0]
    for word, delimiter in zip(reversed_words[1:], delimiters):
        result = delimiter.join((result, word))
    return result

if __name__ == '__main__':
    import sys
    print('-----------------------')
    for string in sys.argv[1:]:
        print('string: "{}"'.format(string))
        print('result: "{}"'.format(reverse_string_by_delimiters(string)))
        print('-----------------------')
