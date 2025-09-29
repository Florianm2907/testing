import hashlib

prefix = "hacktheweb"
n=0

while True:
    input_string = prefix + str(n)
    hash_value = hashlib.md5(input_string.encode()).hexdigest()

    if hash_value[:6] == "000000":
        print(f"Found a hash with six leading zeroes: {hash_value}")
        print(n)
        break

    n += 1
