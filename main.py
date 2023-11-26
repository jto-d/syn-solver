from game import Game
import matplotlib.pyplot as plt
import numpy as np

game = Game(3)

iterations = 1000000

for i in range(iterations):
    game.play_round()

decision_list, rank_list, outcome_list = game.players[0].get_data()



ranks = sorted(set(rank_list), key=lambda rank : int(rank))
swap_wins = [0] * len(ranks)
swap_losses = [0] * len(ranks)
stay_wins = [0] * len(ranks)
stay_losses = [0] * len(ranks)

for decision, rank, outcome in zip(decision_list, rank_list, outcome_list):
    rank_index = ranks.index(rank)
    if decision == 'SWAP':
        if outcome:
            swap_wins[rank_index] += 1
        else:
            swap_losses[rank_index] += 1
    else:
        if outcome:
            stay_wins[rank_index] += 1
        else:
            stay_losses[rank_index] += 1

# Creating the grouped bar chart
bar_width = 0.35
index = np.arange(len(ranks))

fig, ax = plt.subplots()

bars1 = ax.bar(index - bar_width/2, swap_wins, bar_width, label='SWAP Losses', color='green')
bars2 = ax.bar(index + bar_width/2, stay_wins, bar_width, label='STAY Losses', color='blue')

# Add some text for labels, title, and axes ticks
ax.set_xlabel('Card Rank')
ax.set_ylabel('Losses')
ax.set_title('Losses by card rank and decision')
ax.set_xticks(index)
ax.set_xticklabels(ranks)
ax.legend()

plt.show()