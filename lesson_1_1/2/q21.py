import turtle as trtl

size = int(input("What size would you like the square to be? "))
# size = 100
painter = trtl.Turtle()
painter.pensize(3)

# front face
painter.fillcolor("blue")
painter.begin_fill()
painter.goto(0, size)
painter.goto(size, size)
painter.goto(size, 0)
painter.goto(0, 0)
painter.end_fill()

# right face
painter.fillcolor("red")
painter.penup()
painter.goto(size, size)
painter.pendown()
painter.begin_fill()
painter.goto(size * 1.3, size * 1.3)
painter.goto(size * 1.3, size * 0.3)
painter.goto(size, 0)
painter.goto(size, size)
painter.end_fill()

# up face
painter.fillcolor("yellow")
painter.penup()
painter.goto(0, size)
painter.pendown()
painter.begin_fill()
painter.goto(size * 0.3, size * 1.3)
painter.goto(size * 1.3, size * 1.3)
painter.goto(size, size)
painter.goto(0, size)
painter.end_fill()

# TODO
for i in range(1, 3):
    painter.penup()
    painter.goto(0, size / 3 * i)
    painter.pendown()
    painter.goto(size, size / 3 * i)
    painter.goto(size * 1.3, size * 1.3 / 3 * i)

wn = trtl.Screen()
wn.mainloop()

