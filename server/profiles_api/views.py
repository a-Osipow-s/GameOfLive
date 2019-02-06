import itertools

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .validation import Validation
from .constant_error_description import ValidationErrorDescription


class GameOfLive(APIView):

    serializer_class = serializers.GameOfLiveSerializer

    board_array = []
    last_step = False
    error_description = ""

    def post(self, request):
        serializer = serializers.GameOfLiveSerializer(data=request.data)
        if serializer.is_valid():
            board = self.get_board_with_request(serializer.data.get('board'))
            width = self.get_size_with_request(serializer.data.get('width'))
            height = self.get_size_with_request(serializer.data.get('height'))
            if board and width and height:
                self.is_repeated_board(board)
                return Response(
                    {'board_next_step': self.start_game(width['value'], height['value'], board),
                     'last_step': self.last_step})
            else:
                return Response(
                    data=self.error_description, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def is_repeated_board(self, board):
        index = len(self.board_array)
        if board in self.board_array and board == self.board_array[index-1]:
            self.last_step = True
        else:
            self.board_array.append(board)

    def get_board_with_request(self, board_request):
        board = list(map(tuple, board_request))
        if Validation.is_not_required_game_field(board):
            if Validation.is_valid_coord(list(map(lambda x: len(x), board))):
                return board
            else:
                self.error_description = ValidationErrorDescription.ERROR_INVALID_BOARD
                return False
        else:
            self.error_description = ValidationErrorDescription.ERROR_REQUIRED_BOARD
            return False

    def get_size_with_request(self, get_size):
        if Validation.is_valid_range(get_size['value'],
                                     get_size['maxValue'],
                                     get_size['minValue']):
            return get_size
        else:
            self.error_description = ValidationErrorDescription.ERROR_NUMBER_OUT_RANGE
            return False

    @staticmethod
    def get_neighbors(con):
        x, y = con
        neighbors = [(x + i, y + j) for i in range(-1, 2)
                                    for j in range(-1, 2)
                                    if not i == j == 0]
        return neighbors

    def calculate_alive_neighbors(self, con, alive_cons):
        return len(list(filter(lambda x: x in alive_cons,
                        self.get_neighbors(con))))

    def is_alive_con(self, con, alive_cons):
        alive_neighbors = self.calculate_alive_neighbors(con, alive_cons)
        if (alive_neighbors == 3 or
                (alive_neighbors == 2 and con in alive_cons)):
            return True
        return False

    def new_step(self, alive_cons):
        board = itertools.chain(*map(self.get_neighbors, alive_cons))
        new_board = set([con
                        for con in board
                        if self.is_alive_con(con, alive_cons)])
        return list(new_board)

    @staticmethod
    def is_correct_con(width, height, con):
        x, y = con
        return 0 <= y <= width - 1 and 0 <= x <= height - 1

    def correct_cons(self, width, height, cons):
        return list(filter(lambda x: self.is_correct_con(width, height, x), cons))

    def start_game(self, width, height, board):
        return self.correct_cons(width, height, self.new_step(board))
