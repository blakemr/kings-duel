import duel
import matplotlib.pyplot as plt

move_counts = []

for i in range(1000):
    board = duel.setup()
    move_counts.append(duel.random_game(board))

    if i % 100 == 0:
        print(i)

plt.hist(move_counts)
plt.show()