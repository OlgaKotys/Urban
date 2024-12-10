def generate_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i+1, 21):
            if (i + j) > n and n % (i + j) == 0:
                pairs.append((i, j))
    if not pairs:
        for i in range(1, n):
            for j in range(i+1, 21):
                if n % (i + j) == 0:
                    pairs.append((i, j))
    password = ''.join(f"{pair[0]}{pair[1]}" for pair in pairs)
    return password

n = 7
password = generate_password(n)
print(f"Password for {n}: {password}")
