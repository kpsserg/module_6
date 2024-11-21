class Human:
    head = True
    _legs = True
    __arms = True

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    __arms = False
    _Human__arms = False

    def student_arms(self):
        self.__arms = True
        #return self.__arms

    # def about(self):
    #     print('Я студент')

human = Human()
student = Student()

human.about()
student.about()

print(dir(human))
print(dir(student))
print(student._Human__arms)
print(student._Student__arms)

student.student_arms()
print(student.student_arms())
print(dir(student.student_arms()))
print(student._Student__arms)
