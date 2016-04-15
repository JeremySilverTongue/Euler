from collections import namedtuple

FILE_NAME = "p096_sudoku.txt"


def read_grids(file_name=FILE_NAME):
    with open(file_name) as grids:
        output_grids = []
        current_grid = []
        grids.readline()
        for line in grids:
            if "Grid" in line:
                output_grids.append(current_grid)
                current_grid = []
            else:
                current_grid.append(map(int, list(line[:-1])))
    return output_grids


class SudokuCell:

    def __init__(self, grid, y, x):
        self.y = y
        self.x = x
        self.row = [(y, m_x) for m_x in range(9)]
        self.column = [(m_y, x) for m_y in range(9)]
        block_start_y = y / 3 * 3
        block_start_x = x / 3 * 3
        self.block = [(block_start_y + m_y, block_start_x + m_x)
                      for m_y in range(3) for m_x in range(3)]
        self.excluded = set()
        self.value = grid[self.y][self.x]
        if self.value:
            self.excluded = set(range(1, 10)).difference([self.value])

    def __repr__(self):
        # if self.value:
            # return "Soved cell at {}, with value {}".format((self.y,self.x), self.value)
        # else:
        return "Sudoku cell at {}, with value {} with {} excluded".format((self.y, self.x), self.value, self.excluded)

    def __str__(self):
        return self.value

    def update_exclusions(self, grid):
        if not self.value:
            for cell_location in self.row + self.column + self.block:
                other_cell = grid[cell_location[0]][cell_location[1]]
                if other_cell.value:
                    self.excluded.update([other_cell.value])
            if len(self.excluded) == 8:
                self.value = list(
                    set(range(1, 10)).difference(self.excluded))[0]
                # print "Refined cel based on exclusions!"
                return True
        return False

    def group_necessity(self, grid, group):
        interseciton_of_exlcusions = set(range(1, 10))
        for cell_location in group:
            if cell_location != (self.y, self.x):
                other_cell = grid[cell_location[0]][cell_location[1]]
                # print other_cell.excluded
                interseciton_of_exlcusions.intersection_update(
                    other_cell.excluded)
                # print interseciton_of_exlcusions
        # print interseciton_of_exlcusions
        if len(interseciton_of_exlcusions) == 1:
            self.value = next(iter(interseciton_of_exlcusions))
            # print "refined cell based on necessity"
            return True
        return False

    def update_necessity(self, grid):
        if not self.value:
            if self.group_necessity(grid, self.row):
                return True
            if self.group_necessity(grid, self.column):
                return True
            if self.group_necessity(grid, self.block):
                return True
        return False


class Sudoku:

    def __init__(self, grid):
        # print grid
        self.cells = [[SudokuCell(grid, y, x)
                       for x in range(9)] for y in range(9)]
        # print self.cells

    def print_cells(self):
        nice_grid = self.raw_grid()
        for row in nice_grid:
            print row

    def refine(self):
        changed = False
        for row in self.cells:
            for cell in row:
                if cell.update_exclusions(self.cells):
                    changed = True
        for row in self.cells:
            for cell in row:
                if cell.update_necessity(self.cells):
                    changed = True
        return changed

    def raw_grid(self):
        nice_grid = []
        for row in self.cells:
            nice_row = []
            for cell in row:
                nice_row.append(cell.value)
            nice_grid.append(nice_row)
        return nice_grid

    def check_solved(self):
        raw_grid = self.raw_grid()
        for row in raw_grid:
            if sorted(row) != range(1, 10):
                return False
        for x in range(9):
            if sorted([raw_grid[y][x] for y in range(9)]) != range(1, 10):
                return False
        for block_y in range(3):
            for block_x in range(3):
                block_values = [raw_grid[3 * block_y + m_y][3 * block_x + m_x]
                                for m_y in range(3) for m_x in range(3)]
                # print sorted(block_values)
                if sorted(block_values) != range(1, 10):
                    return False
        return True

    def solve(self, iteration_limit=100):
        solved = False
        iterations = 0
        while iterations < iteration_limit:

            is_solved = self.check_solved()
            did_refine = self.refine()
            # print "is solved", is_solved
            # print "did_refine", did_refine
            # self.print_cells()

            # if not did_refine:
            # 	print "Stuck"
            # 	break

            iterations += 1
        if not self.check_solved():
            print "Didn't get it after {} iterations".format(iterations)
        else:
            print "Solved!"
            return True
        return False

grids = read_grids()

test_grid = [
    [4, 8, 3, 9, 2, 1, 6, 5, 7],
    [9, 6, 7, 3, 4, 5, 8, 2, 1],
    [2, 5, 1, 8, 7, 6, 4, 9, 3],
    [5, 4, 8, 1, 3, 2, 9, 7, 6],
    [7, 2, 9, 5, 6, 4, 1, 3, 8],
    [1, 3, 6, 7, 9, 8, 2, 4, 5],
    [3, 7, 2, 6, 8, 9, 5, 1, 4],
    [8, 1, 4, 2, 5, 3, 7, 6, 9],
    [6, 9, 5, 4, 1, 7, 3, 8, 2]]
doku = Sudoku(test_grid)
# print doku.check_solved()
doku.solve()
# doku.refine()

solved = 0
total_attempted = 0
for grid in grids:
    doku = Sudoku(grid)
    total_attempted += 1
    if doku.solve():
        solved += 1

print "Solved {} of {}".format(solved, total_attempted)
