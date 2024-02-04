from Api import CurrencyDataSource
from Calculator.Invoice import Invoice
from Calculator.Payment import Payment


class Calculator:
    def __init__(self, data_source: CurrencyDataSource):
        self.data_source = data_source

    def calculate(self, invoice: Invoice, payment: Payment):
        invoice_rate = self.data_source.get_average_currency_rate(invoice.currency, invoice.date)
        payment_rate = self.data_source.get_average_currency_rate(payment.currency, payment.date)

        invoice_amount_pln = invoice.amount * invoice_rate
        payment_amount_pln = payment.amount * payment_rate

        difference = invoice_amount_pln - payment_amount_pln

        return {
            "amount_in_pln_to_pay": abs(round(difference, 2)),
            "invoice_date": invoice.date,
            "invoice_amount": invoice.amount,
            "invoice_currency": invoice.currency,
            "invoice_rate_to_pln": invoice_rate,
            "payment_date": payment.date,
            "payment_amount": payment.amount,
            "payment_currency": payment.currency,
            "payment_rate_to_pln": payment_rate
        }
