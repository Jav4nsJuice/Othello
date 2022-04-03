from move import Move
from settings import Settings


class MovesHelper:

    @staticmethod
    def gst_unique_values(list_with_duplicated_values):
        unique_list = []
        for x in list_with_duplicated_values:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    @staticmethod
    def get_unique_final_pos(list_with_duplicated_values):
        values = list(map(lambda m: m.final_pos, list_with_duplicated_values))
        unique_list = MovesHelper.get_unique_values(values)
        final_list = []
        for x in unique_list:
            final_list.append(list(filter(lambda v: v.final_pos == x, list_with_duplicated_values)))
        return final_list, unique_list

    @staticmethod
    def get_next_position(action, col, row):
        next_column = None
        next_row = None
        if action == "UP":
            next_row = row - 1
            next_column = col
        if action == "UP-RIGHT":
            next_row = row - 1
            next_column = col + 1
        if action == "RIGHT":
            next_row = row
            next_column = col + 1
        if action == "DOWN-RIGHT":
            next_row = row + 1
            next_column = col + 1
        if action == "DOWN":
            next_row = row + 1
            next_column = col
        if action == "LEFT-DOWN":
            next_row = row + 1
            next_column = col - 1
        if action == "LEFT":
            next_row = row
            next_column = col - 1
        if action == "LEFT-UP":
            next_row = row - 1
            next_column = col - 1
        return next_column, next_row

    @staticmethod
    def _is_out_of_bounds(col, row):
        return col < 0 or row < 0 or col >= Settings.board_size or row >= Settings.board_size or col >= Settings.board_size

    @staticmethod
    def get_possible_moves(player, board):
        possible_moves = []
        enemy_token = Settings.p2_token if player.token == Settings.p1_token else Settings.p1_token
        for token_pos in player.tokens_on_board:
            for action in Settings.actions:
                enemy_found = False
                first_iteration = True
                winnable_cells = 0
                col, row = MovesHelper.get_next_position(action, token_pos[1], token_pos[0])
                while True:

                    if MovesHelper._is_out_of_bounds(col, row):
                        break

                    if first_iteration:
                        if board.cells[row][col].token != enemy_token:
                            break
                        first_iteration = False

                    if board.cells[row][col].token == Settings.empty_token and enemy_found:
                        possible_moves.append(Move((row, col), (token_pos[0], token_pos[1]), action, winnable_cells))
                        break

                    if board.cells[row][col].token == Settings.empty_token:
                        break

                    if board.cells[row][col].token == player.token:
                        break

                    if board.cells[row][col].token == enemy_token:
                        enemy_found = True
                        winnable_cells += 1
                        col, row = MovesHelper.get_next_position(action, col, row)
                        continue

                    col, row = MovesHelper.get_next_position(action, col, row)
                    enemy_found = False
        return possible_moves

    @staticmethod
    def apply_move(board, player, player_enemy, possible_moves):
        for pos in possible_moves:
            current_pos = pos.initial_pos
            while True:
                col, row = MovesHelper.get_next_position(pos.action, current_pos[1], current_pos[0])
                board.place_token(row, col, player.token)
                # board.cells[row][col].token = player.token
                current_pos = (row, col)
                player.tokens_on_board.append(current_pos)
                if current_pos == pos.final_pos:
                    player.tokens_on_board = MovesHelper.get_unique_values(player.tokens_on_board)
                    break
                player_enemy.tokens_on_board.remove(current_pos)
from move import Move
from settings import Settings


class MovesHelper:

    @staticmethod
    def get_unique_values(list_with_duplicated_values):
        unique_list = []
        for x in list_with_duplicated_values:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    @staticmethod
    def get_unique_final_pos(list_with_duplicated_values):
        values = list(map(lambda m: m.final_pos, list_with_duplicated_values))
        unique_list = MovesHelper.get_unique_values(values)
        final_list = []
        for x in unique_list:
            final_list.append(list(filter(lambda v: v.final_pos == x, list_with_duplicated_values)))
        return final_list, unique_list

    @staticmethod
    def get_next_position(action, col, row):
        next_column = None
        next_row = None
        if action == "UP":
            next_row = row - 1
            next_column = col
        if action == "UP-RIGHT":
            next_row = row - 1
            next_column = col + 1
        if action == "RIGHT":
            next_row = row
            next_column = col + 1
        if action == "DOWN-RIGHT":
            next_row = row + 1
            next_column = col + 1
        if action == "DOWN":
            next_row = row + 1
            next_column = col
        if action == "LEFT-DOWN":
            next_row = row + 1
            next_column = col - 1
        if action == "LEFT":
            next_row = row
            next_column = col - 1
        if action == "LEFT-UP":
            next_row = row - 1
            next_column = col - 1
        return next_column, next_row

    @staticmethod
    def _is_out_of_bounds(col, row):
        return col < 0 or row < 0 or col >= Settings.board_size or row >= Settings.board_size or col >= Settings.board_size

    @staticmethod
    def get_possible_moves(player, board):
        possible_moves = []
        enemy_token = Settings.p2_token if player.token == Settings.p1_token else Settings.p1_token
        for token_pos in player.tokens_on_board:
            for action in Settings.actions:
                enemy_found = False
                first_iteration = True
                winnable_cells = 0
                col, row = MovesHelper.get_next_position(action, token_pos[1], token_pos[0])
                while True:

                    if MovesHelper._is_out_of_bounds(col, row):
                        break

                    if first_iteration:
                        if board.cells[row][col].token != enemy_token:
                            break
                        first_iteration = False

                    if board.cells[row][col].token == Settings.empty_token and enemy_found:
                        possible_moves.append(Move((row, col), (token_pos[0], token_pos[1]), action, winnable_cells))
                        break

                    if board.cells[row][col].token == Settings.empty_token:
                        break

                    if board.cells[row][col].token == player.token:
                        break

                    if board.cells[row][col].token == enemy_token:
                        enemy_found = True
                        winnable_cells += 1
                        col, row = MovesHelper.get_next_position(action, col, row)
                        continue

                    col, row = MovesHelper.get_next_position(action, col, row)
                    enemy_found = False
        return possible_moves

    @staticmethod
    def apply_move(board, player, player_enemy, possible_moves):
        for pos in possible_moves:
            current_pos = pos.initial_pos
            while True:
                col, row = MovesHelper.get_next_position(pos.action, current_pos[1], current_pos[0])
                board.place_token(row, col, player.token)
                # board.cells[row][col].token = player.token
                current_pos = (row, col)
                player.tokens_on_board.append(current_pos)
                if current_pos == pos.final_pos:
                    player.tokens_on_board = MovesHelper.get_unique_values(player.tokens_on_board)
                    break
                player_enemy.tokens_on_board.remove(current_pos)