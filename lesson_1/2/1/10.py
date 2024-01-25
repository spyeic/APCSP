#-----import statements-----
import turtle as trtl

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


#-----events----------------
wn = trtl.Screen()
wn.mainloop()