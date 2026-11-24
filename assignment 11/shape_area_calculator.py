from circle import Circle
from rectangle import Rectangle


def main():
    shapes = [
        Circle("circle1", 3),
        Circle("circle2", 5),
        Rectangle("rect1", 4, 5),
        Rectangle("rect2", 6, 2)
    ]

    print("Areas of various shapes:")
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.get_area():.2f}")


if __name__ == "__main__":
    main()
