#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors
color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
height = trtl.window_height() / 2  # the maximum redius is half of the height
print(height)

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle = 100  # different angle
seg = int(360 / angle)

while painter.ycor() < height:
    if space % 10 == 0:
        painter.fillcolor(color1)
        painter.color(color1)
    elif space % 10 == 5:
        painter.fillcolor(color2)
        painter.color(color2)

    painter.right(angle)
    painter.forward(2 * space + 10)  # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space += 1

wn.mainloop()
