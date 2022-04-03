from MinMax import MinMax
from movesHelper import MovesHelper
from copy import deepcopy
from settings import Settings
import numpy


def display_options(player, options):
    indice = 1
    print(player.name, "Choose one option, your token is ", player.token, ":")
    for opt in options:
        print(f"{indice}: {Settings.letters[opt[1]]} {opt[0] + 1}")
        indice += 1


def _is_out_of_bounds(col, row):
    return col < 0 or row < 0 or col >= Settings.board_size or row >= Settings.board_size or col >= Settings.board_size


class MovesManager:
    def __init__(self, board):
        self.player1 = None
        self.player2 = None
        self.board = board

    def get_possible_moves(self, player):
        return MovesHelper.get_possible_moves(player, self.board)

    def make_move(self, player, possible_moves, player_enemy, computer_turn):

        unique_values, unique_opt = MovesHelper.get_unique_final_pos(possible_moves)
        while True:
            display_options(player, unique_opt)
            if computer_turn:
                option_decided = MinMax.min_max_with_depth(player, deepcopy(self.board), player_enemy, unique_values)
                # option_decided = numpy.random.randint(1, len(unique_opt) + 1)

            else:
                option_decided = int(input())
                #option_decided = numpy.random.randint(1, len(unique_opt) + 1)
                #option_decided = 1
            print("choice:", option_decided)

            if option_decided in range(1, len(unique_opt) + 1):
                break
            print("Choose one of the options please!")
        MovesHelper.apply_move(self.board, player,  player_enemy, unique_values[option_decided-1])