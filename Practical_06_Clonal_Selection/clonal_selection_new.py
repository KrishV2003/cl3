import numpy as np

# Objective function
def fitness(x):
    return x**2

# Initial population min, max, size
population = np.random.uniform(-10, 10, 5)

generations = 10

# Store global best
global_best = None
global_fitness = float('inf')

for gen in range(generations):

    # Evaluate fitness
    fitness_values = [fitness(x) for x in population]

    # Select best antibody
    best_index = np.argmin(fitness_values)
    best = population[best_index]

    # Update global best
    if fitness(best) < global_fitness:
        global_best = best
        global_fitness = fitness(best)

    # Clone best antibody
    clones = np.array([best] * 5)

    # Mutation
    mutated = clones + np.random.normal(0, 0.5, 5)

    # New population
    population = mutated

    print(f"Generation {gen+1}")
    print("Best Solution:", best)
    print("Fitness:", fitness(best))
    print()

# Final optimized solution
print("Final Optimized Solution:", global_best)
print("Minimum Fitness Value:", global_fitness)