import copy

class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.size = 3  # Assuming it's a 3x3 puzzle
        self.initial_state = initial_state
        self.goal_state = goal_state

    def print_state(self, state):
        for row in state:
            print(row)
        print()

    def find_blank_position(self, state):
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return i, j

    def get_neighbors(self, state):
        neighbors = []
        blank_i, blank_j = self.find_blank_position(state)

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_i, new_j = blank_i + move[0], blank_j + move[1]
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                new_state = copy.deepcopy(state)
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                neighbors.append(new_state)

        return neighbors

def heuristic(state, goal_state):
    # Simple heuristic: number of misplaced tiles
    return sum([1 for i in range(len(state)) for j in range(len(state[i])) if state[i][j] != goal_state[i][j]])

def hill_climbing_puzzle_solver(puzzle):
    current_state = puzzle.initial_state
    goal_state = puzzle.goal_state

    step = 0
    while True:
        neighbors = puzzle.get_neighbors(current_state)
        neighbors_with_scores = [(neighbor, heuristic(neighbor, goal_state)) for neighbor in neighbors]
        neighbors_with_scores.sort(key=lambda x: x[1])

        best_neighbor, best_score = neighbors_with_scores[0]

        if heuristic(current_state, goal_state) <= best_score:
            break

        print(f"Step {step} - Heuristic: {best_score}")
        puzzle.print_state(current_state)
        print("Move to the next state\n")
        current_state = best_neighbor
        step += 1

    print("Solution found:")
    puzzle.print_state(current_state)

if __name__ == "__main__":
    # Take user input for the initial and goal states
    print("Enter the initial state (3x3 matrix, 0 represents the blank space):")
    initial_state = [[int(x) for x in input().split()] for _ in range(3)]

    print("Enter the goal state (3x3 matrix, 0 represents the blank space):")
    goal_state = [[int(x) for x in input().split()] for _ in range(3)]

    puzzle = EightPuzzle(initial_state, goal_state)

    print("Initial State:")
    puzzle.print_state(puzzle.initial_state)

    print("Goal State:")
    puzzle.print_state(puzzle.goal_state)

    print("Solving the puzzle using Hill Climbing:")
    hill_climbing_puzzle_solver(puzzle)


