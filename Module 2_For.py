numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in range(1, len(numbers)):
    i = numbers.pop(n)
    for d in range(1, i):
        if i % d == 0 and d != 1:
            not_primes.append(i)
            break
    if i % d != 0 or d == 1:
        primes.append(i)
    numbers.insert(n, i)
print('Primes:', primes)
print('Not primes:', not_primes)