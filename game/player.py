import random

#Represents a player (either human or AI)
class Player :
    def __init__(self,name,start_pos,tokens, ai, home_filled):
        self.name = name 
        self.tokens = tokens
        self.ai = ai
        self.home_filled = home_filled
        self.start_pos = start_pos 
    
    def choose_move(self,dice_value, board) :
        pass
    

    def has_valid_move() :
        dice_number = random.choice(range(1,7)) 
        pass 

    def is_all_tokens_home() :
        pass