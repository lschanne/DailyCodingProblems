'''
March 30, 2019

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
uniform probability, implement a function rand7() that returns an integer from
1 to 7 (inclusive).
'''

import numpy as np

def rand5():
    return np.random.randint(1, 6)

### FIXME: this implementation is garbage. Or at least it isn't uniform...
def rand7():
    result = 0
    for _ in range(7):
        result += rand5()

    return round(result / 5.0)

if __name__ == '__main__':
    count = {}
    for _ in range(10000):
        result = rand7()
        count[result] = count.get(result, 0) + 1

    print(count)
