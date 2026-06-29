from .cell import Cell
import random

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8


class MazeGenerator:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(row, col) for col in range(self.cols)]
                     for row in range(self.rows)]

    def get_neighbors(self, row, col) -> list[tuple[int, int, int]]:

        neighbors = []

        if row > 0 and not self.grid[row - 1][col].visited:
            neighbors.append((row - 1, col, NORTH))

        if self.rows > row + 1 and not self.grid[row + 1][col].visited:
            neighbors.append((row + 1, col, SOUTH))

        if col > 0 and not self.grid[row][col - 1].visited:
            neighbors.append((row, col - 1, WEST))

        if self.cols > col + 1 and not self.grid[row][col + 1].visited:
            neighbors.append((row, col + 1, EAST))

        return neighbors

    def generate_maze(self) -> list:
        try:
            self.grid[0][0].visited = True
            stack = [(0, 0)]

            while stack:

                row, col = stack[-1]

                available = self.get_neighbors(row, col)

                if available:
                    neighbors = random.choice(available)
                    n_row, n_col, direction = neighbors

                    if direction == NORTH:

                        self.grid[row][col].remove_wall(direction)
                        self.grid[n_row][n_col].remove_wall(SOUTH)

                    elif direction == EAST:

                        self.grid[row][col].remove_wall(direction)
                        self.grid[n_row][n_col].remove_wall(WEST)

                    elif direction == SOUTH:

                        self.grid[row][col].remove_wall(direction)
                        self.grid[n_row][n_col].remove_wall(NORTH)

                    elif direction == WEST:
                        self.grid[row][col].remove_wall(direction)
                        self.grid[n_row][n_col].remove_wall(EAST)

                    self.grid[n_row][n_col].visited = True
                    stack.append((n_row, n_col))

                else:
                    stack.pop()
        except IndexError as e:
            print(e)
