'''
April 8, 2019

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with
digits. The objective is to fill the grid with the constraint that every row,
column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
'''

from __future__ import print_function

# Well I guess "efficient" is a little subjective here, but I think that this
# bad boy is pretty good. At least in terms of time complexity
class SudokuSolver:
    ROWS = 9
    COLS = 9
    SIZE = ROWS * COLS
    SUBGRID = (3, 3)
    BLANK = '_'
    ELEMENTS = '123456789'

    def __init__(self, input_grid):
        if (
            len(grid) != self.ROWS or
            any(len(row) != self.COLS for row in grid)
        ):
            raise ValueError('Must be a {n_rows}x{n_cols} grid!'.format(
                n_rows=self.ROWS, n_cols=self.COLS
            ))

        self._row_elements = [
            {key: False for key in self.ELEMENTS} for _ in range(self.ROWS)
        ]
        self._col_elements = [
            {key: False for key in self.ELEMENTS} for _ in range(self.COLS)
        ]
        SUBROWS, SUBCOLS = self.SUBGRID
        n_grids = self.SIZE // (SUBROWS * SUBCOLS)
        self._box_elements = [
            {key: False for key in self.ELEMENTS} for _ in range(n_grids)
        ]

        for row_idx, row in enumerate(input_grid):
            for col_idx, value in enumerate(row):
                box_idx = col_idx // SUBCOLS + SUBROWS * (row_idx // SUBROWS)

                if value is self.BLANK:
                    pass
                elif value in self.ELEMENTS:
                    self._row_elements[row_idx][value] = True
                    self._col_elements[col_idx][value] = True
                    self._box_elements[box_idx][value] = True
                else:
                    raise ValueError(
                        'Each value in the grid must be either '
                        '{blank} or a digit 1-9, inclusive'.format(
                            blank=self.BLANK
                        )
                    )

        self._print_and_solve(input_grid)

    def _print_and_solve(self, unsolved_grid):
        self._print_grid(unsolved_grid, 'Unsolved input grid:')
        solved_grid = self._recursive_solver(unsolved_grid, 0)
        if solved_grid:
            self._print_grid(solved_grid, 'Solved grid:')
        else:
            self._print_cannot_be_solved()

    def _print_grid(self, grid, context=None):
        if context:
            print(context)

        SUBROWS, SUBCOLS = self.SUBGRID
        row_break = '-' * (self.COLS * 2 + SUBCOLS * 2 + 1)
        print(row_break)
        for row_idx, row in enumerate(grid):
            print('|', end=' ')
            for col_idx, value in enumerate(row):
                print(value, end=' ')
                if (col_idx % SUBROWS) == SUBROWS - 1:
                    print('|', end=' ')

            print('')
            if (row_idx % SUBCOLS) == SUBCOLS - 1:
                print(row_break)

    def _print_cannot_be_solved(self):
        print('The given input grid cannot be solved!')

    def _recursive_solver(self, grid, current_index=0):
        if current_index == self.SIZE:
            return grid

        SUBROWS, SUBCOLS = self.SUBGRID
        this_row = current_index // self.COLS
        this_col = current_index % self.COLS
        this_box = this_col // SUBCOLS + SUBROWS * (this_row // SUBROWS)
        if grid[this_row][this_col] is self.BLANK:
            for value in self.ELEMENTS:
                if not (
                    self._row_elements[this_row][value] or
                    self._col_elements[this_col][value] or
                    self._box_elements[this_box][value]
                ):
                    grid[this_row][this_col] = value
                    self._row_elements[this_row][value] = True
                    self._col_elements[this_col][value] = True
                    self._box_elements[this_box][value] = True
                    result = self._recursive_solver(grid, current_index + 1)
                    if result:
                        return result
                    else:
                        grid[this_row][this_col] = self.BLANK
                        self._row_elements[this_row][value] = False
                        self._col_elements[this_col][value] = False
                        self._box_elements[this_box][value] = False
        else:
            return self._recursive_solver(grid, current_index + 1)

if __name__ == '__main__':
    import sys
    grid = [list(row) for row in sys.argv[1:]]
    SudokuSolver(grid)
