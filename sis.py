from turtle import *
import random

setup(width=1000, height=600)
bgcolor("black")
tracer(50)
hideturtle()

chars = "0101010101010101010101010101010010100101010101010100101010010010100110010101001010100101010010101010101010101010101010010"
num_columns = 40
turtles = []
font = ("Courier", 18, "normal")

for i in range(num_columns):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.color("green")
    x = -380 + i * 20
    y = random.randint(-300, 300)
    t.goto(x, y)
    turtles.append(t)


def move_rain():
    for t in turtles:
        char = random.choice(chars)
        t.write(char, align="center", font=font)

        y = t.ycor() - 20
        if y < -300:
            y = 300
            t.goto(t.xcor() + random.randint(-5, 5), y)
            t.color(random.choice(["#00FF00", "#1B5A02", "#009900", "#006600"]))

        t.goto(t.xcor(), y)

    update()
    ontimer(move_rain, 100)


move_rain()
done()
