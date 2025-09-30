'''4. Password Strength Checker
	•	Ask user for a password.
	•	Check if it’s “weak” (short, only letters), “medium” (letters + numbers), or “strong” (letters, numbers, special characters, and > 8 characters).
	•	Print the result.'''

from getpass import getpass
import string

password_strength = 0
password_contains = {}
types = ["upper", "lower", "number", "special"]
types_used = 0
password = getpass("Enter a password to check it's strength: ")

def count_occurrences(password, type):
	count = 0
	if type == "lower":
		for char in password:
			if char in string.ascii_lowercase: count +=1
		return count
	if type == "upper":
		for char in password:
			if char in string.ascii_uppercase: count +=1
		return count
	if type == "number":
		for char in password:
			if char.isdigit(): count +=1
		return count
	if type == "special":
		for char in password:
			if not char.isalnum(): count +=1 
		return count

for type in types: password_contains[type] = count_occurrences(password, type)
for key, value in password_contains.items(): 
	if value: types_used += 1

score = len(password)
score *= types_used

print(f"Your password scored {score} points, {len(password)} points for the length itself and {score - len(password)} points for using {types_used} different types of characters!")