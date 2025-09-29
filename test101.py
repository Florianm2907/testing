#calculator
'''2. Simple Calculator
Ask user for two numbers and an operation (+, -, *, /).
Perform the calculation and print the result.
Add support for multiple operations until the user types quit. #fuh naw not yet that shit is hard, dealing with floats and shit'''

while True:
    input_1 = 0
    input_2 = 0
    operation = ""
    result = 0
    print("Calculator\n---\n")

    while True:
        input_1 = input("Input first number: ")
        try:
            input_1 = int(input_1)
            break
        except:
            print("Invalid input! Ensure input is a number")

    while True:
        operation = input("Input operation (+, -, x, /): ").upper()
        if operation in ("+", "-", "X", "/"):
            break
        else:
            print("Invalid input! Ensure input is a valid operation")

    while True:
        input_2 = input("Input second number: ")
        try:
            input_2 = int(input_2)
            break
        except:
            print("Invalid input! Ensure input is a number")


    if operation == "+":
        result = input_1 + input_2
        print(f"{input_1} + {input_2} is equal to {result}")
    elif operation == "-":
        result = input_1 - input_2
        print(f"{input_1} - {input_2} is equal to {result}")
    elif operation == "X":
        result = input_1 * input_2
        print(f"{input_1} x {input_2} is equal to {result}")
    elif operation == "/":
        if input_2 == 0:
            print("Error! Division by zero")
            continue
        result = input_1 / input_2
        print(f"{input_1} / {input_2} is equal to {result}")

    while True:
        new_calculation_query = ""
        new_calculation_query = input("Would you like to start a new calculation (Y/N)? ").upper()
        if new_calculation_query in ("Y", "N"):
            if new_calculation_query == "N":
                exit()
            else:
                print("\n\n\n\n\n\n\n\n")
                break
        else:
            print("Invalid option! Ensure input is a valid option")