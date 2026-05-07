import random
from deap import base, creator, tools, algorithms


# Evaluation Function
def evaluate(individual):

    # individual[0] -> neurons
    # individual[1] -> layers

    neurons = individual[0]
    layers = individual[1]

    # Simulated fitness function
    # Random value used for demonstration

    fitness = random.random()

    return (fitness,)


# Genetic Algorithm Parameters
POPULATION_SIZE = 10

GENERATIONS = 5


# Create Fitness Type
creator.create(
    "FitnessMin",
    base.Fitness,
    weights=(-1.0,)
)

# Create Individual Type
creator.create(
    "Individual",
    list,
    fitness=creator.FitnessMin
)

# Toolbox
toolbox = base.Toolbox()

# Attributes
toolbox.register(
    "attr_neurons",
    random.randint,
    1,
    100
)

toolbox.register(
    "attr_layers",
    random.randint,
    1,
    5
)

# Create Individual
toolbox.register(
    "individual",
    tools.initCycle,
    creator.Individual,
    (
        toolbox.attr_neurons,
        toolbox.attr_layers
    ),
    n=1
)

# Create Population
toolbox.register(
    "population",
    tools.initRepeat,
    list,
    toolbox.individual
)

# Genetic Operators
toolbox.register(
    "evaluate",
    evaluate
)

toolbox.register(
    "mate",
    tools.cxTwoPoint
)

toolbox.register(
    "mutate",
    tools.mutShuffleIndexes,
    indpb=0.2
)

toolbox.register(
    "select",
    tools.selTournament,
    tournsize=3
)

# Create Population
population = toolbox.population(
    n=POPULATION_SIZE
)

# Run Generations
for gen in range(GENERATIONS):

    # Create offspring
    offspring = algorithms.varAnd(
        population,
        toolbox,
        cxpb=0.5,
        mutpb=0.1
    )

    # Evaluate fitness
    fitnesses = list(
        map(toolbox.evaluate, offspring)
    )

    # Assign fitness
    for fit, ind in zip(fitnesses, offspring):

        ind.fitness.values = fit

    # Select next generation
    population = toolbox.select(
        offspring,
        k=len(population)
    )

# Best Individual
best_individual = tools.selBest(
    population,
    k=1
)[0]

# Display Result
print("Best Parameters :", best_individual)