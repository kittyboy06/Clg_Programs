n = int(input("Enter number of cities: "))
graph = [list(map(int, input().split())) for _ in range(n)]
Visited = [False] * n
tour = [0]
Visited[0] = True
cost = 0
current = 0
for _ in range(n-1):
    nearest = min((graph[current][j], j) for j in range(n) if not Visited[j])
    cost += nearest[0]
    current = nearest[1]
    tour.append(current)
    Visited[current] = True
cost += graph[current][0]
tour.append(0)
print("Tour:", tour)
print("Minimum cost:", cost)