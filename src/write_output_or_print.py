def write_output_or_print(filename, line):
    if filename:
        with open(filename, 'a') as file:
            file.write(str(line) + '\n')
    else:
        print(line)