from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.name = "Computer"
        self.identifier = "O"
        self.used_selection = []
        super().__init__()

    def handle_turn(self):
        selection = random.randint(0,9)
        self.player.board[selection-1] = "O"
        self.display_board()
        return selection

    # def check_selection(self, list):
       
    #     for index in self.used_selection:
    #         if index == position:
    #             self.handle_turn()
    #             break
    #         else:
    #             list[selection] = "O"
    #             self.display_board()