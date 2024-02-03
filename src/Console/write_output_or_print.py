import csv


def write_output_or_print(filename, dict_data):
    if filename:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(dict_data.values())
    else:
        print(dict_data)
