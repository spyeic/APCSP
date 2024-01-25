import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("gray")
turtle_list.append(temp_turtle)

turtle_list[0].forward(500)
turtle_list[1].setheading(45)
turtle_list[1].forward(500)
turtle_list[2].setheading(315)
turtle_list[2].forward(500)
turtle_list[3].setheading(180)
turtle_list[3].forward(500)

trtl.mainloop()
