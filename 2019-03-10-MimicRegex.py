'''
March 10, 2019

Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.

For example, given the regular expression "ra." and the string "ray", your
function should return true. The same regular expression on the string
"raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should
return true. The same regular expression on the string "chats" should return
false.
'''

REGEX_TOKENS = {
    'wildcard': '.',
    'repeat': '*',
    'escape': '/',
}

def re_match(regex, string):
    regex_idx = 0
    regex_char = ''
    is_wild = False
    regex_len = len(regex)
    repeat = False
    idx = 0
    while idx < len(string):
        if not repeat:
            is_wild = False
            if regex_idx >= regex_len:
                # this will cause a False return on the next iteration
                # (if there is a next iteration)
                regex_char = ''
            else:
                regex_char = regex[regex_idx]
                if regex_char == REGEX_TOKENS['wildcard']:
                    is_wild = True
                elif regex_char == REGEX_TOKENS['escape']:
                    regex_idx += 1
                    if regex_idx == regex_len:
                        # ending on an escape character is not valid
                        return False
                    regex_char = regex[regex_idx]

                if (
                    regex_idx + 1 < regex_len and
                    regex[regex_idx + 1] == REGEX_TOKENS['repeat']
                ):
                    # skip over the wildcard character
                    regex_idx += 1
                    repeat = True
                else:
                    repeat = False
            regex_idx += 1

        # the asterisk is hard to handle if the next character in the regex
        # is a valid match for the current, so we just recurse
        if repeat and re_match(regex[regex_idx + 1:], string[idx:]):
            return True

        char = string[idx]
        if char != regex_char and not is_wild:
            if not repeat:
                # character does not match
                return False
            repeat = False
        else:
            idx += 1

    # need to ensure the entire regex was used in the match
    return regex_idx == regex_len

if __name__ == '__main__':
    import sys
    regex, string = sys.argv[1:]
    print('regex: {}'.format(regex))
    print('string: {}'.format(string))
    print('is_match: {}'.format(re_match(regex, string)))
