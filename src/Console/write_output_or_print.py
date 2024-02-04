import csv


def write_output_or_print(filename, data):
    """
    Zapisuje informacje o płatności do pliku CSV lub wypisuje je na ekran, w zależności od podanej nazwy pliku.

    Funkcja oblicza status płatności na podstawie kwoty pozostałej do zapłaty (amount_in_pln_to_pay) w danych.
    Generuje komunikat o statusie płatności, informując o dopłacie, nadpłacie lub pełnej zapłacie faktury.
    Jeśli podana jest nazwa pliku (filename), informacje są dopisywane do pliku CSV.
    W przeciwnym przypadku, informacje są wypisywane na standardowe wyjście.

    Args:
        filename (str): Nazwa pliku, do którego mają zostać zapisane dane. Jeśli None, dane są wypisywane na ekran.
        data (dict): Słownik zawierający informacje o płatności, w tym kwotę faktury, walutę, datę faktury,
                     kwotę płatności, walutę płatności, pozostałą kwotę do zapłaty w PLN,
                     oraz przelicznik waluty płatności na PLN.

    Returns:
        None
    """
    if data['amount_in_pln_to_pay'] > 0:
        status_message = f"Do dopłaty pozostało: {data['amount_in_pln_to_pay']} PLN"
    elif data['amount_in_pln_to_pay'] < 0:
        status_message = f"Nadpłata: {abs(data['amount_in_pln_to_pay'])} PLN"
    else:
        status_message = "Faktura została opłacona w całości."

    if filename:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data.values())
    else:
        print(f"Faktura z {data['invoice_date']} na kwotę {data['invoice_amount']} "
              f"{data['invoice_currency']}, płatność z {data['payment_date']} w kwocie "
              f"{data['payment_amount']} {data['payment_currency']}. {status_message} "
              f"(przelicznik w/g NBP z dn. {data['payment_date']}: {data['payment_rate_to_pln']})")
