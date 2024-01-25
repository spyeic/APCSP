import turtle as trtl
import random as rand

walls = 32
forward_length = 50
path_width = 30
init_pos = 0 - forward_length, forward_length
pen = trtl.Turtle()
pen.setheading(90)
pen.speed(0)


def draw_barrier(forward):
    pen.forward(forward)
    # make a wall
    x, y = pen.pos()
    heading = pen.heading()
    pen.left(90)
    pen.forward(path_width)
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()


def draw_door(forward):
    pen.forward(forward)
    # make a door in the wall
    pen.penup()
    pen.forward(path_width)
    pen.pendown()


for i in range(walls):
    forward_length += path_width / 2
    door_start = rand.randint(path_width, forward_length - path_width)
    if i <= 4:
        draw_door(door_start)
        pen.forward(forward_length - door_start)
        pen.left(90)
        continue

    if door_start > forward_length / 2:
        wall_start = rand.randint(path_width, door_start)
        draw_barrier(wall_start)
        draw_door(door_start - wall_start)
        pen.forward(forward_length - door_start)
    else:
        wall_start = rand.randint(door_start, forward_length - path_width)
        draw_door(door_start)
        draw_barrier(wall_start - door_start)
        pen.forward(forward_length - wall_start)

    pen.left(90)

maze_runner = trtl.Turtle(shape="turtle")
maze_runner.color("green")
maze_runner.hideturtle()
maze_runner.penup()
maze_runner.goto(init_pos)
maze_runner.pendown()
maze_runner.showturtle()
amount = 10


def on_up():
    maze_runner.setheading(90)


def on_down():
    maze_runner.setheading(270)


def on_left():
    maze_runner.setheading(180)


def on_right():
    maze_runner.setheading(0)


def move_runner():
    maze_runner.forward(amount)


wn = trtl.Screen()
wn.onkeypress(on_up, "Up")
wn.onkeypress(on_down, "Down")
wn.onkeypress(on_left, "Left")
wn.onkeypress(on_right, "Right")
wn.onkeypress(move_runner, "g")
wn.listen()
wn.mainloop()
