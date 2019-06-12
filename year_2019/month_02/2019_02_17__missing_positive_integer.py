'''
February 17, 2019

Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.


My first thought was to sort the array first, but that has time complexity
of O(n log n), so that doesn't fit the spec.
'''

def missingPositiveInteger_take1(inputs):
    '''
    So this was my first go. It has a few issues:
    - Time complexity > O(n)
    - Doesn't work on something like [1, 2] or [3, 2, 1]
    There could be more issues. I stopped determining edge cases
    after the aforementioned [1, 2] issue was established.
    '''
    result = 1
    first = True
    for x in sorted(inputs, reverse=True):
        if x <= 1:
            if first:
                result = 2
            break
        if result > x - 1 or first:
            first = False
            result = x - 1

    return result

def missingPositiveInteger_take2(inputs):
    '''
    This is definitely better than take1, but the sorting makes the
    time complexity O(n log n) > O(n).
    At least it actually works though.
    '''
    result = 1
    for x in sorted(inputs):
        if x < 1:
            continue
        if x == result:
            result += 1
        else:
            break
    return result

def missingPositiveInteger(inputs):
    # TODO: grow more brain cells
    pass

if __name__ == '__main__':
    import sys
    inputs = list(map(int, sys.argv[1:]))
    print('inputs: {}'.format(inputs))
    print('output: {}'.format(missingPositiveInteger(inputs)))
