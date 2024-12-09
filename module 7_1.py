class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read().strip()
            return products
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products()
        existing_products_list = existing_products.split('\n')

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                product_name = product.name
                if not any(product_name in line for line in existing_products_list):
                    file.write(product_str + '\n')
                else:
                    print(f"Продукт {product_name} уже есть в магазине")

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Tomatoes', 3.2, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3, p4)
print(s1.get_products())