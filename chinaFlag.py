import turtle
from math import *


# 参考https://www.cnblogs.com/leo1875/p/10398926.html
# 绘制五角星, 默认为正五角星(一个顶点朝正北方)
# 五角星每个顶角的角度为 180/5 = 36度 或 pi/5
# (x, y): 五角星中心点坐标
# size: 中心到顶点的长度, 即外接圆的半径
# angle 旋转角度, 正五角星正北顶点 turtle.left 方式旋转到被绘制五角星的角度
def draw5star(x, y, size=100, angle=0):
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(90)  # 默方向为北方
    turtle.left(angle)
    turtle.forward(size)
    turtle.right(180 - 36 / 2)
    turtle.pendown()
    distance = 2 * size * cos(pi / 10)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(distance)
        turtle.right(144)
    turtle.end_fill()


# 画矩形
# (x,y) 矩形左上角坐标
def drawrectangle(x=0, y=0, height=100, width=100):
    turtle.color("red")
    # turtle.penup()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.pensize(2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()


# 画辅助线
def drawsubline(x=0, y=0, mag=1):
    # 国旗尺寸
    width = 300 * mag
    height = 200 * mag

    # 画中心十字
    turtle.pencolor('black')
    turtle.penup()
    turtle.goto(x + width / 2, y)
    turtle.seth(180)
    turtle.pensize(2)
    turtle.pendown()
    turtle.forward(width)
    turtle.penup()
    turtle.goto(x, y - height / 2)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(height)

    # 画小方格的横线
    for i in range(1, 10):
        # 横线
        turtle.penup()
        turtle.goto(x, y + height / 2 - i * 10 * mag)
        turtle.setheading(180)
        turtle.pendown()
        turtle.forward(width / 2)

    # 画小方格的竖线
    for i in range(1, 15):
        turtle.penup()
        turtle.goto(x - width / 2 + i * 10 * mag, y)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(height / 2)

    # 计算国旗矩形左上角坐标
    r_x = x - width / 2
    r_y = y + height / 2

    # 画大五角星外接圆，圆绘制起始点为圆最右侧切点
    turtle.penup()
    turtle.goto(r_x + 80 * msg, r_y - 50 * msg)
    turtle.pendown()
    turtle.circle(30 * msg)
    # 画四个小星星的外接圆
    t = [(110, 20), (130, 40), (130, 70), (110, 90)]
    for i in t:
        turtle.penup()
        turtle.goto(r_x + i[0] * msg, r_y - i[1] * msg)
        turtle.pendown()
        turtle.circle(10 * msg)

    # 画4个小星到大星中心的连线
    t1 = [(100, 20), (120, 40), (120, 70), (100, 90), (100, 90)]
    for i in t1:
        print(t1)
        turtle.penup()
        turtle.goto(r_x + i[0] * msg, r_y - i[1] * msg)
        turtle.pendown()
        turtle.goto(r_x + 50 * msg, r_y - 50 * msg)



# 绘制五星红旗

def drawflag(msg=1):
    # 国旗尺寸
    width = 300 * msg
    height = 200 * msg

    # 计算国旗矩形左上角坐标
    r_x = - width / 2
    r_y = height / 2
    # 画国旗矩形
    drawrectangle(x=r_x, y=r_y, height=height, width=width)
    # 画最大的五角星
    draw5star(x=r_x + 50 * msg, y=r_y - 50 * msg, size=30 * msg)
    # 从上至下画4颗小五角星, 中心：(100, 20), (120, 40), (120, 70), (100, 90)
    l_size = 10 * msg
    draw5star(x=r_x + 100 * msg, y=r_y - 20 * msg, size=l_size, angle=180 - atan(5 / 3) / pi * 180)
    draw5star(x=r_x + 120 * msg, y=r_y - 40 * msg, size=l_size, angle=180 - atan(7 / 1) / pi * 180)
    draw5star(x=r_x + 120 * msg, y=r_y - 70 * msg, size=l_size, angle=90 - atan(2 / 7) / pi * 180)
    draw5star(x=r_x + 100 * msg, y=r_y - 90 * msg, size=l_size, angle=90 - atan(4 / 5) / pi * 180)


if __name__ == '__main__':
    msg = 2.5
    turtle.tracer(False)
    turtle.setup(300 * msg, 200 * msg)
    turtle.hideturtle()
    drawflag(msg=2.5)
    drawsubline(mag=2.5)
    turtle.done()
