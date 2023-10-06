# -----import statements-----
import turtle as trtl
import random as rand

# -----game configuration----
screen_width = 800
screen_height = 600
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False
sizes = [0.5, 1, 1.5, 2, 2.5, 3]

# -----initialize turtle-----
spot = trtl.Turtle()
spot.penup()
spot.speed(0)
spot.fillcolor(spot_color)
spot.pencolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)

score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-screen_width / 2 + 40, screen_height / 2 - 40)

counter = trtl.Turtle()
counter.speed(0)
counter.hideturtle()
counter.penup()
counter.goto(screen_width / 2 - 100, screen_height / 2 - 40)

wn = trtl.Screen()
wn.bgcolor("gray")

# -----game functions--------s
def spot_clicked(x, y):
    if timer_up == False:
        update_score()
        change_size()
        change_position()
    else:
        spot.hideturtle()

def change_size():
    spot_size = rand.choice(sizes)
    spot.shapesize(spot_size)

def change_position():
    new_xpos = rand.randint(-screen_width / 2, screen_width / 2)
    new_ypos = rand.randint(-screen_height / 2, screen_height / 2)
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

# -----events----------------
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.setup(width=screen_width, height=screen_height)
wn.mainloop()
