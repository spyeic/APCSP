import turtle as trtl

spider_painter = trtl.Turtle()

# Create a spider body
spider_painter.pensize(40)
spider_painter.circle(20)

# Configure spider legs
legs = 8
leg_length = 70
angle = 360 / legs
print("angle=", angle)

# Draw legs
spider_painter.pensize(5)
current_leg = 0
while current_leg < legs:
    spider_painter.goto(0, 20)
    spider_painter.setheading(angle * current_leg)
    print("z*n=", angle * current_leg)
    spider_painter.forward(leg_length)
    current_leg = current_leg + 1
spider_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
