from collections import defaultdict, deque

def bidirectional_search(graph, source, destination):
    forward_queue = deque([source])
    backward_queue = deque([destination])

    forward_visited = set([source])
    backward_visited = set([destination])

    while forward_queue and backward_queue:
        # Perform forward search
        current_forward = forward_queue.popleft()
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(neighbor)

        # Check if intersection point is reached
        if current_forward in backward_visited:
            return True

        # Perform backward search
        current_backward = backward_queue.popleft()
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(neighbor)

        # Check if intersection point is reached
        if current_backward in forward_visited:
            return True

    return False

# Example graph representing cities and connections
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E', 'H'],
    'H': ['G']
}

source_city = 'A'
destination_city = 'H'

if bidirectional_search(graph, source_city, destination_city):
    print(f"Path exists between {source_city} and {destination_city}.")
else:
    print(f"No path exists between {source_city} and {destination_city}.")
