from AI_project3.game.board import Board
from AI_project3.game.player import Player

#Controls the overall game flow and manages players, board, and turn-taking 

class Game :
    
    def __init__(self, players, board, current_player_index, dice_value, is_game_over, statistics):
        self.players = players 
        self.board = board 
        self.current_player_index = current_player_index 
        self.dice_value = dice_value 
        self.is_game_over= is_game_over 
        self.statistics = statistics

    def start_game() :
        pass

    def roll_dice() :
        pass 

    def play_turn() :
        pass 

    def switch_turn() :
        pass

    def check_winner() :
        pass

    def print_state() :
        pass 