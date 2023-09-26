import turtle as trtl
import math

is_show_orbit = input("Show orbit? (y/n): ")
circle_count = int(input("How many circles? (1-10): "))

# init screen
wn = trtl.Screen()
wn.setup(width=900, height=900)

# init background color
wn.bgcolor("black")
# register shapes
wn.register_shape("earth.gif")
wn.register_shape("sun.gif")
wn.register_shape("moon.gif")


# init elements
sun = trtl.Turtle(shape="sun.gif")
earth = trtl.Turtle(shape="earth.gif", visible=False)
earth.penup()
earth.pencolor("red")
earth.goto(300, 0)
earth.showturtle()
earth.setheading(90)
moon = trtl.Turtle(shape="moon.gif", visible=False)
moon.penup()
moon.pencolor("white")
moon.goto(380, 0)
moon.showturtle()

# draw orbit if needed
if is_show_orbit == "y":
    earth.pendown()
    moon.pendown()

# init orbit radius
earth_orbit_redius = 300
moon_orbit_redius = 80

# run animation
for i in range(circle_count):
    # use for loop to draw 360 degree
    for deg in range(360):
        # every 1 degree, move earth and moon
        earth.goto(
            earth_orbit_redius * math.cos(math.radians(deg)),
            earth_orbit_redius * math.sin(math.radians(deg)),
        )
        day = deg % 30 + 1
        moon.goto(
            earth.xcor() + moon_orbit_redius * math.cos(math.radians(day * 12)),
            earth.ycor() + moon_orbit_redius * math.sin(math.radians(day * 12)),
        )

wn.mainloop()
