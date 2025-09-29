import random
import string

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate a random password of the specified length
password = ""
for i in range(password_length):
  password += random.choice(string.ascii_letters + string.digits + string.punctuation)

# Print the generated password
print(password)
