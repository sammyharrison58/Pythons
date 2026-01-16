from turtle import *
from colorsys import *

tracer(10)
bgcolor("black")
left(90)
up()
goto(0, -200)
down()


def draw_tree(len):
    if len < 5:
        return
    else:
        h = 0.3 - (len / 200) * 0.3
        color(hsv_to_rgb(h, 1, 1))
        forward(len)
        right(25)
        draw_tree(len * 0.75)
        left(50)
        draw_tree(len * 0.75)
        right(25)
        backward(len)


draw_tree(120)
done()
