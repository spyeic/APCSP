import turtle as trtl
import random as rand

# -----setup-----
letters = ["A", "B", "C", "D", "E"]
apple_image = "apple.gif"  # Store the file name of your shape
font = ("Arial", 40, "bold")

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
apple.hideturtle()
apple.showturtle()


# -----functions-----
# TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters
def new_location(active_apple):
    active_apple.goto(rand.randint(-100, 100), rand.randint(-35, 120))


# TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def draw_letter(active_apple, letter):
    x = active_apple.xcor()
    y = active_apple.ycor()
    active_apple.goto(x - 12.5, y - 25)
    active_apple.color("white")
    active_apple.write(letter, font=font)
    active_apple.goto(x, y)


# TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter, apple_image):
    wn.tracer(False)
    active_apple.shape(apple_image)
    new_location(active_apple)
    draw_letter(active_apple, letter)
    wn.tracer(True)
    wn.update()


# TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.


# TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#


def drop_apple():
    apple.clear()
    apple.goto(apple.xcor(), -150)
    apple.hideturtle()


# -----function calls-----
# TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

letter = rand.choice(letters)
draw_apple(apple, letter, apple_image)
print(letter)
wn.onkeypress(drop_apple, letter)
wn.onkeypress(drop_apple, letter.lower())
wn.listen()

wn.mainloop()
