'''
February 25, 2019

There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time.
'''

import math

def waysToClimb(N, X):
    X = list(sorted(X))
    result = 0
    counts = []
    return _waysToClimb(N, X, result, counts)

def _waysToClimb(N, X, result, counts):
    if not N:
        permutations = math.factorial(sum(counts))
        for c in counts:
            permutations /= math.factorial(c)
        result += permutations
        return result

    if not X:
        return result

    x = X[0]
    if len(X) == 1:
        if N % x == 0:
            result = _waysToClimb(0, [], result, counts + [N // x])
    else:
        for c in range(1 + N // x):
            result = _waysToClimb(N, X[1:], result, counts + [c])
            N -= x

    return result

if __name__ == '__main__':
    import sys
    X = list(map(int, sys.argv[1:]))
    N = X.pop(0) if X else 0
    result = waysToClimb(N, X)

    print('N: {}, X: {}'.format(N, X))
    print('result: {}'.format(result))