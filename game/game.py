from game.board import Board
from game.player import Player
from game.token import Token

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

        #Loop while the game is not over
        while not self.is_game_over : 
            Game.switch_turn(self)  
            Board.show_current_board_position()  
            Game.check_winner() 

    def switch_turn(self) : 
        current_player = self.Players[self.current_player_index] 
        #Roll the dice 
        self.dice_value = Player.get_dice_value() 
        #Ask current player to pick a token
        #Move that token using the board 
        Board.move_token(current_player.current_token, self.dice_value) 

        if self.dice_value == 6 :
            Game.switch_turn() 
        else :
            self.current_player_index = (self.current_player_index + 1) % 3 

    def check_winner() :
        if Player.has_won() : 
            print(f"Player {Player.name} won")

    def print_state() :
        Board.get_state_snapshop() 