'''
June 15, 2019

You are given a 2-d matrix where each cell represents number of coins in that
cell. Assuming we start at matrix[0][0], and can only move right or down, find
the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''

def get_max_coins(matrix):
    def _recurse(matrix, position, current_coins, max_coins):
        this_row, this_col = position
        current_coins += matrix[this_row][this_col]

        if (
            this_row == len(matrix) - 1 and
            this_col == len(matrix[this_row]) - 1
        ):
            if max_coins is None or current_coins > max_coins:
                max_coins = current_coins

        if this_row < len(matrix) - 1:
            max_coins = _recurse(
                matrix,
                (this_row + 1, this_col),
                current_coins,
                max_coins
            )

        if this_col < len(matrix[this_row]) - 1:
            max_coins = _recurse(
                matrix,
                (this_row, this_col + 1),
                current_coins,
                max_coins
            )

        return max_coins

    return _recurse(matrix, (0, 0), 0, None)

if __name__ == '__main__':
    test_cases = []

    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1],
    ]
    max_coins = 12
    test_cases.append((matrix, max_coins))

    matrix = [
        [1, 1],
        [1, 1],
    ]
    max_coins = 3
    test_cases.append((matrix, max_coins))

    matrix = [
        [1, -2],
        [-1, 2],
    ]
    max_coins = 2
    test_cases.append((matrix, max_coins))

    for matrix, max_coins in test_cases:
        result = get_max_coins(matrix)
        if result != max_coins:
            raise ValueError(
                'matrix: {}\nexpected_result: {}\nactual_result: {}'.format(
                    matrix, max_coins, result,
                )
            )
    print('All tests passed')
