def split_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        line = file.read().strip()  # Read the single line and strip any surrounding whitespace

    values = line.split(', ')  # Split the line by ', ' to get individual values

    with open(output_file, 'w') as file:
        for value in values:
            file.write(value + '\n')  # Write each value on a new line

if __name__ == "__main__":
    input_file = "C:/Users/Florian/Desktop/Textdokument (neu) (3).txt"
    output_file = './output.txt'
    split_lines(input_file, output_file)
