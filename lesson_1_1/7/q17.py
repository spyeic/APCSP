# Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic",
                 "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold",
                 "red", "blue", "green", "orange", "purple", "gold"]

# create 6 turtles
for shape in turtle_shapes:
    turtle = trtl.Turtle(shape=shape)
    turtle.penup()
    turtle.color(turtle_colors.pop())
    my_turtles.append(turtle)
    

# set starting point
startx = 0
starty = 0
heading = 90
length = 50

# move turtles to starting point, move them forward
for turtle in my_turtles:
    turtle.goto(startx, starty)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(length)

    # change starting point for next turtle
    startx = turtle.xcor()
    starty = turtle.ycor()
    # change heading for next turtle
    heading = turtle.heading() * 1.02
    # change length for next turtle
    length = length + 5

wn = trtl.Screen()
wn.mainloop()
