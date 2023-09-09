import turtle as trtl

spider_painter = trtl.Turtle()

# Create a spider body
spider_painter.pensize(40)
spider_painter.circle(20)

# Configure spider legs
legs = 8
leg_length = 100
angle = 80 / legs
print("angle=", angle)

# Draw legs
spider_painter.pensize(5)
current_leg = 0
curve_angle = 80

while current_leg < legs:
    spider_painter.penup()
    spider_painter.goto(0, 20)
    spider_painter.pendown()
    if current_leg % 2 == 0:
        spider_painter.setheading(current_leg * angle + 130)
        spider_painter.circle(leg_length, curve_angle)
    else:
        spider_painter.setheading(-(current_leg * angle + 130))
        spider_painter.circle(leg_length, -curve_angle)
        leg_length = leg_length - 10
        curve_angle = curve_angle + 15

    current_leg = current_leg + 1

# Draw head
spider_painter.penup()
spider_painter.goto(0, -30)
spider_painter.pendown()
spider_painter.pensize(30)
spider_painter.circle(5)

# Draw eyes
eyex = -8
for i in range(2):
    spider_painter.pencolor("red")
    spider_painter.penup()
    spider_painter.goto(eyex, -35)
    spider_painter.pendown()
    spider_painter.dot(8)
    eyex += 4
eyex = -8
for i in range(2):
    spider_painter.color("black")
    spider_painter.penup()
    spider_painter.goto(eyex, -35)
    spider_painter.pendown()
    spider_painter.dot(3)
    eyex += 4
    
spider_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
