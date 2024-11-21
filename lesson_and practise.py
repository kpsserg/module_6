class Human:
    __arms = True

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    __arms = False


human = Human()
student = Student()

human.about()
student.about()

print(dir(human))
print(dir(student))
print(student._Human__arms)
print(student._Student__arms)
