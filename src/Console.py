import argparse
import csv
import os
import sys

from src.get_currencies import get_currencies
from src.write_output_or_print import write_output_or_print


class Console:
    def __init__(self, calculator):
        self.calculator = calculator
        self.parser = argparse.ArgumentParser(description='Obliczanie różnic walutowych dla faktur')
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument('--filename', '-f', type=str, help='Nazwa pliku do odczytu')
        self.parser.add_argument('--input', '-i', type=str, help='Dane faktur')
        self.parser.add_argument('--output', '-o', type=str, help='Nazwa pliku wyjściowego do zapisu wyników')
        self.parser.add_argument('--currencies', '-c', type=str, help='Dozwolone waluty po przecinku')

    def run(self):
        args = self.parser.parse_args()

        if len(sys.argv) == 1:
            self.parser.print_help(sys.stderr)
            sys.exit(1)

        if not args.filename:
            print("Nie podano nazwy pliku", file=sys.stderr)
            sys.exit(1)

        if args.output and os.path.exists(args.output):
            os.remove(args.output)

        currencies = get_currencies(args.currencies)

        try:
            with open(args.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    result = self.calculator.calculate(row, currencies)
                    write_output_or_print(args.output, result)

        except FileNotFoundError:
            print(f"Plik {args.filename} nie istnieje.", file=sys.stderr)

        except Exception as e:
            print(f"Wystąpił błąd podczas odczytu pliku: {e}", file=sys.stderr)
