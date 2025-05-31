from game.token import Token
import random

#Represents a player (either human or AI)
class Player :
    def __init__(self, name, is_human, tokens, ai_agent, home_filled, start_position):
        self.name = name 
        self.tokens = tokens
        self.ai_agent = ai_agent 
        self.home_filled = home_filled
        self.is_human = is_human
        self.start_position = start_position
    
    def choose_move(self,dice_value, board) :
        if self.is_human : 
            pass 
        else :
            pass 
    
    def get_movable_tokens(self, dice_value) :
        movable_tokens = []
        for token in self.tokens :
            if Token.can_move(dice_value) or Token.can_enter_board(dice_value) :
                movable_tokens.append(token) 
        return movable_tokens 
    
    def choose_token_to_move(dice_value) :
        pass 

    def has_valid_move() :
        dice_number = random.choice(range(1,7)) 
        pass 

    def is_all_tokens_home() :
        pass 