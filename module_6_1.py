class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    """Метод для классов Mammal и Predator"""
    def eat(self, food):
       if food.edible:
           print(self.name, 'съел ', food.name)
           self.fed = True
       else:
           print(self.name, 'не стал есть ', food.name)
           self.alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(a1.alive)
print((a1.fed))

print(a2.name)
print(a2.alive)
print((a2.fed))

print(p1.name, p1.edible)
print(p2.name, p2.edible)

a1.eat(p1)
a2.eat(p2)

print(f"Сытость {a1.name} равняется {a1.fed}. Его жизнь {a1.alive}")
print(f"Сытость {a2.name} равняется {a2.fed}. Его жизнь {a2.alive}")
