class Cell:
    def __init__(self):
        self.is_bomb = False
        self.is_revealed = False
        self.adjacent_bombs = 0

    def set_bomb(self):
        self.is_bomb = True

    def is_empty(self):
        return not self.is_bomb

    def reveal(self):
        self.is_revealed = True

    def set_adjacent_bombs(self, count):
        self.adjacent_bombs = count

    def __str__(self):
        if self.is_revealed:
            if self.is_bomb:
                return "*"
            elif self.adjacent_bombs > 0:
                return str(self.adjacent_bombs)
            else:
                return " "
        else:
            return "-"
