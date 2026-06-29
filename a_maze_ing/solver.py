from collections import deque
# from .generator import MazeGenerator


class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.visited = False


class MazeSolver:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def solve_maze(self,
                   grid, entery: tuple, exite: tuple) -> list[tuple[int, int]]:

        parent = {}
        queue = deque()

        queue.append(entery)

        visited = set()
        visited.add(entery)

        while queue:

            row, col = queue.popleft()

            if exite == (row, col):
                break

            if row > 0 and not grid[row][col].has_wall(1):

                if (row - 1, col) not in visited:
                    queue.append((row - 1, col))
                    visited.add((row - 1, col))
                    parent[(row - 1, col)] = (row, col)

            if (self.cols > col + 1
                    and not grid[row][col].has_wall(2)):

                if (row, col + 1) not in visited:
                    queue.append((row, col + 1))
                    visited.add((row, col + 1))
                    parent[(row, col + 1)] = (row, col)

            if self.rows > row + 1 and not grid[row][col].has_wall(4):

                if (row + 1, col) not in visited:
                    queue.append((row + 1, col))
                    visited.add((row + 1, col))
                    parent[(row + 1, col)] = (row, col)

            if col > 0 and not grid[row][col].has_wall(8):

                if (row, col - 1) not in visited:
                    queue.append((row, col - 1))
                    visited.add((row, col - 1))
                    parent[(row, col - 1)] = (row, col)

        path = []
        if exite == entery or exite not in visited:
            return None

        current = exite

        while current != entery:

            path.append(current)
            current = parent[current]

        path.append(entery)
        path.reverse()
        return path


# grid = [
#     [0, 0, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0],
#     [1, 0, 0, 0, 1]
# ]

# start = (0, 0)
# target = (4, 3)

# path = solve_maze(grid, start, target)
# print(path)
