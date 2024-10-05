## BFS without queue and node 

def bfs_recursive(graph, visited, layer):
    if not layer:
        return
    next_layer = []
    for node in layer:
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    next_layer.append(neighbor)
    bfs_recursive(graph, visited, next_layer)

graph = {
    1:[2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []}

visited = set()
bfs_recursive(graph, visited, [1])
