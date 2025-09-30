'''5. Even or Odd Number Checker
	•	Ask user for a number.
	•	Tell them if it’s even or odd.
	•	Extend it: run continuously until the user types exit.'''

while True:
    number = input("Enter your number to check whether it is even or odd: ")
    try: number = int(number); break
    except: input("\nInput is not a number! Try again: ")
print("Number is even.") if (number % 2) == 0 else print("Number is odd.")