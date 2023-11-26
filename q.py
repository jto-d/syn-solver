import numpy as np
from game import Game
import time

card_ranks = list(range(0, 13))

actions = ['swap', 'stay']

states = [(card, prev_action) for card in card_ranks for prev_action in [0, 1]]

Q_table = np.zeros((len(states), len(actions)))

# Q-learning parameters
alpha = 0.1 # learning rate
gamma = 0.9 # discount factor
epsilon = 0.1 # exploration rate


def choose_action(state, Q_table, epsilon):
    if np.random.uniform(0,1) < epsilon:
        return np.random.choice(len(actions))
    else:
        return np.argmax(Q_table[state, :])

def update_Q_table(state, action, reward, next_state, Q_table, alpha, gamma):

    predict = Q_table[state, action]
    target = reward + gamma * np.max(Q_table[next_state, :])
    Q_table[state, action] = Q_table[state, action] + alpha * (target - predict)

def get_reward(is_loser):
    return -10 if is_loser else 3

start_time = time.time()

game = Game(4)

num_episodes = 1000000



state_to_index = {state: index for index, state in enumerate(states)}

state = (np.random.choice(card_ranks), 0)
state_index = state_to_index[state]

for episode in range(num_episodes):

    action = choose_action(state, Q_table, epsilon)

    lost, prev_action = game.play_round(state, action)

    next_state = np.random.choice(len(card_ranks))

    reward = get_reward(lost)

    update_Q_table(state, action, reward, next_state, Q_table, alpha, gamma)
    
    state = next_state
    if episode % 100000 == 0:
        print(f"Iteration: {episode}", end='\r')

import seaborn as sns
import matplotlib.pyplot as plt

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time}")

action_labels = ['Stay', 'Swap']

# for testing
state_labels = [str(rank) for rank in card_ranks]

# for final ranges
# state_labels = [str(rank+2) for rank in card_ranks]

sns.heatmap(Q_table, annot=True, cmap='viridis', xticklabels=action_labels, yticklabels=state_labels)
plt.title('Heatmap of the Q-table for UTG 4 Person SYN')
plt.xlabel('Actions')
plt.ylabel('States')
plt.show()

# NOTE: NEED TO UPDATE STATE WHEN IT IS PLAYER'S TURN


