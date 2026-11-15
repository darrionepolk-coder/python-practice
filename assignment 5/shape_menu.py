# This program uses Python's turtle module to draw shapes.
# The user picks a shape from a menu, enters the location and size,
# and then the turtle draws that shape in a chosen color.

import turtle

# These constants are the menu choices.
SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


# This is the main function that controls the whole program.
# It shows the menu over and over until the user decides to quit.
def main():
    while True:
        # Show the menu every time the loop repeats.
        display_menu()
        choice = input("Enter your choice: ").strip()

        # If the user picks square, ask for the starting point, size, and color.
        if choice == SQUARE:
            x = int(input("Enter starting x coordinate: "))
            y = int(input("Enter starting y coordinate: "))
            side = int(input("Enter side length: "))
            color = input("Enter fill color: ")
            square(x, y, side, color)

        # If the user picks circle, ask for the circle center, radius, and color.
        elif choice == CIRCLE:
            x = int(input("Enter starting x coordinate: "))
            y = int(input("Enter starting y coordinate: "))
            radius = int(input("Enter radius: "))
            color = input("Enter fill color: ")
            circle(x, y, radius, color)

        # If the user picks triangle, ask for the starting point, side length, and color.
        elif choice == TRIANGLE:
            x = int(input("Enter starting x coordinate: "))
            y = int(input("Enter starting y coordinate: "))
            side = int(input("Enter side length: "))
            color = input("Enter fill color: ")
            equilateral_triangle(x, y, side, color)

        # If the user chooses 4, the loop ends.
        elif choice == QUIT:
            print("Goodbye!")
            break

        # If the user types anything else, show an error message.
        else:
            print("Invalid choice. Please try again.")

    # This keeps the turtle window open until the user closes it.
    turtle.done()


# This function prints the menu options.
def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


# This function draws a filled square.
# It moves the turtle to the starting point, fills the shape, and draws 4 sides.
def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()


# This function draws a filled equilateral triangle.
# It uses a loop that runs 3 times and turns the turtle 120 degrees each time.
def equilateral_triangle(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()


# This function draws a filled circle.
# The turtle moves to the chosen start point, then uses the circle() method.
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# This is the usual Python entry point.
# It makes sure main() runs only when this file is executed directly.
if __name__ == "__main__":
    main()
