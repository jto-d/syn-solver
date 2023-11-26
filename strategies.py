class Strategy(object):
    def __init__(self, players):
        self.players = players

class FourStrategy(Strategy):
    def __init__(self, players, position):
        Strategy.__init__(self, players)
        self.position = position

    def get_cutoff(self):
        if self.position == 0:
            return 5
        else:
            return 5