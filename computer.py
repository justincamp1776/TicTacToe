from player import Player
import random

class Computer(Player):

    def __init__(self, name):
        self.name = ""
        super().__init__(name)

    def handle_turn(self):
        selection = random.randint(0,9)
        if Player.board[selection-1] != "-":
            self.handle_turn()
        else:
             Player.board[selection-1] = "O"
             self.display_board()
    