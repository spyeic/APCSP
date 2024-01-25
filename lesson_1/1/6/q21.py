import turtle as trtl

spider_painter = trtl.Turtle()

spider_painter.pensize(40)
spider_painter.circle(20)

legs = 6
leg_length = 70
angle = 380 / legs
print("angle=", angle)

spider_painter.pensize(5)
current_leg = 0
while current_leg < legs:
    spider_painter.goto(0, 0)
    spider_painter.setheading(angle * current_leg)
    print("z*n=", angle * current_leg)
    spider_painter.forward(leg_length)
    current_leg = current_leg + 1
spider_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
