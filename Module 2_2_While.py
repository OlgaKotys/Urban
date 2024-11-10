my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n_el = 0   #номер элемента

while n_el < len(my_list):
    if my_list[n_el] > 0:
        print(my_list[n_el])
        n_el += 1
    elif my_list[n_el] < 0:
        break
    else:
        n_el += 1
        continue