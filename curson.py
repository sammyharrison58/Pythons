import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.colormode(1)


def heart(t_param, scale=15):
    x = 16 * (math.sin(t_param)) ** 3
    y = (
        13 * math.cos(t_param)
        - 5 * math.cos(2 * t_param)
        - 2 * math.cos(3 * t_param)
        - math.cos(4 * t_param)
    )
    return x * scale, y * scale


points = []
steps = 200
for i in range(steps):
    t_param = i * (2 * math.pi / steps)
    points.append(heart(t_param))

h = 0

for x, y in points:
    t.penup()
    t.goto(0, 0)
    t.pendown()

    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    h += 0.01

    t.goto(x, y)
    t.penup()
    t.goto(x, y)
    t.dot(10)

turtle.done()
