my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(my_list)
n = 0

while n < a:
    if my_list[n] > 0:
        print(my_list[n])
        n += 1
    elif my_list[n] < 0:
        break
    else:
        n += 1
        continue