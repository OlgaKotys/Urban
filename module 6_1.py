class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(f"{self.name} съел {food.name}")
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name}")
        else:
            print(f"{food} не является растением")

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Трицератопс')
a2 = Mammal('Оленёнок')
p1 = Flower('Одуванчик')
p2 = Fruit('Бананы')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
