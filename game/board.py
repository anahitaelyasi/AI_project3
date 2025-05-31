from game.player import Player
from game.token import Token 
from game.game import Game

class Board :
    def __init__(self, tokens, position, home_slots):
        self.tokens = tokens 
        self.position = position 
        self.home_slots = home_slots 
        self.max_steps = 50 
        self.board = list(range(50)) 

    def show_current_board_position(self) :
        pass 
        
    def is_occupied(self, position) :
        if position.isnumeric() :
            return False
        else :
            return True  

    def place_token(token, position) :
        #if the token is in base and dice value is 6
        if Token.can_enter_board :
            #first check if the token start_position is occupied
            position = token.owner.start_position 
            Board.is_occupied(position)  
    
    def move_token(self, token, dice_value, position) :
        if Token.can_move(dice_value) :
            if Board.is_occupied(position) and self.board[position] != token.name : 
                Token.send_to_base() 
            Token.apply_movement(dice_value) 
            print(self.board) 

    #Clear token from board and send back to base 
    def remove_token(self, token) :
        Token.send_to_base() 
        print(self.board) 

    #Returns list of tokens at a position 
    def get_state_snapshop() :
        players = Player.players 
        dict = {
            "A" : [
                {"position": players[0].position, "steps": players., "is_home": 0},
                {},
                {}
            ], 
            "B" : [
                {},
                {},
                {}
            ], 
            "C" : [
                {},
                {},
                {}
            ] 
        } 
        return dict 