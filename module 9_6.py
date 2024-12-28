def all_variants(text):
    lenght = len(text)
    for i in range(lenght):
        for j in range(i + 1, lenght + 1):
            yield text[i:j]

a = all_variants('abcd')
for i in a:
    print(i)