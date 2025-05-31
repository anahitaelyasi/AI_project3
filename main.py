from game.player import Player
from game.game import Game
from game.ai import AI
from game.board import Board
from game.token import Token 


#Represents one player with three tokens

#Human player (max)
playerA = Player(
                    "A", True, 
                    [
                        Token("A", "base", 0, 0, False), 
                        Token("A", "base", 1, 0, False), 
                        Token("A", "base", 2, 0, False)
                    ],
                    "base", ["A_H1","A_H2","A_H3"], 0
                ) 

#Robot player (min1)
playerB = Player(
                    "B", False, 
                    [
                        Token("B", "base", 0, 0, False), 
                        Token("B", "base", 1, 0, False), 
                        Token("B", "base", 2, 0, False)
                    ], 
                    AI(), ["B_H1","B_H2","B_H3"], 0 
                 ) 
#Robot player (min2)
playerC = Player(
                   "C", False, 
                   [
                       Token("C", "base", 0, 0, False), 
                       Token("C", "base", 1, 0, False), 
                       Token("C", "base", 2, 0, False) 
                   ], 
                   AI(), ["C_H1","C_H2","C_H3"], 0
                )  

# Runs the whole game loop, manages turns, connects players and board
play_game = Game(
                   [playerA, playerB, playerC], 
                   Board(), 0 
                )

#self, players, board, current_player_index, dice_value, is_game_over, statistics

