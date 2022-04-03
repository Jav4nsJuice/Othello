from movesHelper import MovesHelper
from copy import deepcopy
from settings import Settings


class MinMax:
    computer = None
    beta = None
    alpha = None

    @staticmethod
    def min_max_with_depth(current_player, board, player_enemy, unique_values):
        MinMax.beta = Settings.highest_value
        MinMax.alpha = Settings.lowest_value

        MinMax.computer = deepcopy(current_player)
        p_moves = MovesHelper.get_possible_moves(MinMax.computer, deepcopy(board))

        if len(p_moves) > 1:
            heuristic_values = []
            for p_move in deepcopy(unique_values):
                new_board = deepcopy(board)
                new_move = deepcopy(p_move)
                new_enemy = deepcopy(player_enemy)
                adv_search = MinMax._max_value(0, new_board, new_move, deepcopy(MinMax.computer ), new_enemy)
                heuristic_values.append(adv_search)
            return heuristic_values.index(min(heuristic_values)) + 1
        elif len(p_moves) == 1:
            return 1
        else:
            return None

    @staticmethod
    def _min_value(depth, board, possible_moves, current_player, player_enemy):
        MovesHelper.apply_move(board, current_player, player_enemy, possible_moves)

        if MinMax._cut_off(depth):
            computer = current_player if current_player.token == MinMax.computer.token else player_enemy
            return - MinMax._eval(board, computer, possible_moves)
        value = Settings.highest_value
        p_moves = MovesHelper.get_possible_moves(player_enemy, board)

        unique_opt, _ = MovesHelper.get_unique_final_pos(p_moves)
        for p_move in unique_opt:
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            new_board = deepcopy(board)
            new_possible_moves = deepcopy(p_move)
            value = min(value, MinMax._max_value(depth + 1, new_board, new_possible_moves, copied_enemy, copied_current_player))
            if value <= MinMax.alpha:
                return value
            MinMax.beta = min(MinMax.beta, value)
        return value

    @staticmethod
    def _max_value(depth, board, possible_moves, current_player, player_enemy):

        MovesHelper.apply_move(board, current_player, player_enemy, possible_moves)

        if MinMax._cut_off(depth):
            computer = current_player if current_player.token == MinMax.computer.token else player_enemy
            return - MinMax._eval(board, computer,possible_moves)

        value = Settings.lowest_value
        p_moves = MovesHelper.get_possible_moves(player_enemy, board )

        unique_opt, _ = deepcopy(MovesHelper.get_unique_final_pos(p_moves))

        for p_move in unique_opt:
            new_enemy = deepcopy(player_enemy)
            new_c_player = deepcopy(current_player)
            new_board = deepcopy(board)
            new_possible_moves = deepcopy(p_move)
            value = max(value, MinMax._min_value(depth + 1, new_board, new_possible_moves, new_enemy, new_c_player))
            if value >= MinMax.beta:
                return value
            MinMax.alpha = max(MinMax.alpha, value)
        return value

    @staticmethod
    def _eval(state, computer, possible_moves):
        return Settings.heuristic(state, computer, possible_moves)

    @staticmethod
    def _cut_off(depth):
        return depth == Settings.max_depth