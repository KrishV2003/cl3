import random
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

from deap import base, creator, tools, algorithms

from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPRegressor

from sklearn.metrics import mean_squared_error

from sklearn.preprocessing import StandardScaler


# ==============================
# LOAD COCONUT MILK DATASET
# ==============================

data = pd.read_csv("coconut_milk.csv")

# Remove extra spaces if present
data.columns = data.columns.str.strip()

# ==============================
# INPUT FEATURES
# ==============================

X = data.drop(
    "Moisture_Content_percent",
    axis=1
)

# TARGET OUTPUT
y = data["Moisture_Content_percent"]


# ==============================
# FEATURE SCALING
# ==============================

scaler = StandardScaler()

X = scaler.fit_transform(X)


# ==============================
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==============================
# FITNESS FUNCTION
# ==============================

def evaluate(individual):

    neurons = individual[0]

    layers = individual[1]

    # Create hidden layer structure
    hidden_layers = tuple(
        [neurons] * layers
    )

    try:

        # Neural Network Model
        model = MLPRegressor(
            hidden_layer_sizes=hidden_layers,
            max_iter=500,
            random_state=42
        )

        # Train Model
        model.fit(X_train, y_train)

        # Prediction
        predictions = model.predict(X_test)

        # Mean Squared Error
        mse = mean_squared_error(
            y_test,
            predictions
        )

        return (mse,)

    except:

        return (9999,)


# ==============================
# CREATE FITNESS CLASS
# ==============================

creator.create(
    "FitnessMin",
    base.Fitness,
    weights=(-1.0,)
)


# ==============================
# CREATE INDIVIDUAL
# ==============================

creator.create(
    "Individual",
    list,
    fitness=creator.FitnessMin
)


# ==============================
# TOOLBOX
# ==============================

toolbox = base.Toolbox()


# Number of neurons
toolbox.register(
    "attr_neurons",
    random.randint,
    1,
    100
)

# Number of hidden layers
toolbox.register(
    "attr_layers",
    random.randint,
    1,
    3
)


# ==============================
# CREATE INDIVIDUAL
# ==============================

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


# ==============================
# CREATE POPULATION
# ==============================

toolbox.register(
    "population",
    tools.initRepeat,
    list,
    toolbox.individual
)


# ==============================
# GENETIC OPERATORS
# ==============================

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


# ==============================
# CREATE POPULATION
# ==============================

population = toolbox.population(n=10)


# ==============================
# NUMBER OF GENERATIONS
# ==============================

GENERATIONS = 5


# ==============================
# RUN GENETIC ALGORITHM
# ==============================

for gen in range(GENERATIONS):

    print(f"\nGeneration {gen + 1}")

    # Crossover and Mutation
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

    # Selection
    population = toolbox.select(
        offspring,
        k=len(population)
    )


# ==============================
# BEST SOLUTION
# ==============================

best_individual = tools.selBest(
    population,
    k=1
)[0]


# ==============================
# FINAL OUTPUT
# ==============================

print("\n========================================")
print(" HYBRID GA-NN OPTIMIZATION RESULTS ")
print("========================================")

print(
    "\nBest Number of Neurons :",
    best_individual[0]
)

print(
    "Best Number of Hidden Layers :",
    best_individual[1]
)

print(
    "Best Fitness (MSE) :",
    best_individual.fitness.values[0]
)

print("\nOptimization Completed Successfully.")
