from pet import Pet


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def __str__(self):
        return f"Cat - {super().__str__()}, Color: {self.__color}"
