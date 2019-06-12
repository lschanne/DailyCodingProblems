'''
May 28, 2019

Deterimine whether a doubly linked list is a palindrome. What if it's singly
linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
'''

def is_palindromic_list(input_list):
    # this what if is a little funny, because you could of course just write
    # the singly linked list to a doubly linked list or to a string or any
    # object that is easily reversibles. Is that cheating? idk
    return input_list == input_list[::-1]

if __name__ == '__main__':
    import sys
    input_list = sys.argv[1:]
    print('input list: {}'.format(input_list))
    print('is a palindrome: {}'.format(is_palindromic_list(input_list)))
