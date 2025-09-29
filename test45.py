out = [0] * (4294967296 + 1)
prime_sum = 2
for i in range(3, 4294967296 + 1, 2):
    if out[i] == 0:
        prime_sum += i
        for j in range(i * i, 4294967296 + 1, 2 * i):
            out[j] = 1
print(prime_sum)