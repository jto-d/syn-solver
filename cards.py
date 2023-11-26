import random

# Card object with a rank and suit
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (str(self.rank) + str(self.suit))

# Creates a Deck object containing the 52 cards
class Deck:
    suits = ['h', 'd', 's', 'c']
    ranks = list(range(0,13))

    def __init__(self) -> None:
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self) -> str:
        return str(self.deck)
    
    def shuffle_deck(self) -> None:
        random.shuffle(self.deck)

    def pop(self) -> Card:
        return self.deck.pop()





    

