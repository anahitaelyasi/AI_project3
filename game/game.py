from AI_project3.game.board import Board
from AI_project3.game.player import Player

import random

#Controls the overall game flow and manages players, board, and turn-taking 

class Game :
    
    def __init__(self, players, board, current_player_index, dice_value, is_game_over, statistics):
        self.players = players  
        self.board = board 
        self.current_player_index = current_player_index 
        self.dice_value = dice_value 
        self.is_game_over= is_game_over 
        self.statistics = statistics

    def start_game(self) :

        while not self.is_game_over :
            self.dice_value = random.choice(range(1,7)) 
            input("Pick a token (0,1,2) : ")  
        while not Game.check_winner() :
            Game.switch_turn(self)  

    def switch_turn(self) :
        self.current_player_index  += 1 
        

    def check_winner() :
        pass

    def print_state() :
        pass 