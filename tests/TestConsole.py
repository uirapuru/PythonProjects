import io
import unittest
from unittest.mock import MagicMock, patch
from Console.Console import Console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.calculator_mock = MagicMock()
        self.console = Console(self.calculator_mock)

    @patch('Console.validation.validate_amount', side_effect=lambda x: float(x))
    @patch('Console.validation.validate_currency', side_effect=lambda x: x)
    @patch('Console.validation.validate_date', side_effect=lambda x: x)
    @patch('Console.validation.validate_output', side_effect=lambda x: x)
    @patch('builtins.input', side_effect=['100', 'USD', '2023-01-01', '120', 'EUR', '2023-01-10', ''])
    @patch('builtins.print')
    def test_run_interactive_mode_with_valid_input(self, mock_print, mock_input, mock_validate_output, mock_validate_date, mock_validate_currency, mock_validate_amount):
        args_dict = self.console.run_interactive_mode()
        self.assertEqual(args_dict, {
            "invoice_amount": 100.0,
            "invoice_currency": 'USD',
            "invoice_date": '2023-01-01',
            "payment_amount": 120.0,
            "payment_currency": 'EUR',
            "payment_date": '2023-01-10',
            "output": '',
            "currencies": None,
            "filename": None
        })

        mock_print.assert_any_call("Uruchomiono tryb interaktywny.")

        self.assertEqual(mock_input.call_count, 7)

    # @patch('builtins.input', side_effect=['invalid', 'USD', 'invalid-date', '120', 'EUR', '2023-01-10', ''])
    # @patch('builtins.print')
    # @patch('Console.validation.validate_amount', side_effect=[ValueError("Kwota musi być liczbą."), float])
    # def test_run_interactive_mode_with_invalid_input(self, mock_validate_amount, mock_print, mock_input):
    #     self.console.run_interactive_mode()
    #     mock_print.assert_any_call("Kwota musi być liczbą.")

    @patch('sys.argv', ['program_name', '--filename', 'nonexistent.csv'])
    def test_run_with_file_not_found(self):
        with patch('os.path.exists', return_value=False):
            with patch('builtins.print') as mocked_print:
                self.console.run()
                mocked_print.assert_called_with('Plik nonexistent.csv nie istnieje.', file=unittest.mock.ANY)

    def test_process_row_with_unsupported_currency(self):
        args = unittest.mock.MagicMock(output=None, currencies="USD,EUR")
        currencies = ['USD', 'EUR']
        row = ['100', 'USD', '2023-01-01', '120', 'GBP', '2023-01-10']

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.process_row(row, args, currencies)
            self.assertIn("Pomijanie waluty: GBP (dozwolone waluty to: ['USD', 'EUR'])", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
