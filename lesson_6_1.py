class Human:
    head = True

    def __init__(self):
        self.about()

    def say_hello(self):
        print('Здравствуйте')


class Student(Human):
    head = False

    def about(self):
        print('Я студент')


class Teacher(Human):
    pass

student = Student() #Из родительского класса Human вызывается self.about()
# student.say_hello()
# student.about()

# teacher = Teacher()
# teacher.say_hello()