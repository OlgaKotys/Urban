def all_variants(text):
    n = len(text)
    for size in range(1, n + 1):
        for start in range(n - size + 1):
            yield text[start:start + size]

a = all_variants('abcd')
for i in a:
    print(i)