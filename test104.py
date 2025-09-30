'''5. Even or Odd Number Checker
	•	Ask user for a number.
	•	Tell them if it’s even or odd.
	•	Extend it: run continuously until the user types exit.'''

number = input("Enter your number to check whether it is even or odd: ")
while True:
    try: number = int(number); break
    except: number = input("\nInput is not a number! Try again: ")
while True:
    # print("Number is even.") if (number % 2) == 0 else print("Number is odd.")
    number = input(f"Number is {"even" if (number % 2) == 0 else "odd"}. Do you want to continue? Enter another number or enter 'exit' to exit: ")
    if number.lower() == "exit": exit()
    try: number = int(number)
    except: input("\nInput is not a number! Try again: ")