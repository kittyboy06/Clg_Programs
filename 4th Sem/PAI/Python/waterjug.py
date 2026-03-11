def water_jug(jug_1, jug_2, target):
    visited = set()

    def solve(j1, j2):
        if (j1, j2) in visited:
            return False

        print(f"Jug 1: {j1} gallons, Jug 2: {j2} gallons")

        if j1 == target:
            print("Target achieved!")
            return True

        visited.add((j1, j2))

        # Fill Jug 1
        if solve(jug_1, j2):
            return True

        # Fill Jug 2
        if solve(j1, jug_2):
            return True

        # Empty Jug 1
        if solve(0, j2):
            return True

        # Empty Jug 2
        if solve(j1, 0):
            return True

        # Pour Jug 1 -> Jug 2
        pour = min(j1, jug_2 - j2)
        if solve(j1 - pour, j2 + pour):
            return True

        # Pour Jug 2 -> Jug 1
        pour = min(j2, jug_1 - j1)
        if solve(j1 + pour, j2 - pour):
            return True

        return False

    if not solve(0, 0):
        print("No solution found")


# Correct input
water_jug(4, 3, 2)