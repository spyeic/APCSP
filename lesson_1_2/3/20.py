import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

number_list = []
for i in range(4):
    number_list.append(rand.randint(1, 4))

print(number_list)
temp_turtle = trtl.Turtle()
temp_turtle.hideturtle()
font = ("Arial", 74, "bold")
if 4 in number_list:
    temp_turtle.write("4 in list.", font=font)
else:
    temp_turtle.write("4 not in list.", font=font)


trtl.mainloop()
