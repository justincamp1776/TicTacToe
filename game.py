from player import Player
from human import Human
from computer import Computer


class Game:

    def __init__(self):

        self.player1 = Human()
        self.computer = Computer()
        
        self.game_intro()

 
    def game_intro(self):
        # display initial board
        self.display_rules()
        self.player1.display_board()
        self.play_game()

    def display_rules(self):
        print("When selecting a position, the board reads Left to Right -- Top to Bottom. Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9 ")


    def play_game(self):
         print(f'{self.player1.name}, make your selection.')
         self.player1.handle_turn()
         print(f'{self.computer.name} chooses:')
         self.computer.handle_turn(self.computer.board)

  

      

        

   