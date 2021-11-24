

class Player():

    def __init__(self):
        self.score = 0
        


    def handle_turn(self):
        placement = input(" Grid Instructions: Top Row: 1 - 3 -- Second Row: 4 - 6 -- Third Row: 7-9  Choose a position from 1-9   ")
        print(placement)
