def astar(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = None

        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print("Path does not exist!")
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            print("Total cost:", g[stop_node])
            return path

        for (m, cost) in get_neighbors(n):
            new_cost = g[n] + cost

            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = new_cost
            else:
                if new_cost < g.get(m, float('inf')):
                    g[m] = new_cost
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


def get_neighbors(v):
    return graph.get(v, [])


def heuristic(n):
    H_dist = {
        'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7,
        'G': 0
    }
    return H_dist[n]


graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': []
}

astar('A', 'G')
