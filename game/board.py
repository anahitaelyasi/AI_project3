

class Board :
    def __init__(self, position, home_slots):
        self.position = position 
        self.home_slots = home_slots 
        self.max_steps = 50 
        
    def is_occupied(position) :
        pass 

    #Returns list of tokens at a position 
    def get_tokens_at(position) :
        pass 

    def move_token(token, dice_value) :
        pass 

    def check_collision(token) :
        pass 

    def can_enter_home(tokens, steps_remaining) :
        pass 

    def place_token(token, position) :
        pass 

    def remove_token(token, position) :
        pass 