import turtle as trtl
import random as rand

walls = 32
forward_length = 30
path_width = 20
pen = trtl.Turtle()
pen.setheading(90)
pen.speed(0)


for i in range(walls):
    forward_length += path_width / 2
    door_start = rand.randint(path_width, forward_length - path_width)
    if i <= 4:
        pen.forward(door_start)
        # make a door in the wall
        pen.penup()
        pen.forward(path_width)
        pen.pendown()
        pen.forward(forward_length - door_start)
        pen.left(90)
        continue

    if door_start > forward_length / 2:
        wall_start = rand.randint(path_width, door_start)
        pen.forward(wall_start)
        # make a wall
        x, y = pen.pos()
        heading = pen.heading()
        pen.left(90)
        pen.forward(path_width)
        pen.penup()
        pen.goto(x, y)
        pen.setheading(heading)
        pen.pendown()
        pen.forward(door_start - wall_start)
        # make a door in the wall
        pen.penup()
        pen.forward(path_width)
        pen.pendown()
        pen.forward(forward_length - door_start)
    else:
        wall_start = rand.randint(door_start, forward_length - path_width)
        pen.forward(door_start)
        # make a door in the wall
        pen.penup()
        pen.forward(path_width)
        pen.pendown()
        pen.forward(wall_start - door_start)
        # make a wall
        x, y = pen.pos()
        heading = pen.heading()
        pen.left(90)
        pen.forward(path_width)
        pen.penup()
        pen.goto(x, y)
        pen.setheading(heading)
        pen.pendown()
        pen.forward(forward_length - wall_start)

    pen.left(90)


wn = trtl.Screen()
wn.mainloop()
