from math import comb

import numpy as np


def fitness_score(perm):
    prime_diag_counters = {}
    secondary_diag_counters = {}
    for idx, val in enumerate(perm):
        if idx - val in prime_diag_counters:
            prime_diag_counters[idx - val] += 1
        else:
            prime_diag_counters[idx - val] = 1

        if idx + val in secondary_diag_counters:
            secondary_diag_counters[idx + val] += 1
        else:
            secondary_diag_counters[idx + val] = 1
    num_of_checks_on_primary_diagonals = sum([n * (n - 1) for n in prime_diag_counters.values()])
    num_of_checks_on_secondary_diagonals = sum([n * (n - 1) for n in secondary_diag_counters.values()])
    penalty = num_of_checks_on_primary_diagonals + num_of_checks_on_secondary_diagonals
    fitness = 1 / penalty
    return fitness


def crossover(perm1, perm2):
    point = np.random.randint(1, perm1.shape[0] - 1)
    child1, child2 = perm1[:point], perm2[:point]
    child1_to_fill = perm2[point:][~np.isin(perm2[point:], child1)]
    child2_to_fill = perm1[point:][~np.isin(perm1[point:], child2)]
    child1 = np.concatenate((child1, child1_to_fill))
    child2 = np.concatenate((child2, child2_to_fill))
    child1 = np.concatenate((child1, perm2[:point][~np.isin(perm2[:point], child1)]))
    child2 = np.concatenate((child2, perm1[:point][~np.isin(perm1[:point], child2)]))
    return child1, child2, point


def mutate(perm):
    perm = perm.copy()
    if np.random.binomial(1, 0.8) == 1:
        i, j = np.random.choice(8, 2, replace=False)
        perm[i], perm[j] = j, i
    return perm


if __name__ == '__main__':
    # s = 0
    # for _ in range(10000):
    #     l = [i for i in range(8)]
    #     mutate_l = mutate(l)
    #     s += mutate_l != l
    # print(s)

    perm1, perm2 = [1, 3, 5, 4, 2, 6, 7, 8], [4, 5, 2, 3, 6, 8, 7, 1]
    perm1, perm2 = np.array(perm1), np.array(perm2)
    child1, child2, point = crossover(perm1, perm2)
