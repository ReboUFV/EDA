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
       level = []
       for _ in range(len(queue)):
           current_node = queue.popleft()
           level.append(current_node)

           for child in adj[current_node]:
               if child not in seen:
                   seen.add(child)
                   queue.append(child)
       path.append(level)
    return path

path = bfs(adjacency, "A")
print(path)

