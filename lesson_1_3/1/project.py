import turtle as trtl

pen = trtl.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

size = 3
box_size = 40
is_x = True
board = [[None for j in range(size)] for i in range(size)]

wn = trtl.Screen()


def tracer_off(fn):
    def wrapped(*args, **kwargs):
        wn.tracer(False)
        result = fn(*args, **kwargs)
        wn.tracer(True)
        return result

    return wrapped


@tracer_off
def createX(x, y):
    pen.goto(x + 10, y + 10)
    pen.pendown()
    pen.goto(x - 10, y - 10)
    pen.penup()
    pen.goto(x - 10, y + 10)
    pen.pendown()
    pen.goto(x + 10, y - 10)
    pen.penup()


@tracer_off
def createO(x, y):
    pen.goto(x, y - 10)
    pen.pendown()
    pen.circle(10)
    pen.penup()


@tracer_off
def createBoard():
    for i in range(size + 1):
        pen.goto(0, i * box_size)
        pen.pendown()
        pen.goto(size * box_size, i * box_size)
        pen.penup()
    for i in range(4):
        pen.goto(i * box_size, 0)
        pen.pendown()
        pen.goto(i * box_size, size * box_size)
        pen.penup()


def is_out_of_bounds(x, y):
    return x < 0 or x > size or y < 0 or y > size


def is_box_empty(x, y):
    return board[x][y] == None


def is_end():
    return True


def on_click(x, y):
    global is_x
    print(x, y)
    index_x = int(x / box_size)
    index_y = int(y / box_size)
    if is_out_of_bounds(index_x, index_y):
        print("Out of bounds")
        return
    if not is_box_empty(index_x, index_y):
        print("Box is not empty")
        return
    x = index_x * box_size + box_size / 2
    y = index_y * box_size + box_size / 2
    print(index_x, index_y)
    if is_x:
        createX(x, y)
        board[index_y][index_x] = "X"
    else:
        createO(x, y)
        board[index_y][index_x] = "O"

    if is_end():
        print("End")
        return
    is_x = not is_x


createBoard()


wn.onclick(on_click)
wn.mainloop()
