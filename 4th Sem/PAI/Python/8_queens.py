N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()


def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, row):
    if row >= N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, row + 1):
                return True

            board[row][col] = 0  # Backtrack

    return False


def eight_queens():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve(board, 0):
        print("Solution:\n")
        print_board(board)
    else:
        print("No solution found")


# Run the program
eight_queens()