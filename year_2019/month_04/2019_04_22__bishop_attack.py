'''
April 22, 2019

On our special chessboard, two bishops attack each other if they share the same
diagonal. This includes bishops that have another bishop located between them,
i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M
chessboard. Write a function to count the number of pairs of bishops that
attack each other. The ordering of the pair doesn't matter: (1, 2) is
considered the same as (2, 1).

For example, given M = 5 and the list of bishops:
(0, 0)
(1, 2)
(2, 2)
(4, 0)

The board would look like this:
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as
bishops 3 and 4.
'''

def get_attacking_bishops(M, bishop_list):
    left_to_right_diagonals = [0 for _ in range(M * 2 - 1)]
    right_to_left_diagonals = [0 for _ in range(M * 2 - 1)]
    count = 0
    for row, col in bishop_list:
        left_to_right_idx = M - 1 - row + col
        right_to_left_idx = 2 * (M - 1) - row - col
        left_to_right_diagonals[left_to_right_idx] += 1
        right_to_left_diagonals[right_to_left_idx] += 1

    for this_count in left_to_right_diagonals:
        if this_count:
            count += this_count - 1

    for this_count in right_to_left_diagonals:
        if this_count:
            count += this_count - 1

    return count

if __name__ == '__main__':
    M = 5
    bishop_list = [(0, 0), (1, 2), (2, 2), (4, 0)]
    print('M: {}'.format(M))
    print('bishops: {}'.format(bishop_list))
    print('attacking bishops: {}'.format(
        get_attacking_bishops(M, bishop_list))
    )
