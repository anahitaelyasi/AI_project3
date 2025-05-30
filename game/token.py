from AI_project3.game.player import Player

class Token :
    def __init__(self, player, position, state, token_id):
        self.player = player
        self.position = position 
        self.state = state 
        self.token_id = token_id 

    def can_enter_play(dice_value) :
        pass

    def can_move(dice_value, board) :
        pass

    def apply_movement(dice_value, board) :
        pass

    def send_to_base() :
        pass 

    def is_at_home(self) :
        pass  