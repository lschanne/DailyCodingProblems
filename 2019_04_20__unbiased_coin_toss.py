'''
April 20, 2019

Assume you have access to a function toss_biased() which returns 0 or 1 with a
probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the
bias of the coin.

Write a function to simulate an unbiased coin toss.
'''

import numpy as np

pA = np.random.uniform()
def toss_biased():
    return np.random.choice([0, 1], p=[pA, 1 - pA])
'''
Let probability of a head be given as P(A). Then the probability of a tail
is P(B). P(A) = 1 - P(B). Each flip is independent.
Therefore, P(A then B) === P(B then A).
So we can flip until we get either a head followed by a tail or we get a tail
followed by a head. We then arbitrarily map the first event to a head and the
second event to a tail for a 50-50 distribution.
'''
def toss_unbiased():
    while 1:
        A, B = toss_biased(), toss_biased()
        if A > B:
            return 0
        if B > A:
            return 1

if __name__ == '__main__':
    counts = [0, 0]
    for _ in range(100000):
        counts[toss_unbiased()] += 1
    print(counts)
    # [49902, 50098] -- pretty close