# Traveling Salesman Problem using Nearest Neighbor Algorithm

def tsp_nearest_neighbor(graph, start):
    n = len(graph)
    visited = [False] * n
    tour = []
    total_cost = 0

    current = start
    tour.append(current)
    visited[current] = True

    for i in range(n - 1):
        nearest = None
        min_dist = float('inf')

        for city in range(n):
            if not visited[city] and graph[current][city] < min_dist:
                min_dist = graph[current][city]
                nearest = city

        tour.append(nearest)
        visited[nearest] = True
        total_cost += min_dist
        current = nearest

    # Return to starting city
    total_cost += graph[current][start]
    tour.append(start)

    return tour, total_cost


# Input section
n = int(input("Enter number of cities: "))

print("Enter the distance matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting city (0 to n-1): "))

tour, cost = tsp_nearest_neighbor(graph, start)

print("Tour:", tour)
print("Minimum Cost:", cost)