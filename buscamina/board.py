import random
from cell import Cell

class Board:
    def __init__(self, width, height, num_bombs):
        self.width = width
        self.height = height
        self.num_bombs = num_bombs
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]
        self.generate_bombs()

    def generate_bombs(self):
        bomb_count = 0
        while bomb_count < self.num_bombs:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            cell = self.grid[y][x]
            if not cell.is_bomb:
                cell.set_bomb()
                bomb_count += 1
                self.update_adjacent_cells(x, y)

    def update_adjacent_cells(self, x, y):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in offsets:
            dx, dy = offset
            nx, ny = x + dx, y + dy
            if self.is_valid_position(nx, ny):
                cell = self.grid[ny][nx]
                if not cell.is_bomb:
                    cell.set_adjacent_bombs(cell.adjacent_bombs + 1)

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def reveal_cell(self, x, y):
        cell = self.grid[y][x]
        cell.reveal()

        if cell.is_empty():
            offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for offset in offsets:
                dx, dy = offset
                nx, ny = x + dx, y + dy
                if self.is_valid_position(nx, ny):
                    neighbor_cell = self.grid[ny][nx]
                    if not neighbor_cell.is_revealed:
                        self.reveal_cell(nx, ny)

    def is_game_over(self):
        for row in self.grid:
            for cell in row:
                if cell.is_bomb and cell.is_revealed:
                    return True
        return False

    def is_game_won(self):
        for row in self.grid:
            for cell in row:
                if not cell.is_bomb and not cell.is_revealed:
                    return False
        return True

    def __str__(self):
        board_str = ""
        for row in self.grid:
            for cell in row:
                board_str += str(cell) + " "
            board_str += "\n"
        return board_str
