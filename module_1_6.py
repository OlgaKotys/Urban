my_dict = {"Яблок" : 258, "Бананов" : 426, "Капусты" : 37}
print(my_dict)
print(my_dict["Бананов"])
print(my_dict.get("Кукурузы"))
my_dict.update({"Черешни" : 337,
                "Картошки" : 585})
print(my_dict)

my_set = {458, 326, 334, 'string', 458, 334, True, 326, 458, 'string'}
print(my_set)
my_set.add(300), my_set.add(False)
my_set.discard('string')
print(my_set)