from math import comb

import numpy as np


def fitness_score(perm):
    for idx, val in enumerate(perm):
        prime_diag_counters = {}
        secondary_diag_counters = {}
        if idx - val in prime_diag_counters:
            prime_diag_counters[idx - val] += 1
        else:
            prime_diag_counters[idx - val] = 1

        if idx + val in secondary_diag_counters:
            secondary_diag_counters[idx + val] += 1
        else:
            secondary_diag_counters[idx + val] = 1
    num_of_checks_on_primary_diagonals = sum(
        [comb(n_queens_same_prime_diag, 2) for n_queens_same_prime_diag in prime_diag_counters.values()])
    num_of_checks_on_secondary_diagonals = sum(
        [comb(n_queens_same_secondary_diago, 2) for n_queens_same_secondary_diago in secondary_diag_counters.values()])
    penalty = num_of_checks_on_primary_diagonals + num_of_checks_on_secondary_diagonals
    fitness = 1 / penalty
    return fitness


def crossover(perm1, perm2):
    pass


def mutate(perm):
    perm = perm.copy()
    if np.random.binomial(1, 0.8) == 1:
        i, j = np.random.choice(8, 2, replace=False)
        perm[i], perm[j] = j, i
    return perm


if __name__ == '__main__':
    s = 0
    for _ in range(10000):
        l = [i for i in range(8)]
        mutate_l = mutate(l)
        s += mutate_l != l
    print(s)
