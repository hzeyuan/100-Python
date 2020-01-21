"""
井字棋游戏
1.画井字棋盘
2.画圆
3.画x
4.判断输赢
"""
import turtle
from math import sqrt

width = 600
height = 600
# 所有井字的中心位置
position = {(-200, 200): 0, (0, 200): 0, (200, 200): 0
    , (-200, 0): 0, (0, 0): 0, (200, 0): 0
    , (-200, -200): 0, (0, -200): 0, (200, -200): 0}
circle_list = []
x_list = []
last_person = None  # 最后下棋的玩家


def draw_line(x, y, direction=None):
    if direction:
        turtle.seth(direction)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)


# 井棋盘
def tic_tac_toe():
    draw_line(-300, 100)
    draw_line(-300, -100)
    draw_line(-100, 300, 270)
    draw_line(100, 300, 270)
    turtle.update()

# 在点击的位置画圆，画着画x
def draw_flag(x, y):
    global last_person
    in_pos = None
    can_write = False
    for p in position.keys():
        if (p[0] - x) ** 2 + (p[1] - y) ** 2 < 10000:
            in_pos = p
            if position.get(in_pos, None) == 0:
                can_write = True
                break
    # 该位置可以画圈或x
    if can_write:
        # 画x还是画O,当True时，我们画圈，当False时，我们画x
        if len(circle_list) > len(x_list):
            circle_x = False
            position[in_pos] = 'x'
            last_person = 'x'
            x_list.append(in_pos)
        else:
            circle_x = True
            circle_list.append(in_pos)
            position[in_pos] = 'o'
            last_person = 'o'
        # 画圈圈
        if circle_x:
            turtle.color("red")
            turtle.seth(270)
            turtle.penup()
            turtle.goto(in_pos[0] - 100, in_pos[1])
            turtle.pendown()
            turtle.circle(100)
        # 画x
        else:
            turtle.color("black")
            for i in range(4):
                turtle.penup()
                turtle.goto(in_pos[0], in_pos[1])
                turtle.pendown()
                turtle.seth(45 + i * 90)
                turtle.forward(sqrt(20000))
    turtle.update()
    who_win()

# 判断赢家
def who_win():
    v = list(position.values())
    # 胜利的情况，一条横线，一条竖线，斜线
    win_1 = v[0] == v[1] == v[2] != 0 or v[3] == v[4] == v[5] != 0 or v[6] == v[7] == v[8] != 0
    win_2 = v[0] == v[3] == v[6] != 0 or v[1] == v[4] == v[7] != 0 or v[2] == v[5] == v[8] != 0
    win_3 = v[0] == v[4] == v[8] != 0 or v[2] == v[4] == v[6] != 0
    if win_1 or win_2 or win_3:
        turtle.goto(-120, 0)
        turtle.write("game over,{} is winner".format(last_person), font=("Arial", 25, "normal"))
        turtle.onscreenclick(None)


turtle.setup(width, height)
turtle.tracer(False)
turtle.hideturtle()
turtle.listen()
turtle.onscreenclick(draw_flag)
tic_tac_toe()
turtle.mainloop()
