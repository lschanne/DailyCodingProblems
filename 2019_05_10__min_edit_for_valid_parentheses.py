'''
May 10, 2019

Given a string of parentheses, write a function to compute the minimum number
of parentheses to be removed to make the string valid (i.e. each open
parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
'''

def min_edit_for_valid_parentheses(string):
    balance = 0
    count = 0
    for char in string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                balance = 0
                count += 1

    balance += count
    return balance

if __name__ == '__main__':
    import sys
    for string in sys.argv[1:]:
        print('input string: {}'.format(string))
        print(
            'minimum number of parentheses to be removed: {}'.format(
                min_edit_for_valid_parentheses(string)
            )
        )
        print('------------------------------------------')
