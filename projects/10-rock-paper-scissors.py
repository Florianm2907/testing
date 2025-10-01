'''10. Rock, Paper, Scissors
	•	Ask user to pick rock/paper/scissors.
	•	Computer randomly picks one.
	•	Compare and announce winner.
	•	Play multiple rounds until the user quits.'''

import random

score = 0
my_score = 0
streak = 0
max_streak = 0
won_last_round = False
choices = ["rock", "paper", "scissors"]

def win():
    global score
    global streak
    global max_streak
    global won_last_round
    score += 1
    if won_last_round: streak +=1
    if streak >= max_streak: max_streak = streak
    print(f"You win! Your points: {score}, my points: {my_score}")

def lose():
    global my_score
    global streak
    global won_last_round
    my_score +=1
    streak = 0
    won_last_round = False
    print(f"I win! Your points: {score}, my points: {my_score}")

def draw():
    print("It's a draw! We both don't get any points!")

print("Let's play rock paper scissors! You can type 'rock', 'paper' or 'scissors' and I will respond with a random choice! I won't cheat, I promise!")

while True:
    choice = input("Rock, Paper, Scissors! (input your choice): ").lower()
    while True:
        if choice in choices: break
        else: 
            if choice == "exit": print(f"\nFinal score: Your points: {score}, my points: {my_score}, your maximum streak: {max_streak}"); exit()
            choice = input("Invalid choice! Choose from rock, paper or scissors! You can also type 'exit' to exit. ").lower()
    my_choice = choices[random.randint(0,2)]
    print(f"I choose {my_choice}!")
    if choice == "rock" and my_choice == "paper": lose()
    elif choice == "rock" and my_choice == "scissors": win()
    elif choice == "rock" and my_choice == "rock": draw()
    elif choice == "scissors" and my_choice == "paper": win()
    elif choice == "scissors" and my_choice == "scissors": draw()
    elif choice == "scissors" and my_choice == "rock": lose()
    elif choice == "paper" and my_choice == "paper": draw()
    elif choice == "paper" and my_choice == "scissors": lose()
    elif choice == "paper" and my_choice == "rock": win()