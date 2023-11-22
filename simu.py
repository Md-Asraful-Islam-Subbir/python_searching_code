import math
import random

def objective_function(x):
    # Replace this with your own objective function
    return x**2 + 3*x + 5

def simulated_annealing(initial_solution, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    for _ in range(iterations):
        # Generate a neighboring solution
        neighbor_solution = current_solution + random.uniform(-1, 1)
        neighbor_energy = objective_function(neighbor_solution)

        # Calculate the energy difference
        delta_energy = neighbor_energy - current_energy

        # Accept the neighbor solution if it's better or with a certain probability
        if delta_energy < 0 or random.uniform(0, 1) < math.exp(-delta_energy / temperature):
            current_solution = neighbor_solution
            current_energy = neighbor_energy

        # Cool down the temperature
        temperature *= cooling_rate

    return current_solution, current_energy

# Set initial parameters
initial_solution = 0
initial_temperature = 1000.0
cooling_rate = 0.95
iterations = 1000

# Run simulated annealing
result_solution, result_energy = simulated_annealing(initial_solution, initial_temperature, cooling_rate, iterations)

print("Optimal Solution:", result_solution)
print("Optimal Energy:", result_energy)
