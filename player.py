

class Player():

    def __init__(self):
        self.score = 0
        self.board =  [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
            ]
        
    def display_board(self):
        print(self.board[0] , " | " + self.board[1], " | " + self.board[2])
        print(self.board[3] , " | " + self.board[4], " | " + self.board[5])
        print(self.board[6] , " | " + self.board[7], " | " + self.board[8])

    def handle_turn(self):
        selection = input(" Grid Instructions: Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9  Choose an EMPTY position from 1-9   ")
        self.board[int(selection) - 1] = "X"
        self.display_board()

    
       