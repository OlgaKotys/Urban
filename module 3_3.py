def print_params(a=1, b='строка', c=True):
    print(f"a: {a}, b: {b}, c: {c}")


print_params()
print_params(10)
print_params(20, 50)
print_params(13, 22, False)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [33, "я_строка", False]
values_dict = {'a': 11, 'b': "Привет", 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [44.55, "ДРУГОЕ"]
print_params(*values_list_2, 454)
