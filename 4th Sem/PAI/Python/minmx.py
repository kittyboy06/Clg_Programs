import math

def minimax(depth, node_index, is_max, values, height):
    if depth == height:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, height),
            minimax(depth + 1, node_index * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, height),
            minimax(depth + 1, node_index * 2 + 1, True, values, height)
        )

n = int(input("Enter the number of leaf nodes: "))
print(f"Enter {n} leaf node values:")

values = list(map(int, input().split()))

height = math.log2(n)

if height.is_integer():
    height = int(height)
    optimal_value = minimax(0, 0, True, values, height)
    print("Optimal value:", optimal_value)
else:
    print("Invalid Input!")