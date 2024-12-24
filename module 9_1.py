def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        try:
            results[function.__name__] = function(int_list)
        except Exception as e:
            results[function.__name__] = f"Ошибка: {e}"
    return results

# Примеры использования:
print(apply_all_func([6, 20, 15, 9, 5], max, min))
print(apply_all_func([6, 20, 15, 9, 5], len, sum, sorted))
