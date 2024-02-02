import unittest
from unittest.mock import patch

from Api.NBPApiAdapter import NBPApiAdapter


class TestNBPApiAdapter(unittest.TestCase):

    def setUp(self):
        self.adapter = NBPApiAdapter()

    @patch('requests.get')
    def test_get_average_currency_rate_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': [{'mid': 3.5}]
        }

        rate = self.adapter.get_average_currency_rate('USD', '2022-01-01')
        self.assertEqual(rate, 3.5)

    @patch('requests.get')
    def test_get_average_currency_rate_invalid_currency(self, mock_get):
        with self.assertRaises(ValueError):
            self.adapter.get_average_currency_rate('invalid', '2022-01-01')

    @patch('requests.get')
    def test_get_average_currency_rate_api_error(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        with self.assertRaises(Exception):
            self.adapter.get_average_currency_rate('USD', '2022-01-01')


if __name__ == '__main__':
    unittest.main()
