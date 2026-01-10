import turtle


CURVE_DEGREES = 200
STEP = 1
LEFT_ANGLE = 140
INNER_ANGLE = 120
EDGE = 111.65
PEN_SIZE = 3
OUTLINE_COLOR = "red"
FILL_COLOR = "pink"
BG_COLOR = "black"


def draw_curve(t, degrees=CURVE_DEGREES, step=STEP):
    """Draw a smooth right-turning curve with small steps."""
    for _ in range(degrees):
        t.right(1)
        t.forward(step)


def main():
    screen = turtle.Screen()
    screen.bgcolor(BG_COLOR)
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.pensize(PEN_SIZE)
    t.color(OUTLINE_COLOR, FILL_COLOR)

    t.begin_fill()
    t.left(LEFT_ANGLE)
    t.forward(EDGE)
    draw_curve(t)
    t.left(INNER_ANGLE)
    draw_curve(t)
    t.forward(EDGE)
    t.end_fill()
    t.hideturtle()

    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
