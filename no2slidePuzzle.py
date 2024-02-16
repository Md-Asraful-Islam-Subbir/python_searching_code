import heapq


def h(state, goal_state):
    # Heuristic function - Manhattan distance
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:  # Skip the empty tile
                goal_position = divmod(value - 1, 3)
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return distance


def get_neighbors(state):
    # Generate possible moves (up, down, left, right)
    neighbors = []
    empty_position = find_empty_position(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for move in moves:
        new_state = make_move(state, empty_position, move)
        if new_state:
            neighbors.append(new_state)

    return neighbors


def find_empty_position(state):
    # Find the position of the empty tile (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)


def make_move(state, empty_position, move):
    # Move the empty tile in the specified direction
    i, j = empty_position
    x, y = move

    new_i, new_j = i + x, j + y

    if 0 <= new_i < 3 and 0 <= new_j < 3:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
        return new_state
    else:
        return None


def hill_climbing(initial_state, goal_state):
    current_state = initial_state
    while True:
        neighbors = get_neighbors(current_state)
        neighbors_with_scores = [(neighbor, h(neighbor, goal_state)) for neighbor in neighbors]

        if not neighbors:
            break  # No more moves possible

        best_neighbor, best_score = min(neighbors_with_scores, key=lambda x: x[1])

        if h(current_state, goal_state) <= best_score:
            break  # Reached a local minimum

        current_state = best_neighbor

    return current_state


# Example usage:
initial_state = [
    [3, 8, 5],
    [0, 7, 1],
    [2, 6, 4]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

result = hill_climbing(initial_state, goal_state)
print("Result:")
for row in result:
    print(row)
