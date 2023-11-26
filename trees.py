from itertools import combinations, permutations, product
from collection import Counter
from copy import deepcopy
from functools import partial

# NOTE: This file is not actually used for anything,
#       it was the beginning of a CFR algorithm

SWAP = 0
STAY = 1

class GameRules(object):
    def __init__(self, players, deck, stack):
        assert(players >= 3 and players <= 9)
        assert(stack > 0)
        assert(deck != None)
        assert(len(deck) == 52)

        self.players = players
        self.deck = deck
        self.stack = stack

class RoundInfo(object):
    def __init__(self, cards):
        self.cards = cards

class Node(object):
    def __init__(self, parent, cards, history):
        if parent:
            self.parent = parent
            self.parent.add_child(self)
        self.cards = deepcopy(cards)
        self.history = deepcopy(history)
        

    def add_child(self, child):
        if not self.children:
            self.children = [child]
        else:
            self.children.append(child)

# class TerminalNode(Node):
#     def __init__(self, parent,)