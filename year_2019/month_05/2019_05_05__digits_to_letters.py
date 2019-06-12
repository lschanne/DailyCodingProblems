'''
May 5, 2019

Given a mapping of digits to letters (as in a phone number), and a digit
string, return all possible letters the number could represent. You can assume
each valid number in the mapping is a single digit.

For example if {"2", ["a", "b", "c"], 3: ["d", "e", "f"], ...} then "23" should
return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

# We'll assume the mapping as a global constant
DIGIT_MAP = {
    '1': ['a', 'b', 'c'],
    '2': ['d', 'e', 'f'],
    '3': ['g', 'h', 'i'],
    '4': ['j', 'k', 'l'],
    '5': ['m', 'n', 'o'],
    '6': ['p', 'q', 'r'],
    '7': ['s', 't', 'u'],
    '8': ['v', 'w', 'x'],
    '9': ['y', 'z', '.'],
}

'''
So I wrote this with a call to a separate function because when I tried to
write as one function with
def digits_to_letters(digits, current='', result=[]):
The result list was carrying over from one call to the next instead of
creating a new list. I guess I could also just use a sentinel value.
'''
def digits_to_letters(digits):
    return _recurse(digits, '', [])

def _recurse(digits, current, result):
    if not digits:
        result.append(current)
        return result

    digit = digits[0]
    for letter in DIGIT_MAP.get(digit, digit):
        result = _recurse(digits[1:], current + letter, result)

    return result

if __name__ == '__main__':
    import sys
    for digits in sys.argv[1:]:
        print('input string: {}'.format(digits))
        print('output string: {}'.format(digits_to_letters(digits)))
        print('-----------------------------------')
