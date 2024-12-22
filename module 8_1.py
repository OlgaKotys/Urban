class UnsupportedTypeError(Exception):
    pass

def add_everything_up(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("Неподдерживаемый тип данных.")
        return a + b
    except TypeError:
        return str(a) + str(b)
    except UnsupportedTypeError as e:
        return str(e)

# Примеры использования:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up([1, 2, 3], 'string,123'))
