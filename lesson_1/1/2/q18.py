# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.pensize(3)

# set the pen and fill colors
# then draw a circle
painter.fillcolor("red")
painter.pencolor("blue")
painter.begin_fill()
painter.circle(50)
painter.end_fill()
painter.goto(100, 100)

# move the turtle to another part of the screen
painter.penup()
painter.goto(100, 100)
painter.pendown()

# change both the pen and fill colors
# then draw a polygon of your choice
painter.fillcolor("blue")
painter.pencolor("red")
painter.begin_fill()
painter.circle(50, 360, 6)
painter.end_fill()


# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
