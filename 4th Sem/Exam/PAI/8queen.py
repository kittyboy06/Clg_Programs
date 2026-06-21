import random

def solve(q=[], col=0):
    if col == 4:
        print_board(q)
        return True
    rows = list(range(4))
    random.shuffle(rows)  # Shuffle row order for randomness
    for row in rows:
        if all(row != r and abs(row - r) != col - c for c, r in enumerate(q)):
            if solve(q + [row], col + 1):
                return True
    return False

def print_board(q):
    for row in q:
        print(". " * row + "Q " + ". " * (3 - row))
    print()

solve()