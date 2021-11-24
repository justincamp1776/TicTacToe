from player import Player
from human import Human
from computer import Computer


class Game:

    def __init__(self):

        self.player1 = Human()
        self.computer = Computer()
        self.board =  [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
            ]
        self.play_game()

 
    def play_game(self):
        # display initial board
        self.display_board()
        self.display_rules()

    def display_rules(self):
        print("Please select a postion. Board reads left to right - Top to Bottom. Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9 ")

    def display_board(self):
        print(self.board[0] , " | " + self.board[1], " | " + self.board[2])
        print(self.board[3] , " | " + self.board[4], " | " + self.board[5])
        print(self.board[6] , " | " + self.board[7], " | " + self.board[8])


  

      

        

   