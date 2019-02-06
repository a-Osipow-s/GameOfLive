from django.test import TestCase, Client
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from .constant_var_for_data_validation_test import \
    VariableForTestValidationData, VariableForTestGameOfLive
from .constant_error_description import ValidationErrorDescription


class TestValidationData(APITestCase):

    client = RequestsClient()

    def test_request_valid_data(self):
        data = {
            "board": VariableForTestValidationData.VALID_BOARD,
            "width": VariableForTestValidationData.VALID_WIDTH,
            "height": VariableForTestValidationData.VALID_HEIGHT
        }
        response = self.client.post(
            VariableForTestValidationData.URL, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_request_data_with_invalid_width(self):
        data = {
            "board": VariableForTestValidationData.VALID_BOARD,
            "width": VariableForTestValidationData.INVALID_WIDTH,
            "height": VariableForTestValidationData.VALID_HEIGHT
        }
        response = self.client.post(
            VariableForTestValidationData.URL, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, ValidationErrorDescription.ERROR_NUMBER_OUT_RANGE)

    def test_request_data_with_invalid_height(self):
        data = {
            "board": VariableForTestValidationData.VALID_BOARD,
            "width": VariableForTestValidationData.VALID_WIDTH,
            "height": VariableForTestValidationData.INVALID_HEIGHT
        }
        response = self.client.post(
            VariableForTestValidationData.URL, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, ValidationErrorDescription.ERROR_NUMBER_OUT_RANGE)

    def test_request_data_with_invalid_board(self):
        data = {
            "board": VariableForTestValidationData.INVALID_BOARD,
            "width": VariableForTestValidationData.VALID_WIDTH,
            "height": VariableForTestValidationData.VALID_HEIGHT
        }
        response = self.client.post(
            VariableForTestValidationData.URL, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, ValidationErrorDescription.ERROR_INVALID_BOARD)

    def test_request_data_with_required_board(self):
        data = {
            "board": VariableForTestValidationData.REQUIRED_BOARD,
            "width": VariableForTestValidationData.VALID_WIDTH,
            "height": VariableForTestValidationData.VALID_HEIGHT
        }
        response = self.client.post(
            VariableForTestValidationData.URL, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, ValidationErrorDescription.ERROR_REQUIRED_BOARD)


class TestGameOfLive(APITestCase):

    client = RequestsClient()

    def test_next_board_step(self):
        data = {
            "board": VariableForTestGameOfLive.VALID_BOARD,
            "width": VariableForTestGameOfLive.VALID_WIDTH,
            "height": VariableForTestGameOfLive.VALID_HEIGHT
        }
        response = self.client.post(
            VariableForTestValidationData.URL, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['board_next_step'],
                         VariableForTestGameOfLive.BOARD_NEXT_STEP)
