#! usr/bin/env python2
import turtle

# determines what shape the pen is
turtle.shape("turtle")
# could uncomment turtle penup to make the turtle draw
# turtle.penup()

# defines boundary variables for where the turtle can go
x, y = 0, 0
xdir, ydir = 3, 3
xlimit, ylimit = turtle.window_width() / 2, turtle.window_height() / 2


def move():
    global x, y, xdir, ydir

    x = x + xdir
    y = y + ydir

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir

    turtle.goto(x, y)

    turtle.ontimer(move, 3)


turtle.ontimer(move, 3)

turtle.exitonclick()
