def water_jug(jug_1, jug_2, target):
    def solve(j1, j2):
        if (j1, j2) in visited:
            return False
        print(f"Jug 1: {j1} liters, Jug 2: {j2} liters")
        if j1 == target or j2 == target:
            return True
        visited.add((j1, j2))
        if solve(jug_1, j2):
            return True
        if solve(j1, jug_2):
            return True
        if solve(0, j2):
            return True
        if solve(j1, 0):
            return True
        pour = min(j1, jug_2 - j2)
        if solve(j1 - pour, j2 + pour):
            return True
        pour = min(j2, jug_1 - j1)
        if solve(j1 + pour, j2 - pour):
            return True
        return False
    visited = set()
    if not solve(0, 0):
        print("No solution found")
        
water_jug(11, 3, 2)
