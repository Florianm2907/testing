'''12. Prime Number Checker

Ask the user for a number.

Tell them if it’s prime or not.

Extend it: print all prime numbers up to that number.'''


def check_prime(number):
    for i in range(2, number - 1):
        if (number % i) == 0:
            return False
    return True

def enumerate_primes(until):
    primes = []
    for i in range(2, until):
        if check_prime(i): primes.append(i)
    return(primes)
    
while True:
    number = input("Enter a number to check whether it is a prime number. I will tell you if it is and\nI will also list all prime numbers before that number. Type 'exit' to exit. ")
    while True:
        try: number = int(number); break
        except:
            if number.lower() == "exit": exit()
            else: number = input("Please enter a whole number or type 'exit' to exit. ")
    print(f"\n{number} is a prime number.\n") if check_prime(number) else print(f"\n{number} is not a prime number.\n") 
    print(f"Prime numbers until {number}: {str(enumerate_primes(number))[1:-1]}\n")