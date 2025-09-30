'''6. Multiplication Quiz
	•	Generate a random multiplication question (like 7 x 9).
	•	Ask the user for the answer.
	•	Keep score for 5 questions, then print results.'''

import random

current_number1 = 0
current_number2 = 0
result = 0
def create_random():
    global current_number1
    global current_number2
    global result
    global questions_asked
    global answers
    current_number1 = random.randint(1,20)
    current_number2 = random.randint(1,20)
    result = current_number1 * current_number2
    questions_asked[f"{current_number1}x{current_number2}"] = result
    answers[f"{current_number1}x{current_number2}"] = None

print("This is a multiplication quiz! I will ask you multiplication questions and you have to enter the result. At the end, I will give you your score!")
while True:
    rounds = input("Enter the amount of questions you'd like to play: ")
    while True:
        try: rounds = int(rounds); break
        except: rounds = input("What you entered isn't a number. Enter the amount of rounds or type 'exit' to exit: ")
        if rounds.lower() == "exit": exit()
    while True:
        questions_asked = {}
        answers = {}
        current_question = 1
        points = 0
        for i in range(rounds):
            create_random()
            answer = input(f"Question {current_question}: What is {current_number1} x {current_number2}? ")
            while True:
                try: answer = int(answer); break
                except: answer = input(f"Input is not a number, try again. What is {current_number1} x {current_number2}? ")
            answers[f"{current_number1}x{current_number2}"] = answer
            if answer == result: 
                print("Correct!")
                points += 1
            else: print(f"Wrong answer! The correct answer would've been {result}!")
        print(f"\nThe quiz is done! I asked you {rounds} questions and you got {points} of them right! These are the questions I asked, with the results you gave me and the correct ones:")
        for key, value in questions_asked.items():
            print(f"{key}: Your answer: {answers[key]}, Correct answer: {value}")
        choice = input("\n\nDo you want to play again? Type yes or no. ").lower()
        while True:
            if choice == "yes": continue
            elif choice == "no": exit()
            else: choice = input("Invalid selection. Type yes or no. ").lower()