def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    edge = input("Enter edge (format: node1 node2): ").split()
    node1, node2 = edge

    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    graph[node1].append(node2)
    graph[node2].append(node1)

# Take input for the start node
start_node = input("Enter the start node: ")

if start_node not in graph:
    print("Invalid start node.")
else:
    print("DFS starting from node", start_node)
    dfs(graph, start_node)



# Enter the number of edges: 7
# Enter edge (format: node1 node2): A B
# Enter edge (format: node1 node2): A C
# Enter edge (format: node1 node2): B D
# Enter edge (format: node1 node2): B E
# Enter edge (format: node1 node2): C F
# Enter edge (format: node1 node2): C G
# Enter edge (format: node1 node2): E H
# Enter the start node: A