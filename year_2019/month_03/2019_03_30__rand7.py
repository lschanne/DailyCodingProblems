'''
March 30, 2019

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
uniform probability, implement a function rand7() that returns an integer from
1 to 7 (inclusive).
'''

import numpy as np

def rand5():
    return np.random.randint(1, 6)

# So we basically just need to devise 7 scenarios using rand5() that are
# equally likely and then arbitrarily map the numbers 1 to 7 to those
# scenarios
# She's not the prettiest bit of code I've ever written, but it definitely
# works
def rand7():
    while True:
        x, y = rand5(), rand5()
        if x == 1:
            if y <= 3:
                return 1
            return 2
        if x == 2:
            if y == 1:
                return 2
            if y <= 4:
                return 3
            return 4
        if x == 3:
            if y <= 2:
                return 4
            return 5
        if x == 4:
            if y <= 3:
                return 6
            return 7
        if x == 5:
            if y == 1:
                return 7

if __name__ == '__main__':
    count = {}
    for _ in range(10000):
        result = rand7()
        count[result] = count.get(result, 0) + 1

    print(count)
    # {1: 1414, 2: 1437, 3: 1434, 4: 1464, 5: 1398, 6: 1436, 7: 1417}
    # Nice.
