import turtle as trtl
import math
import random

is_show_orbit = input("Show orbit? (y/n): ")
circle_count = float(input("How many circles? (1-10/inf): "))

# init screen
wn = trtl.Screen()
wn.setup(width=900, height=900)

# init background color
wn.bgcolor("black")
# register shapes
shapes = ["earth", "sun", "moon", "star"]
for shape in shapes:
    wn.addshape(f"{shape}.gif")


def new_element(name):
    return trtl.Turtle(shape=f"{name}.gif", visible=False)


# init elements
stars = []
for i in range(5):
    star = new_element("star")
    star.penup()
    star.pencolor("white")
    star.speed(0)
    if i % 2 == 0:
        star.goto(500, random.randint(-450, 450))
        star.setheading(random.randint(90, 270))
    else:
        star.goto(random.randint(-450, 450), 500)
        star.setheading(random.randint(180, 360))
    stars.append(star)

sun = new_element("sun")

earth = new_element("earth")
earth.penup()
earth.pencolor("red")
earth.goto(300, 0)
earth.speed(0)
earth.setheading(90)

moon = new_element("moon")
moon.penup()
moon.pencolor("white")
moon.goto(380, 0)
moon.speed(0)

# show elements
sun.showturtle()
earth.showturtle()
moon.showturtle()
for star in stars:
    star.showturtle()

# draw orbit if needed
if is_show_orbit == "y":
    earth.pendown()
    moon.pendown()

# init orbit radius
earth_orbit_redius = 300
moon_orbit_redius = 80

# run animation
while circle_count > 0:
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
        # move stars for a step
        for star in stars:
            # if star is out of screen, move it to the other side
            if star.xcor() > 500 or star.xcor() < -500 or star.ycor() > 500 or star.ycor() < -500:
                star.hideturtle()
                if round(random.random()) == 1:
                    star.goto(500, random.randint(-450, 450))
                    star.setheading(random.randint(90, 270))
                else:
                    star.goto(random.randint(-450, 450), 500)
                    star.setheading(random.randint(180, 360))
                star.showturtle()
            # move star a random step
            star.forward(random.randint(20, 40))
    circle_count -= 1

wn.mainloop()
