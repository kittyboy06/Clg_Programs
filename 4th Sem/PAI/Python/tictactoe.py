board = [" "] * 9

winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("---+---+---")
    print()


def check(player):
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_combinations
    )


def minimax(is_max):
    if check("o"):
        return 1
    if check("x"):
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "o"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "x"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best


def ai_move():
    best = -100
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "o"
            score = minimax(False)
            board[i] = " "
            if score > best:
                best = score
                move = i
    if move is not None:
        board[move] = "o"


while True:
    print_board()

    while True:
        try:
            m = int(input("Enter position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Enter a number 1-9.")
            continue

        if 0 <= m <= 8 and board[m] == " ":
            board[m] = "x"
            break
        else:
            print("Invalid move! Try again.")

    if check("x"):
        print_board()
        print("Player wins!")
        break

    if " " not in board:
        print_board()
        print("Draw")
        break

    ai_move()

    if check("o"):
        print_board()
        print("AI wins!")
        break

    if " " not in board:
        print_board()
        print("Draw")
        break