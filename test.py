# test.py - Run analysis on various chess bots

import duel
import matplotlib.pyplot as plt


def random_game_length_histogram(trials):
    """Plots a histogram showing the length of random bot games

    args:
        trials: number of trials to run
    """
    move_counts = []

    for i in range(trials):
        board = duel.setup()
        move_counts.append(duel.random_game(board))

        # Output tials progress
        if i % 100 == 0:
            print(i)

    plt.hist(move_counts)
    plt.show()
