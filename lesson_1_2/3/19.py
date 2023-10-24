import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

for i in range(6):
    temp_turtle = trtl.Turtle()
    temp_turtle.pencolor("red")
    temp_turtle.setheading(60 * i)
    turtle_list.append(temp_turtle)


for active_turtle in turtle_list:
    active_turtle.forward(400)
    active_turtle.setheading(active_turtle.heading()+180)
    active_turtle.forward(250)

trtl.mainloop()
