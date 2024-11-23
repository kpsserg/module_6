class Circle():
    sides_count = 1

    def __init__(self, color, *args):
        #Рабочее решение
        print(args, str(args), len(args))
        print(list(args), len(list(args)), "\n")

        ### Код ниже не работает при одном параметре в *args
        # print(*args, len(list(*args)))
        # print(*args, len(*args))

        #### Код ниже не работает при 2 и более параметрах в *args
        # print(args, list(args))
        # print(*args, str(*args))

circle = Circle((0, 0, 0), 5, 4)
circle = Circle((0, 0, 0), 3)

