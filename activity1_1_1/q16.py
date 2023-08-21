import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(2)
painter.pensize(3)

# draw three lines
def draw_line(start):
  painter.goto(0, start)
  painter.pendown()
  painter.forward(100)
  painter.penup()
  
draw_line(0)
draw_line(-10)
draw_line(-20)

# draw a square
painter.goto(0, -100)
painter.pendown()
for i in range(4):
    painter.forward(100)
    painter.right(90)

painter.penup()

# draw a triangle
painter.goto(0, 10)
painter.pendown()
painter.left(90)
for i in range(3):
    painter.forward(100)
    painter.right(120)
painter.penup()

# draw a circle
painter.goto(0, 200)
painter.pendown()
painter.circle(50)

wn = trtl.Screen()
wn.mainloop()