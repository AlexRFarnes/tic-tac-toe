from random import choice

BOARD_MAP = {str(col + 1 + 3 * row): (row, col) for row in range(3) for col in range(3)}


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + row[0] + "   |   " + row[1] + "   |   " + row[2] + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    print("\n\n")


def validate_input(move_input):
    if move_input.isdigit():
        if 1 <= int(move_input) <= 9:
            return True
    return False


def enter_move(board):
    while True:
        move_input = input("Enter your move (1-9): ")
        if validate_input(move_input):
            row, col = BOARD_MAP[move_input]
            if board[row][col] not in ["O", "X"]:  # check if the field is free
                board[row][col] = "O"
                break
            else:
                print("This field is already occupied. Try again.")
        else:
            print("Invalid input. Try again.")

    return board


def make_list_of_free_fields(board):
    free_fields = [
        (i, j) for i in range(3) for j in range(3) if board[i][j] not in ["O", "X"]
    ]
    return free_fields


def victory_for(board, sign):
    n = len(board)

    # check rows
    for i in range(n):
        if all(board[i][j] == sign for j in range(n)):
            return True

    # check columns
    for j in range(n):
        if all(board[i][j] == sign for i in range(n)):
            return True

    # check primary diagonal
    if all(board[i][i] == sign for i in range(n)):
        return True

    # check secondary diagonal
    # in a n x n matrix, indexes follow the pattern row + col = n - 1
    if all(board[i][n - 1 - i] == sign for i in range(n)):
        return True

    return False


def draw_move(board, move_count):
    if move_count == 1:  # first move
        board[1][1] = "X"
        return board

    free_fields = make_list_of_free_fields(board)
    row, col = choice(free_fields)  # choose a random free field
    board[row][col] = "X"
    return board


def build_board():
    return [[str(row + 1 + 3 * col) for row in range(3)] for col in range(3)]


def main():
    computer_won = False
    user_won = False
    move_count = 0
    board = build_board()
    print("Welcome to the Tic-Tac-Toe game!\n\n")

    while True:
        # Computer's move
        print("Computer's move:")
        move_count += 1
        board = draw_move(board, move_count)
        display_board(board)

        if victory_for(board, "X"):
            computer_won = True
            break

        if move_count == 9:
            break

        # User's move
        print("Your move:")
        move_count += 1
        board = enter_move(board)
        display_board(board)

        if victory_for(board, "O"):
            user_won = True
            break

    if computer_won:
        print("Computer won!")
    elif user_won:
        print("User won!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
