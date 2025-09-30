'''7. Countdown Timer
	•	Ask user for a number (seconds).
	•	Print a countdown to 0.
	•	Print “Time’s up!” at the end.'''

import time as t

time = input("Input a time to count down to: ")
while True:
    try: time = int(time); break
    except: time = input("Enter a wholenumber or type exit to exit. ")
    if time.lower() == "exit": exit()

print(f"Counting down from {time}!")
for i in range(time, 0, -1):
    print(f"{i} seconds remaining.")
    t.sleep(1)
print("Time's up!")