'''
March 12, 2019

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

OPENER = 1
CLOSER = -1
def validate_string(string):
    count_dict = {}
    char_dict = {}
    for opener, closer in zip('([{', ')]}'):
        count_dict[opener] = 0
        char_dict[opener] = {'opener': opener, 'value': OPENER}
        char_dict[closer] = {'opener': opener, 'value': CLOSER}

    inner_chars = []
    for char in string:
        this_dict = char_dict.get(char)
        if this_dict:
            opener = this_dict['opener']
            value = this_dict['value']
            count_dict[opener] += value
            if value == OPENER:
                inner_chars.append(opener)

            if (
                count_dict < 0 or
                (value == CLOSER and opener != inner_chars.pop())
            ):
                return False

    return not any(count_dict.values())

if __name__ == '__main__':
    import sys
    for string in sys.argv[1:]:
        print('string: {}'.format(string))
        print('is valid: {}'.format(validate_string(string)))
        print('-------')
