from cell import Cell
from solver import solve, is_solved
import pandas as pd

pd.option_context('display.max_rows', None, 'display.max_columns', None)


grid_str_arr  = [
    "800930002",
    "009000040",
    "702100960",
    "200000090",
    "060000070",
    "070006005",
    "027008406",
    "030000500",
    "500062008"
]

# create grid
sudoku_grid = [[Cell(x, y, grid_str_arr[y][x]) for x in range(9)] for y in range(9)]
sudoku_df = pd.DataFrame(sudoku_grid)
# print(sudoku_df)


x = solve(sudoku_grid)
i=1
while not is_solved(x):
    i = i+1
    x = solve(sudoku_grid)
    print(i,'\n')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
        print(pd.DataFrame(x))


if __name__ == '__main__':
    pass
