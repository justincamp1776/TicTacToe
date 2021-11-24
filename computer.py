from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.name = "Computer"
        self.identifier = "O"
        super().__init__()

    def handle_turn(self, list):
        return random.choice(list)