'''
April 25, 2019

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
uniform probability, implement a function rand5() that returns an integer
from 1 to 5 (inclusive).
'''

import numpy as np

def rand7():
    return np.random.randint(low=1, high=8)

def rand5():
    while True:
        x = rand7()
        if 1 <= x <= 5:
            return x

if __name__ == '__main__':
    counts = {}
    for _ in range(10000):
        x = rand5()
        counts[x] = counts.get(x, 0) + 1
    print(counts)
    # {1: 1960, 2: 2068, 3: 1972, 4: 2048, 5: 1952}
