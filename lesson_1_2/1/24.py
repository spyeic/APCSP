#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"

#-----initialize turtle-----
spot = trtl.Turtle()
spot.penup()
spot.fillcolor(spot_color)
spot.pencolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)


#-----game functions--------
def spot_clicked(x, y):
    change_position()

def change_position():
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.showturtle()

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()