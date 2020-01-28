"""
井字棋游戏
1.画井字棋盘
2.画圆
3.画x
4.判断输赢
"""
import turtle
from math import sqrt

height, width = 600, 600
# 井字棋所有格子的中心位置
position = {(-200, 200): 0, (0, 200): 0, (200, 200): 0
    , (-200, 0): 0, (0, 0): 0, (200, 0): 0
    , (-200, -200): 0, (0, -200): 0, (200, -200): 0}
circle_list = []
x_list = []
last_persion = None  # 最后下棋的玩家


# 画线
def draw_line(x, y, direction=None):
    if direction:
        turtle.seth(direction)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)


# 在井字棋里面画圆或者x
def draw_flag(x, y):
    global last_persion
    in_pos = None
    can_write = False
    for p in position.keys():
        if (p[0] - x) * 2 + (p[1] - y) ** 2 < 10000:
            in_pos = p
            if position.get(in_pos, None) == 0:
                can_write = True
                break
    if can_write:
        # 画x或者画圈，当can_write==True是，画圆，否则画x
        if len(circle_list)>len(x_list):
            circle_x = False
            position[in_pos] = 'x'
            last_persion = 'x'
            x_list.append(in_pos)
        else:
            circle_x = True
            position[in_pos] = 'o'
            last_persion = 'o'
            circle_list.append(in_pos)
        # 画圈圈
        if circle_x:
            turtle.color('red')
            turtle.seth(270)
            turtle.penup()
            turtle.goto(in_pos[0] - 100, in_pos[1])
            turtle.pendown()
            turtle.circle(100)
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


# 判断谁赢了,我们简单判断下就行了
def who_win():
    v = list(position.values())
    # 胜利的情况，一条横向或者一条竖线，或者一条斜线
    win_1 = v[0] == v[1] == v[2] != 0 or v[3] == v[4] == v[5] != 0 or v[6] == v[7] == v[8] != 0
    win_2 = v[0] == v[3] == v[6] != 0 or v[1] == v[4] == v[7] != 0 or v[2] == v[5] == v[8] != 0
    win_3 = v[0] == v[4] == v[8] != 0 or v[2] == v[4] == v[6] != 0
    if win_1 or win_2 or win_3:
        turtle.goto(-120, 0)
        turtle.write("游戏结束，{}是胜利玩家".format(last_persion), font=("Arial", 25, "normal"))
        turtle.onscreenclick(None)


# 井字棋盘
def tic_tac_toe():
    draw_line(-300, 100)
    draw_line(-300, -100)
    draw_line(-100, 300, 270)
    draw_line(100, 300, 270)
    turtle.update()


if __name__ == '__main__':
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.setup(height, width)
    tic_tac_toe()
    turtle.listen()
    turtle.onscreenclick(draw_flag)
    turtle.done()
