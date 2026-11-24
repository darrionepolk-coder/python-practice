from pet import Pet


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed

    def __str__(self):
        return f"Dog - {super().__str__()}, Breed: {self.__breed}"
