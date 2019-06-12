'''
April 11, 2019

Given a string s and an integer k, break up the string into multiple lines such
that each line has a length of k or less. You must break it up so that words
don't break across lines. Each line has to have the maximum possible amount of
words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog"
and k = 10, you should return:
    ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
No string in the list has a length of more than 10.
'''

def line_break(string, k):
    result = []
    current_line = ''
    for word in string.split():
        if len(word) > k:
            return None

        if not current_line:
            current_line = word
        elif len(word) + 1 + len(current_line) <= k:
            current_line = ' '.join((current_line, word))
        else:
            result.append(current_line)
            current_line = word

    result.append(current_line)

    return result

if __name__ == '__main__':
    import sys
    k = int(sys.argv[1])
    for string in sys.argv[2:]:
        print('input string: {}'.format(string))
        print('k: {}'.format(k))
        print('result: {}'.format(line_break(string, k)))
        print('---------------------------------')
