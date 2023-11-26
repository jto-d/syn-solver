from strategies import FourStrategy

# Player class to represent a player's holdings and "spot" in the game
class Player:
    def __init__(self, name, players, position) -> None:
        self.name = name
        self.old_card = None
        self.card = None
        self.chips = 3
        self.strategy = FourStrategy(players, position)


    def __str__(self) -> str:
        return f'{self.name} : {self.card} : {self.chips}'

    def swap_card(self, player) -> bool:
        
        if player.card.rank == 11:
            return False
        player.card = self.card
        self.card = player.old_card

        return True

# Player object to keep track of players actions and results
class ObservedPlayer(Player):
    def __init__(self, name) -> None:
        Player.__init__(self, name)
        self.action = "STAY"
        self.actions = []
        self.hands = []
        self.losses = []
        

    def __str__(self) -> str:
        return f'{str(self.actions)}\n{str(self.hands)}\n{str(self.losses)}\n'

    def get_data(self) -> list:
        return [self.actions, self.hands, self.losses]

    def update_player(self, action, rank, loss):
        self.actions.append(action)
        self.hands.append(rank)
        self.losses.append(loss)
    
