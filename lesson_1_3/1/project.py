import turtle as trtl
import logging


# init logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main")

# init turtle
pen = trtl.Turtle(visible=False)
pen.speed(0)
pen.penup()

instructions_pen = trtl.Turtle(visible=False)
instructions_pen.penup()

wn = trtl.Screen()


# init variables
size = 14
lines = size + 1
box_size = 25
offset_x = -200
offset_y = -200
board = []
all_win_solution = [[{} for j in range(lines)] for i in range(lines)]
solution_amount = 0
player_win_solution = []
computer_win_solution = []
current_color = "B"
is_player_black = True

# setup solutions
for i in range(lines):
    for j in range(lines - 4):
        for k in range(5):
            all_win_solution[i][j + k][solution_amount] = True
        solution_amount += 1

for i in range(lines):
    for j in range(lines - 4):
        for k in range(5):
            all_win_solution[j + k][i][solution_amount] = True
        solution_amount += 1

for i in range(lines - 4):
    for j in range(lines - 4):
        for k in range(5):
            all_win_solution[i + k][j + k][solution_amount] = True
        solution_amount += 1

for i in range(lines - 4):
    for j in range(lines - 1, 3, -1):
        for k in range(5):
            all_win_solution[i + k][j - k][solution_amount] = True
        solution_amount += 1


def change_color_mode():
    global is_player_black
    is_player_black = not is_player_black
    init_game()


def init_game():
    global board, player_win_solution, computer_win_solution, current_color
    wn.clear()
    wn.onkey(init_game, "r")
    wn.onkey(init_game, "R")
    wn.onkey(change_color_mode, "t")
    wn.onkey(change_color_mode, "T")
    wn.listen()
    instructions_pen.goto(-200, 230)
    instructions_pen.write("You are " + ("black side" if is_player_black else "white side"), font=("Arial", 20, "normal"))
    instructions_pen.goto(-200, 200)
    instructions_pen.write("Press R to restart", font=("Arial", 20, "normal"))
    instructions_pen.goto(-200, 170)
    instructions_pen.write("Press T to be change color", font=("Arial", 20, "normal"))
    board = [[None for j in range(lines)] for i in range(lines)]
    player_win_solution = {}
    computer_win_solution = {}
    current_color = "B"
    create_board()
    wn.onclick(on_click)
    if not is_player_black:
        board[7][7] = "B"
        create_piece(7, 7, "B")
        is_win(7, 7, "B")
        change_color()


def tracer_off(fn):
    def wrapped(*args, **kwargs):
        wn.tracer(False)
        result = fn(*args, **kwargs)
        wn.tracer(True)
        return result

    return wrapped


@tracer_off
def create_piece(index_x, index_y, color):
    x = index_x * box_size + offset_x
    y = index_y * box_size + offset_y
    board[index_x][index_y] = color

    if color == "B":
        pen.fillcolor(0, 0, 0)
    else:
        pen.fillcolor(1, 1, 1)
    pen.begin_fill()
    pen.goto(x, y - 10)
    pen.pendown()
    pen.circle(10)
    pen.end_fill()
    pen.penup()


@tracer_off
def create_board():
    pen.goto(offset_x, offset_y)
    pen.fillcolor(0.78, 0.67, 0.13)
    pen.begin_fill()
    pen.pendown()
    pen.goto(offset_x, size * box_size + offset_y)
    pen.goto(size * box_size + offset_x, size * box_size + offset_y)
    pen.goto(size * box_size + offset_x, offset_y)
    pen.goto(offset_x, offset_y)
    pen.end_fill()
    pen.penup()

    for i in range(size):
        pen.goto(offset_x, i * box_size + offset_y)
        pen.pendown()
        pen.goto(size * box_size + offset_x, i * box_size + offset_y)
        pen.penup()
    for i in range(size):
        pen.goto(i * box_size + offset_x, offset_y)
        pen.pendown()
        pen.goto(i * box_size + offset_x, size * box_size + offset_y)
        pen.penup()


def is_out_of_bounds(x, y):
    return x < 0 or x > size or y < 0 or y > size


def is_box_empty(x, y):
    return board[x][y] == None


def is_win(x, y, color):
    for i in range(solution_amount):
        if color == "B":
            if i in all_win_solution[x][y]:
                if i not in player_win_solution:
                    player_win_solution[i] = 0
                player_win_solution[i] += 1
                computer_win_solution[i] = 6
            if player_win_solution.get(i) == 5:
                return True
        else:
            if i in all_win_solution[x][y]:
                if i not in computer_win_solution:
                    computer_win_solution[i] = 0
                computer_win_solution[i] += 1
                player_win_solution[i] = 6
            if computer_win_solution.get(i) == 5:
                return True
    return False


def change_color():
    global current_color
    if current_color == "B":
        current_color = "W"
    else:
        current_color = "B"


def on_click(x, y):
    global current_color
    if (is_player_black and current_color == "W") or (
        (not is_player_black) and current_color == "B"
    ):
        return

    index_x = round((x - offset_x) / box_size)
    index_y = round((y - offset_y) / box_size)
    logger.info(
        f"click event: on ({x} {y}) => ({index_x} {index_y}), color: {current_color}"
    )
    if is_out_of_bounds(index_x, index_y):
        logger.info("click event error: Out of bounds")
        return
    if not is_box_empty(index_x, index_y):
        print("click event error: Box is not empty")
        return
    create_piece(index_x, index_y, current_color)

    if is_win(index_x, index_y, current_color):
        logger.info("game end, player win")
        after_win("player")
        return
    change_color()
    on_computer()
    change_color()


def on_computer():
    player_score = [[0 for j in range(lines)] for i in range(lines)]
    computer_score = [[0 for j in range(lines)] for i in range(lines)]
    max_score = 0
    temp_i = 0
    temp_j = 0

    for i in range(lines):
        for j in range(lines):
            if board[i][j] == None:
                for k in range(solution_amount):
                    if k in all_win_solution[i][j]:
                        if k in player_win_solution:
                            if player_win_solution[k] == 1:
                                player_score[i][j] += 200
                            elif player_win_solution[k] == 2:
                                player_score[i][j] += 400
                            elif player_win_solution[k] == 3:
                                player_score[i][j] += 2000
                            elif player_win_solution[k] == 4:
                                player_score[i][j] += 10000
                        if k in computer_win_solution:
                            if computer_win_solution[k] == 1:
                                computer_score[i][j] += 220
                            elif computer_win_solution[k] == 2:
                                computer_score[i][j] += 420
                            elif computer_win_solution[k] == 3:
                                computer_score[i][j] += 2100
                            elif computer_win_solution[k] == 4:
                                computer_score[i][j] += 20000
                if player_score[i][j] > max_score:
                    max_score = player_score[i][j]
                    temp_i = i
                    temp_j = j
                elif player_score[i][j] == max_score:
                    if computer_score[i][j] > computer_score[temp_i][temp_j]:
                        temp_i = i
                        temp_j = j

                if computer_score[i][j] > max_score:
                    max_score = computer_score[i][j]
                    temp_i = i
                    temp_j = j
                elif computer_score[i][j] == max_score:
                    if player_score[i][j] > player_score[temp_i][temp_j]:
                        temp_i = i
                        temp_j = j

    create_piece(temp_i, temp_j, current_color)
    if is_win(temp_i, temp_j, current_color):
        logger.info("game end, computer win")
        after_win("computer")


def after_win(who_win):
    wn.onclick(None)
    wn.clear()
    wn.onkey(init_game, "r")
    wn.onkey(init_game, "R")
    end_pen = trtl.Turtle()
    end_pen.hideturtle()
    end_pen.penup()
    end_pen.goto(-200, 0)
    end_pen.write(f"Game Over, {who_win} win", font=("Arial", 30, "normal"))
    end_pen.goto(-100, -50)
    end_pen.write("Press R to restart", font=("Arial", 20, "normal"))


init_game()

wn.mainloop()
