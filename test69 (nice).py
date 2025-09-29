from sympy import primefactors

number = 864186418888888888802470247
factors = primefactors(number)
largest_prime_factor = max(factors)

print("Largest prime factor =", largest_prime_factor)
