import numpy as np
import pandas as pd
from eight_queens.process import mutate
import matplotlib.pyplot as plt

from eight_queens.config import POPULATION_SIZE, NUM_QUEENS, N_ITERATIONS
from eight_queens.process import fitness_score, crossover
from eight_queens.visualization import print_board_from_perm


def pipeline():
    population = [np.random.permutation(NUM_QUEENS) for _ in range(POPULATION_SIZE)]
    fitness_scores = [fitness_score(perm) for perm in population]
    df = pd.DataFrame({"perm": population, "fitness": fitness_scores})
    hall_of_fame = df.nlargest(1, columns="fitness")
    i = 0
    fitnesses = {"max": [],
                 "min": [],
                 "mean": [],
                 "median": []}
    while i < 500:
        candidate_parents_indices = np.random.choice(POPULATION_SIZE, 5, replace=False)
        parents_to_crossover = df.iloc[candidate_parents_indices].nlargest(2, columns="fitness")
        child1, child2 = crossover(parents_to_crossover["perm"].iloc[0], parents_to_crossover["perm"].iloc[1])
        child1 = mutate(child1)
        child2 = mutate(child2)
        score1, score2 = fitness_score(child1), fitness_score(child2)
        if score1 >= df["fitness"].max():
            df.loc[df["fitness"][df["fitness"] < score1].idxmax(), :] = pd.Series({"perm": child1, "fitness": score1})
        if score2 >= df["fitness"].max():
            df.loc[df["fitness"][df["fitness"] < score2].idxmax(), :] = pd.Series({"perm": child2, "fitness": score2})
        i += 1
        hall_of_fame = df.nlargest(1, columns="fitness")
        if i % 10 == 0:
            print(f'num checks of hall of fame = {hall_of_fame["fitness"].iloc[0]}')
            print_board_from_perm(hall_of_fame["perm"].iloc[0])

        fitnesses["max"] += [df["fitness"].max()]
        fitnesses["min"] += [df["fitness"].min()]
        fitnesses["mean"] += [df["fitness"].mean()]
        fitnesses["median"] += [df["fitness"].median()]

    plt.figure()
    for measure in ["max", "min", "mean", "median"]:
        plt.plot(fitnesses[measure], ".")
    plt.show()


if __name__ == '__main__':
    pipeline()
