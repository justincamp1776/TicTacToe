from player import Player
import random

class Computer(Player):

    def __init__(self, name, identifier):
        super().__init__(name)

    def handle_turn(self, list):
        return random.choice(list)