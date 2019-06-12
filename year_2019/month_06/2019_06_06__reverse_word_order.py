'''
June 6, 2019

Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this
operation in-place?
'''

# since this is just a daily challenge problem, we'll assume "nice" inputs
def reverse_word_order(string):
    return ' '.join(reversed(string.split()))

def reverse_word_order_in_place(string_list):
    idx = 0
    for word in reversed(''.join(string_list).split()):
        for char in word:
            string_list[idx] = char
            idx += 1
        if idx < len(string_list):
            string_list[idx] = ' '
            idx += 1

if __name__ == '__main__':
    import sys
    string = ' '.join(sys.argv[1:])
    print('input string: {}'.format(string))
    result = reverse_word_order(string)
    print('result: {}'.format(result))
    string_list = list(string)
    reverse_word_order_in_place(string_list)
    result2 = ''.join(string_list)
    print('in-place result: {}'.format(result2))
    print('results equal: {}'.format(result == result2))
