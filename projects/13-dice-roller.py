'''13. Dice Roller

Simulate rolling one or two dice.

Print the result each time.

Extend it: let the user choose how many dice to roll.'''

import random

prev_dice = 1
results = []

def roll(dice):
    result = 0
    global results
    results = []
    for i in range(dice):
        temp = random.randint(1,6)
        result += temp
        results.append(temp)
    return result, results

while True:
    dice = input("Tell me how many dice to roll or type 'exit' to exit! If you just press enter, I'll start rolling\none dice or I will roll however many dice you told me to roll before! ")
    if dice:
        if dice.lower() == "exit": exit()
        while True:
            try: 
                dice = int(dice)
                prev_dice = dice
                break
            except:
                dice = input("Please enter a whole number or type 'exit' to exit. ")
    else: dice = prev_dice
    result, results = roll(dice)
    print(f"Your {dice} dice rolled a total of {result}! Here are they: {str(results)[1:-1]}\n")