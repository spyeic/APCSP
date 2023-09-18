# Move turtles horizontally and vertically across screen.
# Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "circle", "square", "triangle", "classic"]
collide_shape = "turtle"
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    # create horizontal turtle
    ht = trtl.Turtle(shape=s)
    # add horizontal turtle to horiz_turtles list
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    # change color of horizontal turtle
    ht.fillcolor(new_color)
    # set to initial location and heading
    ht.goto(-350, tloc)
    ht.setheading(0)
    # do the same for vertical turtle
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)
    # increase location for next turtle
    tloc += 50

for step in range(50):
    for ht in horiz_turtles:
        for vt in vert_turtles:
            ht.forward(10)
            vt.forward(10)
            x1 = ht.xcor()
            y1 = ht.ycor()
            x2 = vt.xcor()
            y2 = vt.ycor()
            if abs(x1 - x2) < 20 and abs(y1 - y2) < 20:
                horiz_turtles.remove(ht)
                vert_turtles.remove(vt)
                ht.shape(collide_shape)
                ht.fillcolor("black")
                vt.shape(collide_shape)
                vt.fillcolor("black")

wn = trtl.Screen()
wn.mainloop()
