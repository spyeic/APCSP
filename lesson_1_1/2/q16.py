# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

painter.pensize(5)
# add code here for a circle
painter.circle(50)

# move the turtle to another part of the screen
painter.penup()
painter.goto(100, 100)
painter.pendown()

# add code here for an arc
painter.circle(50, 90)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-100, 100)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(50, 180, 5)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-100, -100)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(50, 360, 6)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()


