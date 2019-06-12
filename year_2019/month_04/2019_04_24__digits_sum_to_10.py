'''
April 24, 2019

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

# This problem is irksome to me, because a perfect number is a real thing,
# and this definition is not correct

# So here's the absolute brute force solution:
# Given that there is no spec, this is technically correct
# I might just leave it at that
def get_nth_perfect_number(n):
    if n <= 0:
        return None

    x = 0
    while n:
        x += 1
        if sum(map(int, str(x))) == 10:
            n -= 1

    return x

if __name__ == '__main__':
    import sys
    for x in map(int, sys.argv[1:]):
        print('{}: {}'.format(x, get_nth_perfect_number(x)))