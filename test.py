import turtle
from random import randrange

snake = [[0, 0], [0, 10]]
aim = [0, 10]
food = [-10, 0]


def direction_change(x, y):
    aim[0] = x
    aim[1] = y


def square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def snake_move():
    head = [snake[-1][0] + aim[0], snake[-1][1] + aim[1]]
    if head == food:
        print("snake的长度:", len(snake))
        food[0] = randrange(-15, 15) * 10
        food[1] = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    snake.append(head)
    turtle.clear()
    for body in snake:
        square(body[0], body[1], 10, "black")
    turtle.update()
    square(food[0], food[1], 10, "green")
    turtle.ontimer(snake_move, 300)


# square(0, 0, 10, "black")
turtle.setup(500,500)
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: direction_change(0, 10), "Up")
turtle.onkey(lambda: direction_change(0, -10), "Down")
turtle.onkey(lambda: direction_change(-10, 0), "Left")
turtle.onkey(lambda: direction_change(10, 0), "Right")

snake_move()
turtle.done()
