'''
March 3, 2019

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:
    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place
and you do not need to store the results. You can simply print them out as you
compute them.
'''

# Very naive solution. Works fine, but slow and spacious
def get_max_subarray_values_naive(array, k):
    sub_array = []
    for x in array:
        sub_array.append(x)
        if len(sub_array) > k:
            sub_array.pop(0)
        if len(sub_array) == k:
            print(max(sub_array))

# Python program to find the maximum for
# each and every contiguous subarray of
# size k

from collections import deque

# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size k
# sauce: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
def get_max_subarray_values(array, k):
    n = len(array)

    """ Create a Double Ended Queue, Qi that
    will store indexes of array elements.
    The queue will store indexes of useful
    elements in every window and it will
    maintain decreasing order of values from
    front to rear in Qi, i.e., array[Qi.front[]]
    to array[Qi.rear()] are sorted in decreasing
    order"""
    Qi = deque()

    # Process first k (or first window)
    # elements of array
    for i in range(k):

        # For every element, the previous
        # smaller elements are useless
        # so remove them from Qi
        while Qi and array[i] >= array[Qi[-1]]:
            Qi.pop()

        # Add new element at rear of queue
        Qi.append(i)

    # Process rest of the elements, i.e.
    # from array[k] to array[n-1]
    for i in range(k, n):

        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        print(array[Qi[0]])

        # Remove the elements which are
        # out of this window
        while Qi and Qi[0] <= i - k:
            # remove from front of deque
            Qi.popleft()

        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while Qi and array[i] >= array[Qi[-1]]:
            Qi.pop()

        # Add current element at the rear of Qi
        Qi.append(i)

    # Print the maximum element of last window
    print(array[Qi[0]])

if __name__ == '__main__':
    import sys
    array = list(map(int, sys.argv[1:]))
    k = array.pop(0)
    print('k: {:.0f}'.format(k))
    print('array: {}'.format(array))
    get_max_subarray_values(array, k)
