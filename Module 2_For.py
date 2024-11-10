numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in numbers:
    for d in range(1, n+1):
        if n % d == 0 and d != 1 and n != 1 and n != d:
            not_primes.append(n)
            break
    if n % d != 0 or n == d and n != 1:
        primes.append(n)
print('Primes:', primes)
print('Not primes:', not_primes)