'''
March 18, 2019

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:
    2
    1.5
    2
    3.5
    2
    2
    2
'''

import bisect

def print_running_median(numbers):
    even = True
    sorted_list = []
    idx = 0
    for num in numbers:
        bisect.insort_left(sorted_list, num)
        even = not even
        if even:
            idx += 1
            median = (sorted_list[idx] + sorted_list[idx - 1]) / 2.0
        else:
            # just casting to float so that the print-out is consistent
            median = float(sorted_list[idx])
        print(median)

if __name__ == '__main__':
    import sys
    numbers = list(map(int, sys.argv[1:]))
    print('input list: {}'.format(numbers))
    print_running_median(numbers)
