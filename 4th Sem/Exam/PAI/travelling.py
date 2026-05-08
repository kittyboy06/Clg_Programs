from itertools import permutations

# Number of cities
n = int(input("Enter number of cities: "))

cities = []

print("Enter city names:")
for i in range(n):
    city = input()
    cities.append(city)

# Cost matrix
graph = {}

print("\nEnter cost matrix:")

for i in range(n):

    graph[cities[i]] = {}

    for j in range(n):

        if i != j:

            cost = int(input(f"Cost from {cities[i]} to {cities[j]}: "))
            graph[cities[i]][cities[j]] = cost


min_path = float('inf')
best_route = None

for path in permutations(cities):

    cost = 0

    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]

    cost += graph[path[-1]][path[0]]

    if cost < min_path:
        min_path = cost
        best_route = path

# Output
print("\nOptimal Route:")

for city in best_route:
    print(city, end=" -> ")

print(best_route[0])

print("Minimum Cost:", min_path)