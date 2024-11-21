class Human:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Привет, меня зовут {self.name}\n")

class Student(Human):
    def __init__(self, name, place):
        super().__init__(name)
        self.place = place
        super().info()

human = Human('Сергей')
print(human.name)
human.info()

student = Student('Serg', 'Urban')
print(student.name, student.place)