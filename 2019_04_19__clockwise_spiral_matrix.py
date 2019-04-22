'''
April 19, 2019

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:
    1
    2
    3
    4
    5
    10
    15
    20
    19
    18
    17
    16
    11
    6
    7
    8
    9
    14
    13
    12
'''

def yield_clockwise_spiral(matrix):
    if not (matrix and matrix[0]):
        return

    row_start = 0
    row_end = len(matrix) - 1
    col_start = 0
    col_end = len(matrix[0]) - 1

    this_row = 0
    this_col = 0

    row_delta = 0
    col_delta = 1

    for _ in range(len(matrix) * len(matrix[0])):
        yield matrix[this_row][this_col]

        if col_delta == 1 and this_col == col_end:
            row_delta = 1
            col_delta = 0
            row_start += 1
        elif col_delta == -1 and this_col == col_start:
            row_delta = -1
            col_delta = 0
            row_end -= 1
        elif row_delta == 1 and this_row == row_end:
            row_delta = 0
            col_delta = -1
            col_end -= 1
        elif row_delta == -1 and this_row == row_start:
            row_delta = 0
            col_delta = 1
            col_start += 1

        this_row += row_delta
        this_col += col_delta

if __name__ == '__main__':
    matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    for x in yield_clockwise_spiral(matrix):
        print(x)
    print('----------------------')

    matrix = [[1, 2, 3, 4, 5]]
    for x in yield_clockwise_spiral(matrix):
        print(x)
    print('----------------------')

    matrix = [[1], [2], [3], [4], [5]]
    for x in yield_clockwise_spiral(matrix):
        print(x)
