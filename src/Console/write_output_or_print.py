import csv


def write_output_or_print(filename, data):
    if filename:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data.values())
    else:
        print(f"Faktura z {data['invoice_date']} na kwotę {data['invoice_amount']} "
              f"{data['invoice_currency']}, płatność z {data['payment_date']} w kwocie "
              f"{data['payment_amount']} {data['payment_currency']}, do dopłaty pozostało: "
              f"{data['amount_in_pln_to_pay']} PLN (przelicznik w/g NBP z dn. "
              f"{data['payment_date']}: {data['payment_rate_to_pln']})")
