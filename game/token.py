from game.player import Player
from game.board import Board
from copy import deepcopy

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

    #check if the movement is valid and allowed
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
                # options = [f"{self.owner.name}_H1", f"{self.owner.name}_H2", f"{self.owner.name}_H3"]
                options = Player.home_filled
                options_copy = deepcopy(Player.home_filled) 
                for token in self.owner.tokens :
                    if token.position in options :
                        options_copy.remove(token.position)              
                #if at least one options exists , choose it        
                if len(options_copy) > 0 :
                    opt = options_copy.pop(0)
                    self.position = opt 
                    # options[options.index(opt)] = self.name 
                    self.is_at_home = True
                    self.steps_taken = 50 
                else :
                    print("The token can't go to home!") 
            else :
                self.position = (Player.start_position + self.steps_taken) % 50 
                Token.kickOut_opponent()
                Board.board[self.position] = self.name 

    def kickOut_opponent(self) :
        if Board.is_occupied(self.position) :
            competitor = Board.board[self.position]
            competitor_obj = [token for token in Player.players if token.name == competitor][0]
            print(f"The {competitor} is kicked out") 
            Token.send_to_base(competitor_obj)
            return True 

    def send_to_base(self, token) : 
        #DONE
        Board.board[self.position] = self.position 
        token.position = None 
        token.steps_taken = 0 
        # token.state = "base"

    def is_at_home(self) :
        if self.position in ["H1","H2","H3"] :
            return True 