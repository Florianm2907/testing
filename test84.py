def trim_lines(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()  # Read lines and strip newline characters

    trimmed_line = ', '.join(lines)  # Join lines with ', ' as separator

    print(trimmed_line)  # Print the single trimmed line to the console

if __name__ == "__main__":
    input_file = './image'
    trim_lines(input_file)
