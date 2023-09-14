#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# create 6 turtles
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.penup()
    t.color(turtle_colors.pop())
    my_turtles.append(t)
    

# set starting point
startx = 0
starty = 0
heading = 90

# move turtles to starting point, move them forward
for t in my_turtles:
    t.goto(startx, starty)
    t.setheading(heading)
    t.pendown()
    t.right(45)
    t.forward(50)

    # change starting point for next turtle
    startx = t.xcor()
    starty = t.ycor()
    # change heading for next turtle
    heading = t.heading()

wn = trtl.Screen()
wn.mainloop()
