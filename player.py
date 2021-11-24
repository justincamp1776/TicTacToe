import random

class Player():

    board =  [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
            ]


    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.score = 0
        
        
    def display_board(self):
        print(Player.board[0] , " | " + Player.board[1], " | " + Player.board[2])
        print(Player.board[3] , " | " + Player.board[4], " | " + Player.board[5])
        print(Player.board[6] , " | " + Player.board[7], " | " + Player.board[8])

    def handle_turn(self):
        selection = input(" Grid Instructions: Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9  Choose an EMPTY position from 1-9   ")
        if Player.board[int(selection) -1] != "-":
            print("That position is already taken. Please select and empty postion")
            self.handle_turn()
        else:
            Player.board[int(selection) -1] = "X"
            self.display_board()
        

    def handle_AI_turn(self):
        selection = random.randint(0,9)
        if Player.board[selection-1] != "-":
            self.handle_AI_turn()
        else:
             Player.board[selection-1] = "O"
             self.display_board()
        
