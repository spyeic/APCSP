# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color = input("What color would you like the circle to be? ")

# ask user for the radius of a circle
radius = int(input("What radius would you like the circle to be? "))

# draw a circle with the radius and line color entered by the user
painter.pencolor(color)
painter.circle(radius)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
