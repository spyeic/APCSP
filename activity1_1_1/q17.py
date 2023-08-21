import turtle as trtl
import random

painter = trtl.Turtle()
painter.turtlesize(2)
painter.pensize(3)

def goto(x, y):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

def get_random(n1, n2):
    return random.randint(min(n1, n2), max(n1, n2))

def draw_isosceles_triangle(x, y, width, height):
    goto(x, y)
    painter.goto(x + width / 2, y - height)
    painter.goto(x - width / 2, y - height)
    painter.goto(x, y)
    

draw_isosceles_triangle(0, 200, 60, 40)
draw_isosceles_triangle(0, 160, 120, 40)
draw_isosceles_triangle(0, 120, 180, 60)

goto(-10, 60)
painter.goto(-10, 0)
painter.goto(10, 0)
painter.goto(10, 60)


# draw 10 roots
for i in range(10):
    goto(-10 + i * 2, 0)
    for j in range(20):
        painter.setheading(get_random(180 + i * 18, 270))
        painter.forward(get_random(2, 4))


wn = trtl.Screen()
wn.mainloop()

