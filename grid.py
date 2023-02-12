from cell import Cell
import math
import time


class Grid:

    def __init__(self):
        self.grid = self.create_grid()

    def create_grid(self):
        grid = []

        for y in range(0, 9):
            grid.append([])

            for x in range(0, 9):
                grid[y].append(Cell(0, (x, y)))

        return self.populate_neighbours(grid)

    def populate_neighbours(self, grid):
        for y in range(0, 9):
            for x in range(0, 9):
                neighbours = []

                # Same Y, Diff X
                for xi in range(0, 9):
                    if xi != x:
                        neighbours.append(grid[y][xi])

                # Same X, Diff Y
                for yi in range(0, 9):
                    if yi != y:
                        neighbours.append(grid[yi][x])

                # Subgrid
                start_y = y - y % 3
                start_x = x - x % 3

                for k in range(start_y, start_y + 3):
                    for l in range(start_x, start_x + 3):
                        if k != y and l != x:
                            neighbours.append(grid[k][l])

                grid[y][x].neighbours = neighbours

        return grid

    def get_empty(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if self.grid[y][x].value == 0:
                    return (x, y)

        return None

    def is_valid(self, position, value):
        # VALIDATE SUDOKU BOARD
        cell = self.grid[position[1]][position[0]]

        for i in range(len(cell.neighbours)):
            if cell.neighbours[i].value == value:
                return False

        return True

    def solve_sudoku(self, run_per_ittr=None, fps=None):
        # SOLVE BY BACKTRACKING
        grid = self.grid
        spot = self.get_empty()

        if spot == None:
            return True

        for i in range(1, 10):
            if run_per_ittr: run_per_ittr(grid)
            if self.is_valid(spot, i):
                grid[spot[1]][spot[0]].value = i

                if run_per_ittr: 
                    run_per_ittr(grid)
                    time.sleep(1/fps)

                if self.solve_sudoku(run_per_ittr=run_per_ittr, fps=fps):
                    return True

                grid[spot[1]][spot[0]].value = 0

        return False

    def get_filled_count(self):
        filled = 0

        for row in self.grid:
            for cell in row:
                if cell.value != 0:
                    filled += 1
        
        return filled


    def render_grid(self):
        grid_string = ""

        for y in range(0, 9):
            if y == 0:
                grid_string += "\n      1 2 3   4 5 6   7 8 9\n"
                grid_string += "    —————————————————————————\n"

            for x in range(0, 9):
                if x == 0:
                    grid_string += f" {y+1} ▕  "

                grid_string += self.grid[y][x].as_string() + " "

                if (x + 1) % 3 == 0 and x < 8:
                    grid_string += "| "

                if x == 8:
                    grid_string += " ▏"

            if (y + 1) % 3 == 0 and y < 8:
                grid_string += "\n   ▕—————————————————————————▏\n"

            else:
                grid_string += "\n"

            if y == 8:
                grid_string += "    —————————————————————————\n"

        print(grid_string)
