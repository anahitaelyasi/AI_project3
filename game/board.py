from game.player import Player
from game.token import Token 
from game.game import Game

import regex as re 

class Board :
    def __init__(self, tokens, position, home_slots):
        self.tokens = tokens 
        self.position = position 
        self.home_slots = home_slots 
        self.max_steps = 50 
        self.board = list(range(50)) 

    def show_current_board_position(self) :
        print(self.board)
        
    def is_occupied(self, position) :
        if position.isnumeric() :
            return False
        else :
            return True  

    #place the token on the board
    def place_token(token, position) :
        #if the token is in base and dice value is 6
        if Token.can_enter_board :
            #first check if the token start_position is occupied
            position = token.owner.start_position 
            Board.is_occupied(position)  
    
    def move_token(self, token, dice_value) :
        if Token.can_move(dice_value) :
            pattern = token.owner + r"_[0-2]$"  
            #if the position is occupied and the occupied token is not your tokens
            if Board.is_occupied(token.position) and re.fullmatch(self.board[token.position], pattern)  :
                #khick the rival's token out of the board  
                Token.send_to_base(token) 
            Token.apply_movement(dice_value) 
            Board.show_current_board_position()  

    #Clear token from board and send back to base 
    def remove_token(self, token) :
        Token.send_to_base() 
        Board.show_current_board_position()

    #Returns list of tokens at a position 
    def get_state_snapshop() :
        players = Player.players 
        dict = {
            "A" : [
                {
                    "token_name" : players[0].tokens[0].name,
                    "position": players[0].tokens[0].position, 
                    "is_home": players[0].tokens[0].is_home, 
                    "steps_taken": players[0].tokens[0].steps_taken
                },
                {
                    "token_name" : players[0].tokens[1].name,
                    "position": players[0].tokens[1].position, 
                    "is_home": players[0].tokens[1].is_home, 
                    "steps_taken": players[0].tokens[1].steps_taken
                },
                {
                    "token_name" : players[0].tokens[2].name,
                    "position": players[0].tokens[2].position, 
                    "is_home": players[0].tokens[2].is_home, 
                    "steps_taken": players[0].tokens[2].steps_taken
                }
            ], 
            "B" : [
                {
                    "token_name" : players[1].tokens[0].name,
                    "position": players[1].tokens[0].position, 
                    "is_home": players[1].tokens[0].is_home, 
                    "steps_taken": players[1].tokens[0].steps_taken
                },
                {
                    "token_name" : players[1].tokens[1].name,
                    "position": players[1].tokens[1].position, 
                    "is_home": players[1].tokens[1].is_home, 
                    "steps_taken": players[1].tokens[1].steps_taken
                },
                {
                    "token_name" : players[1].tokens[2].name,
                    "position": players[1].tokens[2].position, 
                    "is_home": players[1].tokens[2].is_home, 
                    "steps_taken": players[1].tokens[2].steps_taken
                }
            ], 
            "C" : [
                {
                    "token_name" : players[2].tokens[0].name,
                    "position": players[2].tokens[0].position, 
                    "is_home": players[2].tokens[0].is_home, 
                    "steps_taken": players[2].tokens[0].steps_taken
                },
                {
                    "token_name" : players[2].tokens[1].name,
                    "position": players[2].tokens[1].position, 
                    "is_home": players[2].tokens[1].is_home, 
                    "steps_taken": players[2].tokens[1].steps_taken
                },
                {
                    "token_name" : players[2].tokens[2].name,
                    "position": players[2].tokens[2].position, 
                    "is_home": players[2].tokens[2].is_home, 
                    "steps_taken": players[2].tokens[2].steps_taken
                }
            ] 
        } 
        return dict 