# Hit the Target Game
# This is a beginner Python Turtle game.
# The goal is to aim the turtle at a target square and launch it.
# We will also add some hints when the shot misses.

import turtle

# Named constants
SCREEN_WIDTH = 600     # width of the game window
SCREEN_HEIGHT = 600    # height of the game window
TARGET_LLEFT_X = 100   # lower-left corner of the target, point A
TARGET_LLEFT_Y = 250   # lower-left corner of the target, point A
TARGET_WIDTH = 25      # size of the target square
FORCE_FACTOR = 60      # makes the projectile move a bigger distance
PROJECTILE_SPEED = 1   # animation speed for the turtle
NORTH = 90             # angle for going up
SOUTH = 270            # angle for going down
EAST = 0               # angle for going right
WEST = 180             # angle for going left

# We will use these values to check the target box corners.
# A = (TARGET_LLEFT_X, TARGET_LLEFT_Y)
# B = (TARGET_LLEFT_X + TARGET_WIDTH, TARGET_LLEFT_Y)
# C = (TARGET_LLEFT_X, TARGET_LLEFT_Y + TARGET_WIDTH)
# The target is a square, so B.xcor is the right edge and C.ycor is the top edge.
A_X = TARGET_LLEFT_X
A_Y = TARGET_LLEFT_Y
B_X = TARGET_LLEFT_X + TARGET_WIDTH
C_Y = TARGET_LLEFT_Y + TARGET_WIDTH

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target square.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle before launch.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Ask the user to choose the angle and the force.
angle = turtle.numinput("Input", "Enter the projectile's angle", minval=0, maxval=360)
force = turtle.numinput("Input", "Enter the launch force (1-10)", minval=1, maxval=10)

# Convert the force into distance.
distance = force * FORCE_FACTOR

# Aim the turtle in the chosen direction.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Check if the projectile hit the target square.
# The turtle must stay inside the target box.
# That means:
#   x must be between A_X and B_X
#   y must be between A_Y and C_Y
if (turtle.xcor() >= A_X and
    turtle.xcor() <= B_X and
    turtle.ycor() >= A_Y and
    turtle.ycor() <= C_Y):
    print('Target hit!')
else:
    print('You missed the target.')

    # This is the extra hint block for a beginner.
    # It compares the turtle's current position to the target corners.
    # If the turtle goes too far right, try a bigger angle.
    # If the turtle goes too far left, try a smaller angle.
    # If the turtle goes too high, use less force.
    # If the turtle goes too low, use more force.
    if turtle.xcor() > B_X:
        print('Try a greater angle.')
    if turtle.xcor() < A_X:
        print('Try a lesser angle.')
    if turtle.ycor() > C_Y:
        print('Try lesser force.')
    if turtle.ycor() < A_Y:
        print('Try more force.')

# Keep the window open until the user closes it.
turtle.done()