from random import choice


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + row[0] + "   |   " + row[1] + "   |   " + row[2] + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def validate_input(row, col):
    if row.isdigit() and col.isdigit():
        row = int(row)
        col = int(col)
        if 0 < row < 4 and 0 < col < 4:
            return True
    return False


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        row = input("Enter the row number (1-3): ")
        col = input("Enter the column number (1-3): ")

        if validate_input(row, col):
            free_fields = make_list_of_free_fields(board)
            row = int(row) - 1  # convert to 0-based index
            col = int(col) - 1  # convert to 0-based index

            if (row, col) in free_fields:  # check if the field is free
                board[row][col] = "O"
                break
            else:
                print("This field is already occupied. Try again.")
        else:
            print("Invalid input. Try again.")

    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = [
        (i, j) for i in range(3) for j in range(3) if board[i][j] not in ["O", "X"]
    ]
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board, move_count):
    if move_count == 1:  # first move
        board[1][1] = "X"
        return board

    free_fields = make_list_of_free_fields(board)
    row, col = choice(free_fields)  # choose a random free field
    board[row][col] = "X"
    return board


def build_board():
    return [[str(i + 1 + 3 * j) for i in range(3)] for j in range(3)]


def main():
    move_count = 1
    board = build_board()
    print("Welcome to the Tic-Tac-Toe game!")
    print("Move count: ", move_count)
    display_board(board)

    # TODO: game loop

    while True:
        # Computer's move
        board = draw_move(board, move_count)
        display_board(board)
        move_count += 1
        # TODO: check if the computer has won
        if victory_for(board, "X"):
            pass

        # User's move
        board = enter_move(board)
        display_board(board)
        move_count += 1

        # TODO: check if the user has won
        if victory_for(board, "O"):
            pass


if __name__ == "__main__":
    main()
