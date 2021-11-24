from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.name = "Computer"
        self.identifier = "O"
        self.used_selection = []
        super().__init__()

    def handle_turn(self, list):
       selection = random.randint(0,9)
       self.check_selection(list, selection)

    def check_selection(self, list,  selection):
        for index in self.used_selection:
            if index == selection:
                self.handle_turn()
                break
            else:
                list[selection] = "O"
                self.display_board()