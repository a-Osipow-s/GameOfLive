class VariableForTestValidationData:

    URL = "http://0.0.0.0:7000/api/game-of-live/"

    VALID_WIDTH = {'value': 10, "maxValue": 20, "minValue": 0}
    VALID_HEIGHT = {"value": 10, "maxValue": 20, "minValue": 0}
    VALID_BOARD = [[1, 2], [2, 1], [2, 2]]

    INVALID_WIDTH = {'value': 60, 'maxValue': 50, 'minValue': 0}
    INVALID_HEIGHT = {'value': 8, 'maxValue': 20, 'minValue': 10}
    INVALID_BOARD = [[1, 2, 4], [2, 1], [1, 0]]
    REQUIRED_BOARD = []


class VariableForTestGameOfLive:

    VALID_WIDTH = {'value': 3, "maxValue": 20, "minValue": 0}
    VALID_HEIGHT = {"value": 3, "maxValue": 20, "minValue": 0}
    VALID_BOARD = [[0, 1], [1, 1], [2, 1]]
    BOARD_NEXT_STEP = [(1, 2), (1, 0), (1, 1)]
