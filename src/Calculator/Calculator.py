from Api import CurrencyDataSource
from Calculator.Invoice import Invoice
from Calculator.Payment import Payment


class Calculator:
    """
    Kalkulator do obliczania różnic walutowych między fakturami a płatnościami.

    Attributes:
        data_source (CurrencyDataSource): Źródło danych o kursach walut, z którego kalkulator pobiera informacje.
    """

    def __init__(self, data_source: CurrencyDataSource):
        """
        Inicjalizuje kalkulator z określonym źródłem danych o kursach walut.

        Args:
            data_source (CurrencyDataSource): Obiekt dostarczający dane o kursach walut.
        """
        self.data_source = data_source

    def calculate(self, invoice: Invoice, payment: Payment) -> dict:
        """
        Oblicza różnicę między kwotą faktury a kwotą płatności, przeliczając obie kwoty na PLN
        według kursu waluty na datę faktury i płatności.

        Args:
            invoice (Invoice): Obiekt faktury, zawierający kwotę, walutę i datę.
            payment (Payment): Obiekt płatności, zawierający kwotę, walutę i datę.

        Returns:
            dict: Słownik zawierający szczegółowe informacje o obliczeniach, w tym:
                - amount_in_pln_to_pay (float): Absolutna wartość różnicy między kwotą faktury a płatności w PLN,
                  zaokrąglona do dwóch miejsc po przecinku.
                - invoice_date (str): Data wystawienia faktury.
                - invoice_amount (float): Kwota faktury.
                - invoice_currency (str): Waluta faktury.
                - invoice_rate_to_pln (float): Kurs waluty faktury do PLN na datę faktury.
                - payment_date (str): Data płatności.
                - payment_amount (float): Kwota płatności.
                - payment_currency (str): Waluta płatności.
                - payment_rate_to_pln (float): Kurs waluty płatności do PLN na datę płatności.
        """
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
