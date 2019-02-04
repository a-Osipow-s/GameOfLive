class Validation:

    @staticmethod
    def is_valid_range(value, max_value, min_value):
        return min_value < value <= max_value

    @staticmethod
    def is_not_required_game_field(board):
        return len(board)

    @staticmethod
    def is_valid_coord(list_len_of_coordinates):
        for len_coord in list_len_of_coordinates:
            if len_coord != 2:
                return False
        return True
