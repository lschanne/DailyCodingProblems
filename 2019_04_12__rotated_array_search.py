'''
April 12, 2019

A sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than
linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4
(the index of 8 in the array).

You can assume all the integers in the array are unique.
'''

def search(rotated_array, element):
    if not rotated_array:
        return None

    left_idx = 0
    right_idx = len(rotated_array) - 1
    while True:
        idx = (left_idx + right_idx) // 2
        if rotated_array[idx] == element:
            return idx
        if left_idx == idx:
            if rotated_array[right_idx] == element:
                return right_idx
            return None

        if rotated_array[idx] > element:
            if rotated_array[left_idx] <= element:
                right_idx = idx
            else:
                left_idx = idx
        else:
            if rotated_array[right_idx] >= element:
                left_idx = idx
            else:
                right_idx = idx

if __name__ == '__main__':
    import sys
    rotated_array = list(map(int, sys.argv[1:]))
    for element in (
        [min(rotated_array) - 1] + rotated_array + [max(rotated_array) + 1]
    ):
        print('rotated array: {}'.format(rotated_array))
        print('element: {}'.format(element))
        print('index: {}'.format(search(rotated_array, element)))
        print('--------------------------------')
