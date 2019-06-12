'''
April 14, 2019

Given a multiset of integers, return whether it can be partitioned into two
subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return
true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which
both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't
split it up into two subsets that add up to the same sum.
'''

def can_get_same_sum_subsets(multiset, sum_A=0, sum_B=0, non_empty=False):
    if non_empty and sum_A == sum_B:
        return True

    for x in multiset:
        new_set = multiset - {x}
        if any((
            can_get_same_sum_subsets(new_set, sum_A, sum_B, True),
            can_get_same_sum_subsets(new_set, sum_A + x, sum_B, True),
            can_get_same_sum_subsets(new_set, sum_A, sum_B + x, True),
        )):
            return True

    return False

if __name__ == '__main__':
    import sys
    multiset = set(map(int, sys.argv[1:]))
    print('multiset: {}'.format(multiset))
    print('result: {}'.format(can_get_same_sum_subsets(multiset)))
