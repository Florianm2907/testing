#number guessing game
'''Computer picks a random number (say 1-100).
Player tries to guess it.
After each guess, tell them if it's too high, too Iow,
Count how many guesses it took.'''

import random

print("Number Guessing Game\nI've chosen a number between 0 and 100 (inclusive) - try to guess my number and I'll tell you if you're too high or low!\n"); rand_number = random.randint(0, 100); game_count = 0; guess_count = 0; new_game = True
while True:
    user_choice = input("Enter guess: ")
    while True:
        try : user_choice = int(user_choice); break
        except : user_choice = input("\nYou did not enter a number, try again: ")
    guess_count += 1
    if user_choice == rand_number:
        game_count += 1
        print(f"Congrats, you guessed the number!\nThe number was {rand_number}!\nIt took you {guess_count} guesses to get it right!\nYou've played {game_count} games so far.\n")
        while True:
            new_game_query = input("Would you like to play again? (Y/N): ")
            if new_game_query.upper() == "Y": new_game = True; rand_number = random.randint(0, 100); guess_count = 0; print(""); break
            elif new_game_query.upper() == "N": exit()
            else: print("Invalid choice!")
    elif user_choice < rand_number: print("Your guess is too low!\n")
    else: print("Your guess is too high!\n")