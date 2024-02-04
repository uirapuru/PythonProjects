import argparse
import csv
import os
import sys

from Calculator.Invoice import Invoice
from Calculator.Payment import Payment
from Console.get_currencies import get_currencies
from Console.validation import validate_amount, validate_currency, validate_date, validate_output
from Console.write_output_or_print import write_output_or_print


class Console:
    """
    Klasa Console służy do interaktywnego obliczania różnic walutowych dla faktur
    oraz opcjonalnego zapisu wyników do pliku.

    Attributes:
        calculator (Calculator): Obiekt kalkulatora używany do obliczeń.
        parser (ArgumentParser): Parser argumentów linii poleceń.
    """

    def __init__(self, calculator):
        """
        Inicjalizuje konsolę z podanym kalkulatorem.

        Args:
            calculator (Calculator): Obiekt kalkulatora używany do obliczeń.
        """
        self.calculator = calculator
        self.parser = argparse.ArgumentParser(description='Obliczanie różnic walutowych dla faktur')
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument('--filename', '-f', type=str, help='Nazwa pliku do odczytu')
        self.parser.add_argument('--output', '-o', type=str, help='Nazwa pliku wyjściowego do zapisu wyników')
        self.parser.add_argument('--currencies', '-c', type=str, help='Dozwolone waluty po przecinku')

    def run_interactive_mode(self):
        """
        Uruchamia tryb interaktywny, pozwalając użytkownikowi na wprowadzenie danych faktury i płatności,
        a następnie oblicza różnicę walutową i opcjonalnie zapisuje wynik.

        Returns:
            dict: Słownik zawierający dane wejściowe użytkownika i wynik obliczeń.
        """
        print("Uruchomiono tryb interaktywny.")
        try:
            invoice_amount = validate_amount(input("Podaj kwotę na fakturze: "))
            invoice_currency = input("Podaj walutę na fakturze: ").upper()
            validate_currency(invoice_currency)
            invoice_date = input("Podaj datę wystawienia faktury (YYYY-MM-DD): ")
            validate_date(invoice_date)
            payment_amount = validate_amount(input("Podaj kwotę zapłaconą: "))
            payment_currency = input("Podaj walutę płatności: ").upper()
            validate_currency(payment_currency)
            payment_date = input("Podaj datę dokonania płatności (YYYY-MM-DD): ")
            validate_date(payment_date)

            output = input("Podaj nazwę pliku wyjściowego lub pozostaw puste, aby wyświetlić wynik: ")
            validate_output(output)

            return {
                "invoice_amount": invoice_amount,
                "invoice_currency": invoice_currency,
                "invoice_date": invoice_date,
                "payment_amount": payment_amount,
                "payment_currency": payment_currency,
                "payment_date": payment_date,
                "output": output,
                "currencies": None,
                "filename": None
            }
        except ValueError as e:
            print(e)
            return {}

    def run(self):
        """
        Główna metoda uruchamiająca logikę programu. Przetwarza argumenty linii poleceń
        lub uruchamia tryb interaktywny, jeśli nie podano argumentów.
        """
        args = self.parser.parse_args()

        if len(sys.argv) == 1:
            args_dict = self.run_interactive_mode()
            args = argparse.Namespace(**args_dict)

        if args.output and os.path.exists(args.output):
            os.remove(args.output)

        currencies = get_currencies(args.currencies)

        try:
            with open(args.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                column_names = next(reader)

                try:
                    float(column_names[0])

                    for row in [column_names] + list(reader):
                        self.process_row(row, args, currencies)

                except ValueError:
                    for row in reader:
                        self.process_row(row, args, currencies)

        except FileNotFoundError:
            print(f"Plik {args.filename} nie istnieje.", file=sys.stderr)

        except Exception as e:
            print(f"Wystąpił błąd podczas odczytu pliku: {e}", file=sys.stderr)

    def process_row(self, row, args, currencies):
        """
        Przetwarza pojedynczy wiersz danych, obliczając różnice walutowe i zapisując lub wypisując wynik.

        Args:
            row (list): Wiersz danych do przetworzenia.
            args (Namespace): Argumenty linii poleceń.
            currencies (set): Zestaw dozwolonych walut.
        """
        if row[4].upper() not in currencies:
            print(f"Pomijanie waluty: {row[4]} (dozwolone waluty to: {currencies})")
            return

        invoice = Invoice(row[0], row[1], row[2])
        payment = Payment(row[3], row[4], row[5])
        result = self.calculator.calculate(invoice, payment)
        write_output_or_print(args.output, result)
