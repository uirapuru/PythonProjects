# Dokumentacja Użytkownika (PL)

## Opis programu
Program analizuje dane faktur i płatności w różnych walutach. Na podstawie kursu walut z dnia płatności, oblicza różnicę walutową do uregulowania. 

## Sposób użycia
Uruchom w terminalu Linux wpisując `./src/main.py`. Możesz podać argumenty lub uruchomić tryb interaktywny, nie podając żadnych argumentów.

### Argumenty
- `--filename=input.csv`: określa plik CSV zawierający dane do przetworzenia.
- `--output=output.csv`: (opcjonalnie) określa plik wyjściowy dla zapisu wyników. Jeśli nie podano, wyniki wyświetlane są w konsoli.
- `--currenciec=EUR,USD`: (opcjonalnie) określa dozwolone waluty

Dozwolone waluty można określić również za pomocą zmiennej środowiskowej CURRENCIES.

# User Documentation (EN)

## Program Description
The program analyzes invoice and payment data in various currencies. Based on the exchange rate on the payment date, it calculates the currency difference to be settled.

## How to Use
Run in the Linux terminal by typing `./src/main.py`. You can provide arguments or launch an interactive mode by not providing any arguments.

### Arguments
- `--filename=input.csv`: specifies the CSV file containing data to be processed.
- `--output=output.csv`: (optional) specifies the output file for saving results. If not provided, results are displayed in the console.
- `--currenciec=EUR,USD`: (optional) allowed currencies

You can also define allowed currencies with ENV variable CURRENCIES
