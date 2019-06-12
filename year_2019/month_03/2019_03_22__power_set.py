'''
March 22, 2019

The power set of a set is the set of all its subsets. Write a function that,
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

# Ok yeah this is kind of cheating, but why reinvent the wheel?
from itertools import combinations

def get_powerset(input_set):
    powerset = []
    for n in range(len(input_set) + 1):
        powerset.extend(combinations(input_set, n))
    return powerset

if __name__ == '__main__':
    import sys
    input_set = set(sys.argv[1:])
    print('input set: {}'.format(input_set))
    print('power set: {}'.format(get_powerset(input_set)))
