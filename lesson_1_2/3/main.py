import turtle as trtl
import random as rand

# -----setup-----
number_of_apples = 5
apple_list = []
random_letters = []
for i in range(number_of_apples):
    while True:
        # Generate a random number between 65 and 90 (inclusive)
        # Convert the number to a character and add it to the list
        # 65 is the ASCII value of 'A'
        # 90 is the ASCII value of 'Z'
        num = rand.randint(65, 90)
        if chr(num) not in random_letters:
            random_letters.append(chr(num))
            break

print(random_letters)
apple_image = "apple.gif"  # Store the file name of your shape
font = ("Courier", 40, "bold")

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("background.gif")


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
    active_apple.goto(x - 18, y - 40)
    active_apple.color("white")
    active_apple.write(letter, font=font)
    active_apple.goto(x, y)


# TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter, apple_image):
    wn.tracer(False)
    active_apple.shape(apple_image)
    draw_letter(active_apple, letter)
    wn.tracer(True)
    wn.update()


# TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.
# TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.
# We use a function instead of functions per letter because it has less code duplication.
def drop_apple(apple):
    apple.clear()
    apple.goto(apple.xcor(), -150)
    apple.hideturtle()


# -----function calls-----
# TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

for i in range(number_of_apples):
    apple = trtl.Turtle(visible=False)
    apple.penup()
    new_location(apple)
    draw_apple(apple, random_letters[i], apple_image)
    apple.showturtle()
    print(random_letters[i])
    def on_press(apple=apple):
        drop_apple(apple)
    wn.onkeypress(on_press, random_letters[i])
    wn.onkeypress(on_press, random_letters[i].lower())

    apple_list.append(apple)

wn.listen()
wn.mainloop()
