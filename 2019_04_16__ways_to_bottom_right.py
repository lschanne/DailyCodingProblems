'''
April 16, 2019

There is an N by M matrix of zeroes. Given N and M, write a function to count
the number of ways of starting at the top-left corner and getting to the
bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two
ways to get to the bottom-right:
    - Right, then down
    - Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def count_num_ways_to_bottom_right(N, M):
    if N < 1 or M < 1:
        return 0

    if N == 1 or M == 1:
        return 1

    return (
        count_num_ways_to_bottom_right(N - 1, M) +
        count_num_ways_to_bottom_right(N, M - 1)
    )

if __name__ == '__main__':
    import sys
    N, M = map(int, sys.argv[1:3])
    print('N: {}, M: {}'.format(N, M))
    print('number of ways to the bottom-right corner: {}'.format(
        count_num_ways_to_bottom_right(N, M)
    ))
