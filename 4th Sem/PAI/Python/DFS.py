graph = {}

e = int(input("Enter number of edges: "))
print("Enter each edge in format: node1 node2 (e.g., A B)")

for i in range(e):
    edge = input(f"Edge {i+1}: ").strip()
    if not edge:
        print("Empty input! Please enter two nodes.")
        continue
    parts = edge.split()
    if len(parts) != 2:
        print("Invalid format! Please enter exactly two nodes.")
        continue
    u, v = parts
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, [])  # Ensures the node exists in the graph

start = input("Enter starting node for DFS: ").strip()
visited = set()
stack = [start]

print("DFS Order:")
while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        stack.extend(reversed(graph[node]))