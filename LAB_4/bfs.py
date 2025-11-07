from collections import deque

adjacency = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D", "E"],
        "D": ["B", "C", "E"],
        "E": ["C", "D", "F"],
        "F": ["E"]
        }

def bfs(adj, first_node):
    seen = set()
    queue = deque([])
    queue.append(first_node)
    seen.add(first_node)
    path = []

    while queue:
        current_node = queue.popleft()
        path.append(current_node)

        for child in adj[current_node]:
            if child not in seen:
                queue.append(child)
                seen.add(child)

    return path

path = bfs(adjacency, "A")
print(path)
