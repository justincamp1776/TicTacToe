from player import Player

class Human(Player):

    def __init__(self, name):
        self.name = ""
        super().__init__(name)
