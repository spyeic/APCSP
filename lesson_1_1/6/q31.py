import turtle as trtl

spider_painter = trtl.Turtle()

# Create a spider body
spider_painter.pensize(40)
spider_painter.circle(20)

# Configure spider legs
legs = 8
leg_length = 70
angle = 100 / legs
print("angle=", angle)

# Draw legs
spider_painter.pensize(5)
current_leg = 0
while current_leg < legs:
    spider_painter.goto(0, 20)
    angle_should_reduce = (legs / 2 - 1) * angle
    if current_leg % 2 == 0:
        spider_painter.setheading(current_leg * angle - angle_should_reduce)
    else:
        spider_painter.setheading(current_leg * angle + 180 - angle - angle_should_reduce)
    print("z*n=", angle * current_leg)
    spider_painter.forward(leg_length)
    current_leg = current_leg + 1

# Draw eyes
spider_painter.pencolor("red")
for i in range(2):
    spider_painter.penup()
    spider_painter.goto(10 * (-1) ** (i + 1), 40)
    spider_painter.pendown()
    spider_painter.dot(8)
    
spider_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
