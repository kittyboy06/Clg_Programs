from collections import deque

def water_jug():

    visited = set()

    queue = deque()

    queue.append((0, 0, []))

    while queue:

        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        path = path + [(x, y)]

        # Goal condition
        if x == 2 or y == 2:

            print("Steps to reach goal:\n")

            for step in path:
                print(step)

            print("\nGoal Reached!")
            return

        possible_states = [

            (4, y),   # Fill 4L jug
            (x, 3),   # Fill 3L jug

            (0, y),   # Empty 4L jug
            (x, 0),   # Empty 3L jug

            # Pour 4L -> 3L
            (x - min(x, 3 - y),
             y + min(x, 3 - y)),

            # Pour 3L -> 4L
            (x + min(y, 4 - x),
             y - min(y, 4 - x))
        ]

        for state in possible_states:

            if state not in visited:
                queue.append((state[0], state[1], path))

water_jug()