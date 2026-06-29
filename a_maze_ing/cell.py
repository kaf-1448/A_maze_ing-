

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.state = 15

    def remove_wall(self, direction):

        if self.state & direction:
            self.state ^= direction

    def has_wall(self, direction):
        return self.state & direction != 0
