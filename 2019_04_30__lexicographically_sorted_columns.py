'''
April 30, 2019

You are given an N by M 2D matrix of lowercase letters. Determine the minimum
number of columns that can be removed to ensure that each row is ordered from
top to bottom lexicographically. That is, the letter at each column is
lexicographically later as you go down each row. It does not matter whether
each row itself is ordered lexicographically.

For example, given the following table:
cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second
column to make it ordered:
ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:
abcdef
Your function should return 0, since the rows are already ordered (there's
only one row).

As another example, given the following table:
zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns
to order it.
'''

def count_unsorted_cols(matrix):
    N = len(matrix)
    if not N:
        return 0
    M = len(matrix[0])

    last_row = ['' for _ in range(M)]
    bad_col = [False for _ in range(M)]
    for row in matrix:
        for idx, val in enumerate(row):
            if not bad_col[idx]:
                if last_row[idx] <= val:
                    last_row[idx] = val
                else:
                    bad_col[idx] = True

        if all(bad_col):
            return M

    return sum(bad_col)

if __name__ == '__main__':
    import sys
    # not a true matrix, but it works for this function
    matrix = sys.argv[1:]
    for row in matrix:
        print(row)
    print('result: {}'.format(count_unsorted_cols(matrix)))
