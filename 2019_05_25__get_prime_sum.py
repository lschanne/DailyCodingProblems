'''
May 25, 2019

Given an even number (greater than 2), return two prime numbers whose sum will
be equal to the given number.

A solution will always exist (see Goldbach's conjecture).

Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically
smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution
with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d.
'''

def get_prime_sum(x):
    if x <= 2 or x % 2:
        raise ValueError(
            'Input to get_prime_sum must be a an even number greater than 2.'
        )

    a = 2
    b = x - a
    while a:
        if is_prime(a) and is_prime(b):
            return (a, b)
        a += 1
        b -= 1

def is_prime(x):
    return all(x % n for n in range(2, 1 + x // 2))

if __name__ == '__main__':
    import sys
    for x in map(int, sys.argv[1:]):
        a, b = get_prime_sum(x)
        print('{} + {} = {}'.format(a, b, x))
