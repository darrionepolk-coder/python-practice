from pet import Pet


class Bird(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.__species = species

    def __str__(self):
        return f"Bird - {super().__str__()}, Species: {self.__species}"
