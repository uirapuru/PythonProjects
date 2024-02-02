import unittest
from unittest.mock import Mock, patch
import sys
from Console.Console import Console
from Calculator.Calculator import Calculator


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.mock_calculator = Mock(spec=Calculator)
        self.console = Console(self.mock_calculator)

    # @patch('builtins.print')
    # def test_missing_filename_argument(self, mock_print):
    #     test_args = ['prog', '--input', 'test_data']
    #     with patch.object(sys, 'argv', test_args):
    #         with self.assertRaises(SystemExit) as cm:
    #             self.console.run()
    #         self.assertEqual(cm.exception.code, 1)
    #         mock_print.assert_called_with("Nie podano nazwy pliku", file=sys.stderr)


    @patch('builtins.print')
    def test_invalid_currency_argument(self, mock_print):
        test_args = ['prog', '--filename', 'data.csv', '--currencies', 'INVALID']
        with patch.object(sys, 'argv', test_args):
            try:
                self.console.run()
            except SystemExit:
                pass

    @patch('builtins.print')
    def test_valid_currency_argument(self, mock_print):
        test_args = ['prog', '--filename', 'data.csv', '--currencies', 'USD,EUR']
        with patch.object(sys, 'argv', test_args):
            try:
                self.console.run()
            except SystemExit:
                pass

    @patch('builtins.print')
    def test_output_argument_with_existing_file(self, mock_print):
        test_args = ['prog', '--filename', 'data.csv', '--output', 'existing_output.csv']
        with patch.object(sys, 'argv', test_args), patch('os.path.exists', return_value=True), patch('os.remove') as mock_remove:
            try:
                self.console.run()
            except SystemExit:
                pass
            mock_remove.assert_called_with('existing_output.csv')

    @patch('builtins.print')
    def test_output_argument_without_existing_file(self, mock_print):
        test_args = ['prog', '--filename', 'data.csv', '--output', 'new_output.csv']
        with patch.object(sys, 'argv', test_args), patch('os.path.exists', return_value=False):
            try:
                self.console.run()
            except SystemExit:
                pass

    @patch('builtins.input', side_effect=['100', 'USD', '2022-01-01', '120', 'EUR', '2022-01-10'])
    @patch('builtins.print')
    def test_run_interactive_mode(self, mock_print, mock_input):
        self.console.run_interactive_mode()
        # Dodaj asercje dotyczące zachowania po interakcji z użytkownikiem.


if __name__ == '__main__':
    unittest.main()
