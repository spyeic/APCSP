import turtle as trtl
import random

painter = trtl.Turtle()

painter.turtlesize(2)

def goto(x, y):
  painter.penup()
  painter.goto(x, y)
  painter.pendown()

def get_random(n1, n2):
    return random.randint(min(n1, n2), max(n1, n2))

painter.pensize(3)
goto(0, 200)

painter.goto(-30, 160)
painter.goto(30, 160)
painter.goto(0, 200)

goto(0, 160)
painter.goto(-60, 120)
painter.goto(60, 120)
painter.goto(0, 160)

goto(0, 120)
painter.goto(-90, 60)
painter.goto(90, 60)
painter.goto(0, 120)

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

