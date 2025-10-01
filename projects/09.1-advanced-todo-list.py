'''9. Basic To-Do List (text only)
	•	Let the user add, remove, and view tasks in a list.
	•	Keep looping until they type quit.'''

todo = []

print('Basic to-do list. Enter what you want to do or enter "list" to show the list. Enter "exit" to exit. Enter "clear" to clear the list.')
while True:
    cmd = input('Enter what you want to do (Actual to-do item or "list" to show the list. Enter "exit" to exit. Enter "clear" to clear the list.): ')
    if cmd.lower() == "list":
        print("\nCurrent to-do list:")
        with open("./todolist.txt", "r") as x:
            for line in x.read().split("\n"): print(line)
        x.close()
    elif cmd.lower() == "exit": exit()
    elif cmd.lower() == "clear": 
        with open("./todolist.txt", "w") as x: x.write("")
        print("Cleared the to-do list.")
    else: 
        todo.append(cmd)
        with open("./todolist.txt", "a") as x:
            x.write(f"{cmd}\n")
        x.close()
        print(f'Added "{cmd}" onto the to-do list.\n')