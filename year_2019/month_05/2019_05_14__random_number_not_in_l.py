'''
May 14, 2019

Given an integer n and a list of integers l, write a function that randomly
generates a number from 0 to n-1 that isn't in l (uniform).
'''

import numpy as np

def random_number_not_in_l(n, l):
    return np.random.choice(list(set(range(n)) - set(l)))

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    l = list(map(int, sys.argv[2:]))
    print('n: {}'.format(n))
    print('l: {}'.format(l))
    counts = {}
    for _ in range(10000):
        x = random_number_not_in_l(n, l)
        counts[x] = counts.get(x, 0) + 1
    print('counts: {}'.format(counts))
