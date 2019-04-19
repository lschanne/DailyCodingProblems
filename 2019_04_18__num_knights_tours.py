'''
April 18, 2019

A knight's tour is a sequence of moves by a knight on a chessboard such that
all squares are visited once.

Given N, write a function to return the number of knight's tours on an
N by N chessboard.
'''

'''
So the problem I have with this problem statement is that it's really
ambiguous. It seems reasonable to assume that they mean unique knight's tours.
However, even "unique" is ambiguous. What if it's the same sequence of moves,
but just a different starting spot? Is it unique starting spots? What if you
start in the same spot but are able to tour the board via different moves?

So these are the questions to answer. It could be the case that once I
understand the properties of a knight's tour, these questions will answer
themselves. (I hope.)

It seems like we could just brute force a recursive solution. It's a bit of a
shame though because it lacks any insights or intuition into the properties
of the knight's tour. However, trying to figure those out feels too hard and
time consuming for a daily problem. So then the alternative is to look them up,
which is basically cheating. That being said, I probably will look them up
after I solve this problem. Also, the recursive solution, will use the most
generous interpretation of unique. If the sequence of moves is not exactly the
same and in the exact same order, it is unique.
'''
def get_number_of_knights_tours(N):
    move_matrix = [[False for _ in range(N)] for _ in range(N)]
    possible_moves = [(iii, jjj) for iii in range(N) for jjj in range(N)]
    return _recurser(possible_moves, move_matrix, num_moves=0, N=N)

# As you would expect, this recursive approach becomes slow very quickly
# For N=5 and N=8, it really took a long time
# Just by checking each possible starting position, we are automatically at
# least at O(N^2). Unfortunately, the time complexity is even worse than that
# once you introduce the actual recursive function.
def _recurser(possible_moves, move_matrix, num_moves, N):
    count = 0
    num_moves += 1
    if num_moves == N * N:
        return len(possible_moves)

    for this_row, this_col in possible_moves:
        these_moves = []
        for row_diff, col_diff in (
            (1, 2), (1, -2), (-1, -2), (-1, 2),
            (2, 1), (2, -1), (-2, -1), (-2, 1),
        ):
            next_row = this_row + row_diff
            next_col = this_col + col_diff
            if (
                0 <= next_row < N and
                0 <= next_col < N and
                not move_matrix[next_row][next_col]
            ):
                these_moves.append((next_row, next_col))

        if these_moves:
            # need a deep copy of that bad boy
            this_matrix = [[x for x in row] for row in move_matrix]
            this_matrix[this_row][this_col] = True
            count += _recurser(these_moves, this_matrix, num_moves, N)

    return count

if __name__ == '__main__':
    import sys
    for N in map(int, sys.argv[1:]):
        print(
            "For N={}, there are {} knight's tours.".format(
                N, get_number_of_knights_tours(N)
            )
        )

'''
RESULTS:
For N=0, there are 0 knight's tours.
For N=1, there are 1 knight's tours.
For N=2, there are 0 knight's tours.
For N=3, there are 0 knight's tours.
For N=4, there are 0 knight's tours.
For N=5, there are 1728 knight's tours.

# 1-5 are right according to https://en.wikipedia.org/wiki/Knight%27s_tour
# 8 should be 19,591,828,170,979,904
'''