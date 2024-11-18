def get_multiplied_digits(number):
    str_number = str(number).rstrip('0')

    if len(str_number) > 1:
        first = int(str_number[0])
        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        else:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number[0])

result = get_multiplied_digits(44000)
print(result)