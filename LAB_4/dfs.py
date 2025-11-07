adjacency = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D", "E"],
        "D": ["B", "C", "E"],
        "E": ["C", "D", "F"],
        "F": ["E"]
        }

def dfs(adj, first_node):
    seen = set()
    path = []
    stack = [first_node]
    seen.add(first_node)

    while stack:
        current_node = stack.pop()
        # Marcar como visitado
        #   seen.add(current_node)
        # Agrego al path
        path.append(current_node)
        # Agrego a la pila sus hijos
        #   children = adj[current_node]

        for child in adj[current_node]:
            if child not in seen:
                stack.append(child)
                seen.add(child)

    return path

path = dfs(adjacency, "A")
print(path)
