import turtle as trtl

walls = 20
forward_step = 20
path_width = 10
pen = trtl.Turtle()
pen.setheading(90)

for i in range(walls):
    pen.forward(forward_step)
    pen.left(90)
    forward_step += path_width

wn = trtl.Screen()
wn.mainloop()
