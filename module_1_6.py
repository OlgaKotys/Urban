my_dict = {"Яблок" : 258, "Бананов" : 426, "Капусты" : 37}
print(my_dict)
print(my_dict["Бананов"])
my_dict["Кукурузы"] = 45
my_dict.update({"Черешни" : 337,
                "Картошки" : 585})
del my_dict["Капусты"]
print(my_dict.get("Капусты", "Такого продукта нет"))
print(my_dict)

my_set = {458, 326, 334, 'string', 458, 334, True, 326, 458, 'string'}
print(my_set)
my_set = set(my_set)
my_set.add(300), my_set.add(False)
my_set.discard('string')
print(my_set)