from player import Player
from human import Human
from computer import Computer


class Game:

    def __init__(self):

        self.player1 = Player(input("Please Enter your name   "), "X")
        self.computer = Player("Computer", "O")
        self.keep_playing = True
        
        self.game_intro()

 
    def game_intro(self):
        # display initial board
        self.display_rules()
        self.player1.display_board()
        self.play_game()

    def display_rules(self):
        print("When selecting a position, the board reads Left to Right -- Top to Bottom. Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9 ")


    def play_game(self):
        
        while  self.keep_playing:
            print(f'{self.player1.name}, make your selection.')
            self.player1.handle_turn()
            print(f'{self.computer.name} chooses:')
            self.computer.handle_AI_turn()
            if self.keep_playing == True:
                self.end_game()
                break
        

    def check_winner(self):
        if Player.board[0] =="X" & Player.board[1] =="X" & Player.board[2] =="X": 
            self.keep_playing = False
            self.end_game(self.player1.name)
        if Player.board[0] =="O" & Player.board[1] =="O" & Player.board[2] =="O":
            self.keep_playing = False
            self.end_game(self.computer.name)
        if Player.board[3] =="X" & Player.board[4] =="X" & Player.board[5] =="X": 
            self.keep_playing = False
            self.end_game(self.player1.name)
        if Player.board[3] =="O" & Player.board[4] =="O" & Player.board[5] =="O":
            self.keep_playing = False
            self.end_game(self.computer.name)
        if Player.board[6] =="X" & Player.board[7] =="X" & Player.board[8] =="X": 
            self.keep_playing = False
            self.end_game(self.player1.name)
        if Player.board[6] =="O" & Player.board[7] =="O" & Player.board[8] =="O":
            self.keep_playing = False
            self.end_game(self.computer.name)
        if Player.board[0] =="X" & Player.board[4] =="X" & Player.board[8] =="X": 
            self.keep_playing = False
            self.end_game(self.player1.name)
        if Player.board[0] =="O" & Player.board[4] =="O" & Player.board[8] =="O":
            self.keep_playing = False
            self.end_game(self.computer.name)
        if Player.board[2] =="X" & Player.board[4] =="X" & Player.board[6] =="X": 
            self.keep_playing = False
            self.end_game(self.player1.name)
        if Player.board[2] =="O" & Player.board[4] =="O" & Player.board[6] =="X":
             self.keep_playing = False
             self.end_game(self.computer.name)
        
      

        

    def end_game(self):
        print("Thanks for playing. Rerun the program to play again.")