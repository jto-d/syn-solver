from player import Player, ObservedPlayer
from cards import Card, Deck
import random
import numpy as np

# TODO: implement better "EV" practices (# of wins out of 100 rounds if this strategy)
#       implement a round as turn based for Q-learning efficiency

# object representing a single game of screw your neighbor
class Game:

    # update to number of players - 1
    button = 3

    # initialize a game object with parameter amount of players
    def __init__(self, players: int) -> None:
        self.players = []
        self.deck = None

        for i in range(players):
            player = Player("Player " + str(i+1), 4, i)
            self.add_player(player)

    # represent the game as "player": "chip count"
    def __str__(self) -> str:
        string_builder = []
        for player in self.players:
            string_builder.append(f'{str(player)}\n')
        return "".join(string_builder)
    
    # add a player to the game object
    def add_player(self, Player: Player) -> None:
        self.players.append(Player)

    # play the entire game and return the winner
    def play_game(self) -> Player:
        while len(self.players) > 1:
            self.play_round()
        return self.players[0]

    # play a round of the game
    def play_round(self, rank, action) -> bool:

        # update depending on what position you're solving for
        CURRENT_SOLVE = 1

        self.deck = Deck()
        self.deck.shuffle_deck()

        # TODO: turn this into a function probably
        # deal a card to each player
        for i in range(len(self.players)):
            if i != CURRENT_SOLVE:
                self.players[i].card = self.deck.pop()
                self.players[i].old_card = self.players[i].card
            else:
                self.players[i].card = Card(rank, "h")
                self.players[i].old_card = self.players[i].card


        # start with the player on the button and go in a circle
        # each player gets the ability to swap or stay
        size = len(self.players)
        seen = []

        for i in range(size):
            curr_index = (self.button + i + 1) % size
            curr_player = self.players[curr_index]



            # determine whether or not to swap their cards
            if curr_index == CURRENT_SOLVE and action == 1:

                next_player = self.players[(curr_index + 1) % size]
                status = curr_player.swap_card(next_player)
                # if not status:
                #     print("KING")
                # print("Swapped:" + str(curr_player.card))
            elif curr_index != CURRENT_SOLVE:
                SWAP = False
                rand = np.random.choice(100)
                card = int(curr_player.card.rank)
                if int(curr_player.old_card.rank) < card:
                    continue
                elif card < curr_player.strategy.get_cutoff():
                    SWAP = True
                if SWAP:
                    # if last player, swap with deck
                    if i == size - 1:
                        curr_player.card = self.deck.pop()
                    else:
                        next_player = self.players[(curr_index + 1) % size]
                        status = curr_player.swap_card(next_player)
                        
                        # if next_player.card is a King, break the swap
                        # if not status:
                            # print("King")
                            # print(curr_player.card.rank)
                    # print("Swapped:" + str(curr_player.card))
                
                
            seen.append(curr_player.card)
        
        # find the player with the lowest ranked card
        lowest = []
        for i, val in enumerate(seen):
            if len(lowest) == 0 or val.rank < seen[lowest[0]].rank:
                lowest = [i]
            elif val.rank == seen[lowest[0]].rank:
                lowest.append(i)
        
        # loser = self.players[loser_index]
        # print("Loser " + str(loser.card))
        # loser.chips -= 1

        # update observed player
        # observed_player = self.players[0]
        # observed_player.update_player(observed_player.action, observed_player.card.rank, loser_index == 0)
        # observed_player.action = "STAY"

        # check to see if player is still "alive"
        # if loser.chips <= 0:
        #     self.players.pop(loser_index)
        #     # print("Player out")
        #     if self.button <= loser_index:
        #         self.button -= 1


        seen.clear()


        # self.button += 1
        # self.button %= size





        return CURRENT_SOLVE in lowest

