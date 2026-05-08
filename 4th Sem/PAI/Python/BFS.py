graph = {}

e = int(input("Enter number of edges: "))
print("Enter each edge in format: node1 node2, e.g., A B")

for i in range(e):
    while True:
        edge = input(f"Edge {i+1}: ").strip()
        if not edge:
            print("Empty input! Please enter two nodes.")
            continue

        parts = edge.split()
        if len(parts) != 2:
            print("Invalid format! Please enter exactly two nodes separated by a space.")
            continue

        u, v = parts
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
        break

start = input("Enter starting node for BFS: ").strip()
if not start:
    print("No starting node entered.")
    raise SystemExit(1)

visited = set()
queue = [start]

print("BFS order:")
while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

print()