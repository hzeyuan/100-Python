import turtle
from random import randrange

snake = [[0, 0]]
aim = [0, 10]
food = [-10, 0]


def change_direction(x, y):
    aim[0] = x
    aim[1] = y


def sqaure(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


import copy

def inside(head):
    return -250<head[0]<250 and -250 <head[1] <250

def snake_move():
    #head = snake[-1][:]
    head = [snake[-1][0],snake[-1][1]]
    #head = copy.deepcopy(snake[-1])
    head = [head[0] + aim[0], head[1] + aim[1]]
    #print(head)
    if head in snake or not inside(head):
        sqaure(head[0],head[1],10,'red')
        turtle.update()
        return
    if head == food:
        print("snake", len(snake))
        food[0] = randrange(-15, 15) * 10
        food[1] = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    snake.append(head)
    turtle.clear()
    sqaure(food[0], food[1], 10, "green")
    for body in snake:
        sqaure(body[0], body[1], 10, "black")
    turtle.update()
    turtle.ontimer(snake_move, 300)

turtle.setup(500,500)
turtle.hideturtle()
turtle.listen()
turtle.onkey(lambda: change_direction(0, 10), "Up")
turtle.onkey(lambda: change_direction(0, -10), "Down")
turtle.onkey(lambda: change_direction(-10, 0), "Left")
turtle.onkey(lambda: change_direction(10, 0), "Right")
turtle.tracer(False)
snake_move()
turtle.done()


