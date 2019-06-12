'''
March 27, 2019

Given a list of integers S and a target number k, write a function that returns
a subset of S that adds up to k. If such a subset cannot be made, then return
null.

Integers can appear more than once in the list. You may assume all numbers in
the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
since it sums up to 24.
'''

def get_subset_by_sum(S, k, current_sum=0, subset=[]):
    if current_sum == k:
        return subset

    if not S or current_sum > k:
        return None

    x = S[0]
    if x + current_sum <= k:
        result = get_subset_by_sum(S[1:], k, current_sum + x, subset + [x])
        if result:
            return result

    return get_subset_by_sum(S[1:], k, current_sum, subset)

if __name__ == '__main__':
    import sys
    S = list(map(int, sys.argv[1:]))
    k = S.pop()
    print('S: {}'.format(S))
    print('k: {}'.format(k))
    print('result: {}'.format(get_subset_by_sum(S, k)))
