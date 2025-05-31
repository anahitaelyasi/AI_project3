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

    def get_dice_value() :
        dice_value = random.choice(range(1,7)) 
        return dice_value
    
    #no matter who the player is, get the movable tokens
    def get_movable_tokens(self, dice_value) :
        movable_tokens = []
        for token in self.tokens :
            if Token.can_move(dice_value) or Token.can_enter_board(dice_value) :
                movable_tokens.append(token) 
        return movable_tokens 
    
    #depending on who the player is, move the tokens
    def choose_token_to_move(self, dice_value) :
        movable_tokens = Player.get_movable_tokens(dice_value) 
        if self.is_human :
            print("These are the movable tokens :\n")
            print(movable_tokens)
            player_choice = int(input("\nChoose one of the movable tokens (1,2,3) : ")) 
            return player_choice 
        else : 
            self.ai_agent.choose_best_move(dice_value) 
         
    #check if the player won 
    def has_won(self) :
        counter = 0
        for token in self.tokens :
            if token.position in self.home_filled :
                counter += 1
        if counter == 3 :
            return True

    #return tokens positions for board display or debugging 
    def get_token_positions(self) :
        tokens_positions = [ token.position for token in self.tokens]
        return tokens_positions 