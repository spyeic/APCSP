#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
# painter.speed(0)
painter.pensize(5)

# Add a loop with a zero-iteration condition
i = 0
while i < 0:
    painter.circle(50, 360, i + 3)
    i += 1

# Add an infinite loop
while i >= 0:
    painter.circle(30 * i, 360, 5)
    i += 1


wn = trtl.Screen()
wn.mainloop()