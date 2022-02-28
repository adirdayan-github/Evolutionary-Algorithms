import numpy as np


def fitness_score(perm):
    for idx, val in enumerate(perm):
        prime_diagonals = {}
        secondary_diagonals = {}
        if idx - val in prime_diagonals:
            prime_diagonals[idx - val] += 1
        else:
            prime_diagonals[idx - val] = 1

        if idx + val in secondary_diagonals:
            secondary_diagonals[idx + val] += 1
        else:
            secondary_diagonals[idx + val] = 1



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
