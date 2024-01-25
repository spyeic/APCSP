#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    if floor % 21 == 0:
        x = x + 100
        y = -150
    painter.goto(x, y)
    if floor % 9 == 0:
        painter.color("blue")
    if floor % 9 == 3:
        painter.color("gray")
    if floor % 9 == 6:
        painter.color("red")

    y = y + 5  # location of next floor

    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()
