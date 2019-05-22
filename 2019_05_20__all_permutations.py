'''
May 20, 2019

Given a number in the form of a list of digits, return all possible
permutations.

For example, given [1,2,3], return
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''

def get_all_permutations(input_list):
    return _get_all_permutations(input_list, [], [])

def _get_all_permutations(input_list, all_permutations, this_permutation):
    if not input_list:
        all_permutations.append(this_permutation)

    for idx, value in enumerate(input_list):
        all_permutations = _get_all_permutations(
            input_list[:idx] + input_list[idx + 1:],
            all_permutations,
            this_permutation + [value]
        )

    return all_permutations


if __name__ == '__main__':
    import sys
    input_list = sys.argv[1:]
    print('input list: {}'.format(input_list))
    print('result: {}'.format(get_all_permutations(input_list)))
