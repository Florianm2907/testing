import random
import string
chars = []
for string in string.ascii_letters:
	chars.append(string)
i = 0
while i < 10:
	chars.append(i)
	i+=1
symbols = [",", ".", "*", ":", ";", "!", "?", "_", "-", "+", "(", ")", "/"]
for symbol in symbols:
	chars.append(symbol)
x = 0
pwd = ""
while x < 20:
	pwd = pwd + str(chars[random.randint(0, len(chars)-1)])
	x+=1
# print(chars)
print(pwd)