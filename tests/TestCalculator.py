import unittest
from unittest.mock import MagicMock

from Api.CurrencyDataSource import CurrencyDataSource
from Calculator.Calculator import Calculator
from Calculator.Invoice import Invoice
from Calculator.Payment import Payment


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.mock_data_source = MagicMock(spec=CurrencyDataSource)
        self.calculator = Calculator(data_source=self.mock_data_source)

    def test_calculate_success(self):
        self.mock_data_source.get_average_currency_rate.side_effect = lambda currency, date: 4.0 if currency == 'EUR' else 3.8
        invoice = Invoice(amount=100, currency='EUR', date='2022-01-01')
        payment = Payment(amount=100, currency='EUR', date='2022-01-10')

        result = self.calculator.calculate(invoice, payment)

        self.assertEqual(result['amount_in_pln_to_pay'], 0)
        self.assertEqual(result['invoice_rate_to_pln'], 4.0)
        self.assertEqual(result['payment_rate_to_pln'], 4.0)

    def test_calculate_with_rate_difference(self):
        self.mock_data_source.get_average_currency_rate.side_effect = lambda currency, date: 4.0 if date == '2022-01-01' else 3.8
        invoice = Invoice(amount=100, currency='EUR', date='2022-01-01')
        payment = Payment(amount=100, currency='EUR', date='2022-01-10')

        result = self.calculator.calculate(invoice, payment)

        self.assertNotEqual(result['amount_in_pln_to_pay'], 0)

    def test_calculate_error_handling(self):
        self.mock_data_source.get_average_currency_rate.side_effect = Exception("API error")

        with self.assertRaises(Exception) as context:
            invoice = Invoice(amount=100, currency='EUR', date='2022-01-01')
            payment = Payment(amount=100, currency='EUR', date='2022-01-10')
            self.calculator.calculate(invoice, payment)

        self.assertTrue('API error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
