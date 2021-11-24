from player import Player

class Human(Player):

    def __init__(self):
        self.name = ""
        self.identifier = ""
        super().__init__()
