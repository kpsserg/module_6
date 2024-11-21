class Figure:
    sides_count = 0
    print(sides_count)
    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = True
        # print(self.__sides)

    def get_color(self):
        return self.__color

    def  set_color(self, new_color):
        self.__color = new_color

    def __is_valid_sides(self):
        pass

    def get_sides(self):
        return self.__sides

    def __len__(self):
        pass

    def set_sides(self, *new_sides):
        pass

class Circle(Figure):
    sides_count = 1
    print(sides_count)

circle = Circle((200,200,200),2)
print(isinstance(circle, Circle))

# print(figure._Figure__color)
# figure.set_color((100,100,100))
# print(dir(figure))
# print(figure._Figure__color)

