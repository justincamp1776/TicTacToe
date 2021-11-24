from player import Player



class Game:

    def __init__(self):

        self.player1 = Hua
        self.board =  [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
            ]

 

    def display_board(self):
        print(self.board[0] , " | " + self.board[1], " | " + self.board[2])
        print(self.board[3] , " | " + self.board[4], " | " + self.board[5])
        print(self.board[6] , " | " + self.board[7], " | " + self.board[8])


    def play_game(self):
        # display initial board
        display_board()

        # Prompts User for Input
        handle_turn()

        

    def handle_turn():
        placement = input(" Grid Instructions: Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9  Choose a position from 1-9   ")
        print(placement)