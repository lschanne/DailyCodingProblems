'''
March 29, 2019

We can determine how "out of order" an array A is by counting the number of
inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j]
but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than
O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has
three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten
inversions: every distinct pair forms an inversion.
'''

# slightly better than O(N^2)...
def array_inversion_count(arry):
    count = 0
    for iii, iii_value in enumerate(array):
        for jjj_value in array[iii + 1:]:
            if iii_value > jjj_value:
                count += 1

    return count

if __name__ == '__main__':
    import sys
    array = list(map(int, sys.argv[1:]))
    print('input array: {}'.format(array))
    print('inversion count: {}'.format(array_inversion_count(array)))
