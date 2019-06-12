'''
April 3, 2019

Given an array of numbers, find the maximum sum of any contiguous subarray of
the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would
be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would
not take any elements.

Do this in O(N) time.
'''

def get_max_sum(array):
    max_sum = 0
    current_sum = 0
    for value in array:
        current_sum += value
        if current_sum < 0:
            current_sum = 0
        elif current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == '__main__':
    import sys
    array = list(map(int, sys.argv[1:]))
    print('input array: {}'.format(array))
    print('max sum of any contiguous subarray: {}'.format(get_max_sum(array)))
