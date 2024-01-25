import turtle as trtl

walls = 20
forward_step = 80
path_width = 20
pen = trtl.Turtle()
pen.setheading(90)

for i in range(walls):
    pen.forward(10)
    # make a gap in the wall
    pen.penup()
    pen.forward(path_width)
    pen.pendown()
    pen.forward(path_width + 10)
    # make a wall
    if i >= 4:
        x, y = pen.pos()
        heading = pen.heading()
        pen.left(90)
        pen.forward(path_width)
        pen.penup()
        pen.goto(x, y)
        pen.setheading(heading)
        pen.pendown()
    # keep going
    pen.forward(forward_step - 20 - path_width * 2)
    pen.left(90)
    forward_step += path_width / 2

wn = trtl.Screen()
wn.mainloop()
