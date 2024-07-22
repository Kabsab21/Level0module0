import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
my_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
my_turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
my_turtle.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
my_turtle.color('green')
my_turtle.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
my_turtle.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
my_turtle.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
my_turtle.color('blue')
my_turtle.begin_fill()
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.end_fill()
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
my_turtle.goto(0, 0)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
my_turtle.color('green')
my_turtle.begin_fill()
my_turtle.circle(20, 1090)
my_turtle.end_fill()
my_turtle.goto(10, 0)
my_turtle.penup()
my_turtle.forward(300)
my_turtle.pendown()
my_turtle.color('red')
my_turtle.begin_fill()
for i in range(9):
    my_turtle.left(45)
    my_turtle.forward(70)
my_turtle.end_fill()
my_turtle.hideturtle()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
