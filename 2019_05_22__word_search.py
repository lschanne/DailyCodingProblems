'''
May 22, 2019

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
'''

def exists(board, word):
    if not word:
        return True

    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if _exists(board, word, row_idx, col_idx, []):
                return True

    return False

def _exists(board, word, row_idx, col_idx, used):
    if not word:
        return True

    if not (
        0 <= row_idx < len(board) and
        0 <= col_idx < len(board[row_idx]) and
        (row_idx, col_idx) not in used
    ):
        return False

    return (
        word[0] == board[row_idx][col_idx] and
        any(
            _exists(
                board,
                word[1:],
                next_row,
                next_col,
                used + [(row_idx, col_idx)]
            ) for (next_row, next_col) in (
                (row_idx, col_idx + 1),
                (row_idx, col_idx - 1),
                (row_idx + 1, col_idx),
                (row_idx - 1, col_idx),
            )
        )
    )

if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    print(exists(board, "ABCCED")) # true
    print(exists(board, "SEE")) # true
    print(exists(board, "ABCB")) # false
