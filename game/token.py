from game.player import Player
from game.board import Board
import regex as re

class Token :
    def __init__(self, owner, position, name, steps_taken, is_home):
        self.owner = owner 
        self.position = position 
        # self.token_id = token_id 
        self.name = name 
        self.steps_taken = steps_taken 
        self.is_home = is_home 
        # self.state = state 

    def can_enter_board(self, dice_value) :
        #DONE
        if self.position == None and dice_value == 6 :
            return True 

    def can_move(self, dice_value) :
        #DONE
        can_move_token = self.steps_taken + dice_value
        if isinstance(self.position) and can_move_token <= 50 :
            return True 

    def apply_movement(self, dice_value) :

        #if the movement is valid and allowed
        if Token.can_move(dice_value) :
            self.steps_taken += dice_value 
            # if self.steps_taken + dice_value > 50 :
            #     return 
            if self.steps_taken ==  50 :
                self.is_at_home = True 

                #remove the occupied homes
                options = [f"{self.owner.name}_H1", f"{self.owner.name}_H2", f"{self.owner.name}_H3"]
                for token in self.owner.tokens :
                    if token.position in options :
                        options.remove(token.position)              
                #if at least one options exists , choose it        
                if len(options) > 0 :
                    opt = options.pop(0)
                    self.position = opt 
                    self.is_at_home = True
                    self.steps_taken = 50 
                else :
                    print("The token can't go to home!") 
                 

    def send_to_base(self) :
        #DONE
        Board.board[self.position] = self.position 
        self.position = None
        self.steps_taken = 0 
        self.state = "base"

    def is_at_home(self) :
        if self.position in ["H1","H2","H3"] :
            return True 