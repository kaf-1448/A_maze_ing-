from .generator import MazeGenerator
from .solver import MazeSolver


class DisplayMaze:

    def __init__(self, width, height, entery, exite):
        self.width = width
        self.height = height
        self.entery = entery
        self.exite = exite
        maze = MazeGenerator(width, height)
        maze.generate_maze()
        self.maze = maze.grid

    def draw_maze(self):
        mazesolver = MazeSolver(self.width, self.height)
        path = mazesolver.solve_maze(self.maze, self.entery, self.exite)

        actual_path = path if path is not None else []

        for row in range(self.width):
            top = ""
            inner = ""

            for col in range(self.height):

                cell = self.maze[row][col]

                # draw the north line
                if cell.has_wall(1):
                    top += "+---"
                else:
                    top += "+   "

                # draw path inside each cell
                if (row, col) == self.entery:
                    body = " E "
                elif (row, col) == self.exite and path:
                    body = " S "
                elif (row, col) in actual_path:
                    body = " * "
                else:
                    body = "   "

                # draw full cell content
                if cell.has_wall(8):
                    inner += "|" + body
                else:
                    inner += " " + body

            # full the the last cell for in row
            if self.maze[row][-1].has_wall(2):
                inner += "|"
            else:
                inner += " "

            top += "+"
            print(top)
            print(inner)

        bottom = ""
        for col in range(self.height):
            if self.maze[self.width - 1][col].has_wall(4):
                bottom += "+---"
            else:
                bottom += "+   "
        bottom += "+"
        print(bottom)
