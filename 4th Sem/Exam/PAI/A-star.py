graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

open_list = ['A']
closed_list = []

g = {'A': 0}
parents = {'A': 'A'}

while open_list:

    n = None

    for v in open_list:
        if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
            n = v

    if n == 'G':
        path = []

        while parents[n] != n:
            path.append(n)
            n = parents[n]

        path.append('A')
        path.reverse()

        print("Path found:", path)
        break

    for (m, weight) in graph[n]:

        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parents[m] = n
            g[m] = g[n] + weight

        else:
            if g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n

                if m in closed_list:
                    closed_list.remove(m)
                    open_list.append(m)

    open_list.remove(n)
    closed_list.append(n)