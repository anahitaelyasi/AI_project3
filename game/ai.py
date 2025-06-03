from game.player import Player
from game.board import Board
from game.game import Game
from game.token import Token

from copy import deepcopy

class AI : 
    def __init__(self, depth_limit, nodes_explored):
        self.depth_limit = depth_limit 
        self.nodes_explored = nodes_explored 

    def choose_best_move(game_state, dice_value) : 

         
        current_player = game_state.players[game_state.current_player_index] 

        for tokeni in current_player.get_movable_tokens(dice_value) :
            copied_game = deepcopy(game_state) 
            copied_player = copied_game.players[copied_game.current_player_index] 
            copied_token = [token for token in copied_player.tokens if token.name == tokeni.name][0] 
            copied_board = copied_game.board 
        #deep copy of attributes

        movable_tokens = current_player.get_movable_tokens(dice_value)
        tokens_status = copied_board.get_state_snapshop()
        current_board_info = copied_board.show_current_board_position()
        occupied_positions = [] 
        for pos in copied_board.board : 
            if copied_board.is_occupied(pos) :
                occupied_positions.append(pos) 
        
        all_players = copied_game.players
        
        current_dice_value = copied_game.dice_value 

        #deep copy of methods 

    def minimax(game_state, depth, is_maximizing) :
        if game_state == "over" or depth == 0 :
            return AI.evaluate(game_state) 

    def alpha_beta(game_state, depth, alpha, beta, is_maximizing) :
        pass 

    def evaluation_func(game_state) :
        pass 