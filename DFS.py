def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node)  # Process the node
        visited.add(node)

        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [7],
        6: [],
        7: []}

start_node = 1
visited_nodes = set()
print("DFS Traversal:")
