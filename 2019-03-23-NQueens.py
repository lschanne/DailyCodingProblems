'''
March 23, 2019

You have an N by N board. Write a function that, given N, returns the number of
possible arrangements of the board where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column,
or diagonal.
'''

# I think that there was a solution to this in one of the tips and tricks
# emails that I archived. Luckily I don't really remember
def get_num_arrangements(N, placed_queens=[], this_row=0, count=0):
    if len(placed_queens) == N:
        return count + 1

    for this_col in range(N):
        if is_valid_board(this_col, placed_queens):
            count = get_num_arrangements(
                N,
                placed_queens + [this_col],
                this_row + 1,
                count
            )

    return count

def is_valid_board(this_col, placed_queens):
    this_row = len(placed_queens)
    for row, col in enumerate(placed_queens):
        if col == this_col or abs(this_row - row) == abs(this_col - col):
            return False

    return True

if __name__ == '__main__':
    import sys
    for N in map(int, sys.argv[1:]):
        print('N: {}'.format(N))
        print('possible arrangements: {}'.format(get_num_arrangements(N)))
        print('------------------------------------')
