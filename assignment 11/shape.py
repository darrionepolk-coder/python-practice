class Shape:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_area(self):
        return 0.0

    def __str__(self):
        return self.__name
