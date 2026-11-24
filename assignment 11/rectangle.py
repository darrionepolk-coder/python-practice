from shape import Shape


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def __str__(self):
        return (f"{super().__str__()} "
                f"(length: {self.__length}, width: {self.__width})")
