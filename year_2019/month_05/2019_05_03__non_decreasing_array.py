'''
May 3, 2019

Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any
one element to get a non-decreasing array.
'''

MAX_MODIFICATIONS = 1

def can_become_non_decreasing(array):
    modifications = 0
    prev_idx = 0
    for idx in range(1, len(array)):
        if (
            array[prev_idx] <= array[idx] and (
                idx + 1 == len(array) or
                array[idx] <= array[idx + 1]
            )
        ):
            prev_idx = idx
        else:
            modifications += 1
            if modifications > MAX_MODIFICATIONS:
                return False
            if (
                idx + 1 == len(array) or
                array[prev_idx] <= array[idx + 1]
            ):
                pass
            else:
                prev_idx = idx
    return True

if __name__ == '__main__':
    # I don't know if this is comprehensive enough, but I can't immediately
    # think of any more cases that would break the code
    for array, expected in (
        ([1, 5, 2, 3], True),
        ([10, 5, 1], False),
        ([1, 5, 2], True),
        ([10, 5, 7], True),
        ([1, 2, 1, 2], False),
        ([10, 1, 2, 3, 1], False),
    ):
        print('array: {}'.format(array))
        print('expected: {}'.format(expected))
        result = can_become_non_decreasing(array)
        print('actual: {}'.format(result))
        print('test passed: {}'.format(result == expected))
        print('----------------------------------')
