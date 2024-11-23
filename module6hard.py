from math import prod

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        # НЕ НРАВИТСЯ ЭТО УСЛОВИЕ ИЗ-ЗА str().
        # len(list(*sides)) > 1: не работает, если 1 элемент в *sides
        if len(str(*sides)) > 1:
            self.__sides = list(*sides)
        else:
            self.__sides = list(sides)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, new_color):
        rgb = len(new_color)
        if rgb != 3:
            print(f"Вы указали цвет не в режиме RGB! Возможно указали в режиме CMYK")
            print(f"Укажите цвет в виде трех чисел в диапазоне от 0 до 255")
            print(f"Цвет остался прежний")
            return False
        else:
            for i in range(rgb):
                # all = 0
                if 0 <= new_color[i] <= 255:
                    continue
                else:
                    print(f"Вы указали цвет RGB вне диапазона 0-255")
                    return False
            print("Цвет изменен успешно!")
            return True

    def set_color(self, *new_color):
        if self.__is_valid_color(new_color):
            self.__color = new_color

    def __is_valid_sides(self, sides_count, *new_sides):
        new_sides = list(new_sides)
        len_param = len(new_sides)
        for i in range(len_param):
            if isinstance(new_sides[i], int) and new_sides[i] > 0:
                continue
            else:
                print(f"Размер должен быть положительным десятичным числом!")
                return False

        if sides_count == len(list(new_sides)):
            # print("Count of sides is True")
            return True
        else:
            print(f"ЗАДАНО НЕПРАВИЛЬНОЕ КОЛ-ВО СТОРОН. Их должно быть: {sides_count}")
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        # if len(self.__sides) == 1 or len(self.__sides) == 12:
        return sum(self.__sides)

    """Изменяем размеры сторон"""
    def set_sides(self, *new_sides):
        # если у объекта 12 сторон, а новая длина стороны задана одним параметром, значит имеем делок с кубом
        if self.sides_count == 12 and len(new_sides) == 1:
            new_sides *= 12
        if self.sides_count == len(new_sides):
            if self._Figure__is_valid_sides(self.sides_count, *new_sides):
                if self.sides_count > 1:
                    self.__sides.clear()
                    self.__sides = list(new_sides)
                else:
                    self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if not super()._Figure__is_valid_sides(self.sides_count, *sides):
            sides = 1
            print(f"Длина окружности задается по умолчанию {sides}")

        super().__init__(color, sides)

    def get_square(self):
        radius = self._Figure__sides[0] / (2 * 3.1415)
        return 3.14 * radius ** 2


class Cube(Figure):
    sides_count = 12
    args_count = 1

    def __init__(self, color, *sides):
        if not super()._Figure__is_valid_sides(self.args_count, *sides):
            sides = []
            for i in range(self.sides_count):
                sides.append(1)
            print(f"Размер всех ребер куба задан по умолчанию (1)")
        else:
            sides *= self.sides_count
        super().__init__(color, sides)

    def get_volume(self):
        return self._Figure__sides[0]**3


class Triangle(Figure):
    sides_count = 3
    args_count = 3

    def __init__(self, color, *sides):
        if not super()._Figure__is_valid_sides(self.args_count, *sides):
            sides = []
            for i in range(self.sides_count):
                sides.append(1)
            print(f"Размер всех сторон треугольника задан по умолчанию (1)")
        super().__init__(color, sides)

    """площадь треугольника"""
    def get_square(self):
        p = sum(self.get_sides()) / 2
        diff_of_nums = []
        for i in range(len(self.get_sides())):
            diff_of_nums.append(p - self._Figure__sides[i])
        if 0 in diff_of_nums:
            print("По формуле Герна площадь треугольника с заданными сторонами не рассчитать!")
            return 0
        # print(p, diff_of_nums, prod(diff_of_nums))
        s = (p * prod(diff_of_nums)) ** 0.5
        print("Площадь треугольника по формуле Герона равна: ", s)

###Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


### Мои проверки
print('\n\nКРУГ')
circle = Circle((200, 200, 200), 5)
print(f"Цвет круга: {circle.get_color()}\n")

print(f"Зададим новый цвет: (10, 100, 117)")
circle.set_color(10, 100, 117)
print(f"Проверяем цвет: {circle.get_color()}\n")

print(f"Зададим неправильный цвет: (-10, 100, 117)")
circle.set_color(-10, 100, 117)
print(f"Проверяем цвет: {circle.get_color()}\n")

print(f"Зададим неправильный цвет: (-10, 100, 117, 255)")
circle.set_color(-10, 100, 117, 255)
print(f"Проверяем цвет: {circle.get_color()}\n")

print("Длина окружности: ", len(circle))

print(f"Зададим новую дину окружности: 10")
circle.set_sides(10)
print(f"Проверяем новыую длину круга: {circle.get_sides()}, {len(circle)}\n")

print(f"Зададим новую дину окружности: '15'")
circle.set_sides("15")
print(f"Проверяем новыую длину круга: {circle.get_sides()}, {len(circle)}\n")

print(f"Зададим новую дину окружности: -15")
circle.set_sides(-15)
print(f"Проверяем новыую длину круга: {circle.get_sides()}, {len(circle)}\n")

print("Площадь круга:", circle.get_square())
print(f"периметр круга равен длине окружности {len(circle)}")
print("\n")

print('КУБ')
cube = Cube((200, 200, 200), 2)
print(f"Цвет куба {cube.get_color()}")
print("Изменим цвет куба на (10, 100, 117)")
cube.set_color(10, 100, 117)
print(f"Цвет куба {cube.get_color()}")
print(f"Длина каждого ребра куба составляет: {set(cube._Figure__sides)}")
print("Посмотрим на стороны куба:", cube.get_sides())
print("Периметр куба:", len(cube))
print("Площадь куба:", len(cube))
print("Объем куба:", cube.get_volume())
print("Зададим новую сторону кубу: 5")
cube.set_sides(5)
print("Посмотрим на сторону куба", cube.get_sides())

print("\n")

print(f"{"Треугольник".upper()}")
triangle = Triangle((200, 200, 200), 4, 2, 3)
triangle.set_color((10, 100, 117))
print("Посмотрим на стороны треугольника:", triangle.get_sides())

print("Зададим новые стороны треугольнику: 2, 3, 4")
triangle.set_sides(2, 3, 4)
print("Посмотрим на стороны треугольника:", triangle.get_sides())

print("\nЗададим неправильные стороны треугольнику: 2, 3")
triangle.set_sides(2, 3)
print("Посмотрим на стороны треугольника:", triangle.get_sides())

print("Периметр треугольника:", len(triangle))
triangle.get_square()