'''
May 8, 2019

Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s that
are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''

'''
To be a bit more explicit, we'll call the diagonals part of the perimeter as
well. So this matrix
1 0
0 1
has 1 island.
'''
def island_count(matrix):
    island_matrix = [[None if x == 1 else 0 for x in row] for row in matrix]
    count = 0
    for iii, row in enumerate(island_matrix):
        for jjj, value in enumerate(row):
            if value == 0:
                continue

            # see if the island has already been numbered
            # check top-left, top, top-right, left
            for neighbor_row, neighbor_col in (
                (iii - 1, jjj - 1),
                (iii - 1, jjj),
                (iii - 1, jjj + 1),
                (iii, jjj - 1),
            ):
                if (
                    0 <= neighbor_row < len(island_matrix) and
                    0 <= neighbor_col < len(row) and
                    island_matrix[neighbor_row][neighbor_col]
                ):
                    island_matrix[iii][jjj] = (
                        island_matrix[neighbor_row][neighbor_col]
                    )
                    break

            # make a new island
            else:
                count += 1
                island_matrix[iii][jjj] = count

    return count

if __name__ == '__main__':
    import sys
    matrix = [[int(x) for x in arg.split(',')] for arg in sys.argv[1:]]
    print('input matrix:')
    for row in matrix:
        print(' '.join(map(str, row)))
    print('island count: {}'.format(island_count(matrix)))
