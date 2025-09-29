# import hashlib

# prefix = "hacktheweb"
# n = 0

# while True:
#     input_string = prefix + str(n)
#     hash_value = hashlib.md5(input_string.encode()).hexdigest()

#     if hash_value[:6] == "000000":
#         print(f"Found a hash with six leading zeroes: {hash_value}")
#         print(n)
#         break

    # n += 1





def isPrime(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False 
    return True
number = 864186418888888888802470247
for i in range(number//2, 2, -1 ):
    if number % i == 0:
        if isPrime(i):
            print ("Largest prime factor = " , i)
            break

       