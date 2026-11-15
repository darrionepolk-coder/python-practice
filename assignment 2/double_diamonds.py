# Import the Turtle graphics module
import turtle


# Function to draw a filled diamond using a square rotated by 45 degrees
def draw_diamond(pen, size, x, y):
    pen.penup()          # Lift the pen before moving to the start position
    pen.goto(x, y)      # Move to the given position
    pen.pendown()       # Put the pen down to draw
    pen.setheading(45)  # Rotate the square so it becomes a diamond
    pen.fillcolor("blue")
    pen.begin_fill()    # Start filling the shape with blue
    for _ in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()      # Finish the filled diamond


# Create the drawing screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle pen and set drawing properties
pen = turtle.Turtle()
pen.speed(1)
pen.color("blue")

# Draw the first diamond on the left side
draw_diamond(pen, 100, -100, 0)

# Draw the second diamond on the right side
draw_diamond(pen, 100, 100, 0)

# Hide the turtle pointer and keep the window open until clicked
pen.hideturtle()
screen.exitonclick()
