immutable_var = 1, 2, 3, "apple", True
print(immutable_var)
# immutable_var[3] = 458
# print(immutable_var)
# невозможно изменить неизменяемый объект кортежа, можно изменить только элементы списка внутри кортежа

mutable_list = [4, 5, 6, "banana", False]
print(mutable_list)
mutable_list[3] = 7
mutable_list[4] = 8
print(mutable_list)