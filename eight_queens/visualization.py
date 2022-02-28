import numpy as np
from tqdm import tqdm

from eight_queens.config import NUM_QUEENS


def check_solution(perm):
    rows = set()
    cols = set()
    prime_diagonals = set()
    secondary_diagonals = set()
    for idx, val in enumerate(perm):
        if idx in rows:
            return False
        rows.add(idx)
        if val in cols:
            return False
        cols.add(val)
        if idx - val in prime_diagonals:
            return False
        prime_diagonals.add(idx - val)
        if idx + val in secondary_diagonals:
            return False
        secondary_diagonals.add(idx + val)
    return True


def print_board_from_perm(perm):
    board = np.zeros((NUM_QUEENS, NUM_QUEENS))
    for idx, val in enumerate(perm):
        board[idx, val] = 1
    print("\n", end="")
    for i in range(NUM_QUEENS):
        for j in range(NUM_QUEENS):
            print('*\t' if board[i, j] == 1 else '-\t', end="")
        print("\n", end="")


if __name__ == '__main__':
    for i in tqdm(range(10000)):
        perm = np.random.permutation(NUM_QUEENS)
        if check_solution(perm):
            print_board_from_perm(perm)
            print('\n')
