'''
March 19, 2019

Given a string, find the palindrome that can be made by inserting the fewest
number of characters as possible anywhere in the word. If there is more than
one palindrome of minimum length that can be made, return the lexicographically
earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can
add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three
letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

def make_palindrome(string):
    n = len(string)
    for idx in range(n):
        left, right = map(is_palindrome, (string[idx:], string[:n - idx]))
        if left or right:
            break
    else:
        left = right = True
        idx += 1

    if left and right:
        palindrome = min(
            string + string[:idx][::-1],
            string[n - idx:][::-1] + string
        )
    elif left:
        palindrome = string + string[:idx][::-1]
    elif right:
        palindrome = string[n - idx:][::-1] + string

    return palindrome


def is_palindrome(string):
    return string == string[::-1]

if __name__ == '__main__':
    import sys
    for string in sys.argv[1:]:
        print('input string: {}'.format(string))
        print('smallest palindrome: {}'.format(make_palindrome(string)))
        print('-------------------------------------')
