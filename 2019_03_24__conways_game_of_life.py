'''
March 24, 2019

Conway's Game of Life takes place on an infinite two-dimensional board of
square cells. Each cell is either dead or alive, and at each tick, the
following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or
diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run
for. Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates, i.e.
from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a
dot (.).
'''

import sys

class ConwaysGameOfLife:
    LIVE = '*'
    DEAD = '.'

    def __init__(self):
        self.this_step = 0
        self.steps = 0
        self.live_cells = []

    def parse_inputs(self, inputs=sys.argv[1:]):
        self.steps = int(inputs[0])
        self.live_cells = [tuple(map(int, x.split(','))) for x in inputs[1:]]
        if not self.live_cells:
            self.live_cells = [(0, 0)]

    def print_inputs(self):
        print('steps: {}'.format(self.steps))
        print('live cells: {}'.format(self.live_cells))

    def main(self):
        self.print_board()
        while self.this_step <= self.steps:
            self.make_move()
            self.print_board()

    def make_move(self):
        '''
        Rules stipulated above:
        # Any live cell with less than two live neighbours dies.
        # Any live cell with two or three live neighbours remains living.
        # Any live cell with more than three live neighbours dies.
        # Any dead cell with exactly three live neighbours becomes a live cell.
        # A cell neighbours another cell if it is horizontally, vertically, or
          diagonally adjacent.
        '''
        self.live_cells = []
        for row, values in enumerate(self.board):
            for col, value in enumerate(values):
                is_live = value == self.LIVE
                self._update_live_cells(is_live, row, col)

        # Keeping these rules in mind, we need to check the row above our
        # current board, the row below our current board, the column left of
        # our current board, and the column right of our current board.
        # Those dead cells could have 3 live neighbors and therefore become
        # live cells.
        is_live = False
        for row in (-1, len(self.board)):
            for col in range(len(self.board[0])):
                self._update_live_cells(is_live, row, col)
        for row in range(len(self.board)):
            for col in (-1, len(self.board[0])):
                self._update_live_cells(is_live, row, col)

    def _update_live_cells(self, is_live, row, col):
        '''
        Again, we have the rules:
        # Any live cell with less than two live neighbours dies.
        # Any live cell with two or three live neighbours remains living.
        # Any live cell with more than three live neighbours dies.
        # Any dead cell with exactly three live neighbours becomes a live cell.
        # A cell neighbours another cell if it is horizontally, vertically, or
          diagonally adjacent.
        '''
        live_neighbors = 0
        for iii in (-1, 0, 1):
            for jjj in (-1, 0, 1):
                n_row = row + iii
                n_col = col + jjj
                if (
                    not (n_row == row and n_col == col) and
                    0 <= n_row < len(self.board) and
                    0 <= n_col < len(self.board[0]) and
                    self.board[n_row][n_col] == self.LIVE
                ):
                    live_neighbors += 1

        if (
            (is_live and live_neighbors in (2, 3)) or
            (not is_live and live_neighbors == 3)
        ):
            self.live_cells.append((row, col))

    def get_board_stats(self):
        max_row = max_col = -sys.maxint
        min_row = min_col = sys.maxint
        for row, col in self.live_cells:
            if row < min_row:
                min_row = row
            if row > max_row:
                max_row = row
            if col < min_col:
                min_col = col
            if col > max_col:
                max_col = col

        col_offset = -min_col
        row_offset = -min_row
        num_cols = max_col + col_offset + 1
        num_rows = max_row + row_offset + 1

        return (row_offset, col_offset, num_rows, num_cols)

    def print_board(self):
        row_offset, col_offset, num_rows, num_cols = self.get_board_stats()
        self.board = [
            [self.DEAD for _ in range(num_cols)]
            for _ in range(num_rows)
        ]

        for row, col in self.live_cells:
            self.board[row + row_offset][col + col_offset] = self.LIVE
        print('Step #{}:'.format(self.this_step))
        print('Live cells: {}'.format(self.live_cells))
        self.this_step += 1
        for row in self.board:
            print(' '.join(row))
        print('-----------------')
        print('-----------------')


if __name__ == '__main__':
    conways_game_of_life = ConwaysGameOfLife()
    conways_game_of_life.parse_inputs()
    conways_game_of_life.print_inputs()
    conways_game_of_life.main()