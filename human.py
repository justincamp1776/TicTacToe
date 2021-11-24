from player import Player

class Human(Player):

    def __init__(self):
        self.name = "Player 1"
        self.identifier = "X"
        super().__init__()
