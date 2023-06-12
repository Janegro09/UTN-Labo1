from board import Board

def play_game():
    width = 10
    height = 10
    num_bombs = 10
    board = Board(width, height, num_bombs)

    while not board.is_game_over() and not board.is_game_won():
        print(board)
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))

        if board.is_valid_position(x, y):
            board.reveal_cell(x, y)
        else:
            print("Invalid position. Try again.")

    if board.is_game_over():
        print("Game over! You hit a bomb!")
    elif board.is_game_won():
        print("Congratulations! You won the game!")

if __name__ == "__main__":
    play_game()
