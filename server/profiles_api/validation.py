class Validation:

    @staticmethod
    def is_valid_range(value, max_value, min_value):
        if min_value < value <= max_value:
            return True
        else:
            return False

    @staticmethod
    def is_not_required_game_field(board):
        if len(board):
            return True
        else:
            return False
