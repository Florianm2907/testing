'''9. Basic To-Do List (text only)
	•	Let the user add, remove, and view tasks in a list.
	•	Keep looping until they type quit.
	•	(You don’t need to save to a file yet — just use variables).'''

todo = []

print('Basic to-do list. Enter what you want to do or enter "list" to show the list. Enter "exit" to exit and discard the list.')
while True:
    cmd = input('Enter what you want to do (Actual to-do item or "list" to show the list. Enter "exit" to exit and discard the list.): ')
    if cmd.lower() == "list":
        print("\nCurrent to-do list:")
        for item in todo:
            print(f"Item {todo.index(item) + 1}: {item}")
        print("\n")
    elif cmd.lower() == "exit": exit()
    else: 
        todo.append(cmd)
        print(f'Added "{cmd}" onto the to-do list.\n')