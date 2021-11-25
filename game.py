from player import Player
from human import Human
from computer import Computer



class Game:

    def __init__(self):

        self.player1 = Human(input("Please Enter your name   "))
        self.computer = Computer("Computer")
        self.keep_playing = True
        self.game_intro()

 
    def game_intro(self):
        # displays rules and initial board
        self.display_rules()
        self.player1.display_board()
        self.play_game()

    def display_rules(self):
        print("When selecting a position, the board reads Left to Right -- Top to Bottom. Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9 ")


    def play_game(self):
        # This function loops through the handle_turn fucntions and checks for a winner after each iteration. 
        while  self.keep_playing:
            print(f'{self.player1.name}, make your selection.')
            self.player1.handle_turn()
            self.check_winner()
            print(f'{self.computer.name} chooses:')
            self.computer.handle_turn()
            self.check_winner()
          
    def check_winner(self):
        # This function calls the 7 functions below and checks for every pattern that could result in a win.
        self.check_first_row()
        self.check_second_row()
        self.check_third_row()
        self.check_first_col()
        self.check_second_col()
        self.check_third_col()
        self.check_diagnol() 

        
    def check_first_row(self):
        if Player.board[0] =="X" and Player.board[1] =="X" and Player.board[2] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[0] =="O" and Player.board[1] =="O" and Player.board[2] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)

    def check_second_row(self):
        if Player.board[3] =="X" and Player.board[4] =="X" and Player.board[5] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[3] =="O" and Player.board[4] =="O" and Player.board[5] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)

    def check_third_row(self):
        if Player.board[6] =="X" and Player.board[7] =="X" and Player.board[8] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[6] =="O" and Player.board[7] =="O" and Player.board[8] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)

    def check_first_col(self):
        if Player.board[0] =="X" and Player.board[3] =="X" and Player.board[6] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[0] =="O" and Player.board[3] =="O" and Player.board[6] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)

    def check_second_col(self):
        if Player.board[1] =="X" and Player.board[4] =="X" and Player.board[7] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[1] =="O" and Player.board[4] =="O" and Player.board[7] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)


    def check_third_col(self):
        if Player.board[2] =="X" and Player.board[5] =="X" and Player.board[8] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[2] =="O" and Player.board[5] =="O" and Player.board[8] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)

    def check_diagnol(self):
        if Player.board[0] =="X" and Player.board[4] =="X" and Player.board[8] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[0] =="O" and Player.board[4] =="O" and Player.board[8] =="O":
            self.keep_playing = False
            self.play_again(self.computer.name)
        elif Player.board[2] =="X" and Player.board[4] =="X" and Player.board[6] =="X": 
            self.keep_playing = False
            self.play_again(self.player1.name)
        elif Player.board[2] =="O" and Player.board[4] =="O" and Player.board[6] =="X":
             self.keep_playing = False
             self.play_again(self.computer.name)
     
    def play_again(self, player_name):
        valid = False
        print(f'{player_name} wins')
        user_input = input("Would you like A Rematch? Enter Yes or No    ")
        if user_input.lower() == "Yes".lower():
            self.keep_playing = True
            valid == True
            Player.board = [
                            "-", "-", "-",
                            "-", "-", "-",
                            "-", "-", "-"
                            ]
            self.game_intro()
       
        elif user_input.lower() == "No".lower():
            print("Thanks for playing!")
            self.keep_playing = False
        

        

    def end_game(self):
        
        self.play_again()
        
