import turtle
import random

STAMP_SIZE = 20
SQUARE_SIZE = 20
FINISH_LINE = 200
COLOR_LIST = ["maroon", "aquamarine", "purple", "deepPink", "blueViolet", "gold"]
STARTING_LINE_X = -350
STARTING_LINE_Y = 280
TURTLE_DISTANCE = 90

def draw_starting_line():
    turtle.speed("fastest")
    turtle.penup()
    turtle.setpos(-350, 300)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(520)

def draw_finish_line():
    turtle.shape("square")
    turtle.shapesize(SQUARE_SIZE/STAMP_SIZE)
    turtle.penup()

    for i in range(18):
        turtle.setpos(FINISH_LINE, (300 -(i * SQUARE_SIZE * 2)))
        turtle.stamp()

    for j in range(18):
        turtle.setpos(FINISH_LINE + SQUARE_SIZE, ((300 - SQUARE_SIZE) - (j * SQUARE_SIZE * 2)))
        turtle.stamp()

    turtle.hideturtle()

def move_turtle(turtle_racer):
    turtle_racer.forward(random.randint(1,10))
    if turtle_racer.xcor() < FINISH_LINE:
        turtle.ontimer(lambda turtle_racer=turtle_racer: move_turtle(turtle_racer), 50)

print "Welcome to Turtle Racing!"
number_of_turtles = int(raw_input("How many turtles (between 3 and 6):"))

draw_starting_line()
draw_finish_line()

turtle_list = []

for index in range(number_of_turtles):
    racer = turtle.Turtle("turtle", visible=False)
    racer.speed("fastest")
    racer.penup()
    racer.setpos(STARTING_LINE_X - STAMP_SIZE, STARTING_LINE_Y - index * TURTLE_DISTANCE)
    racer.color(COLOR_LIST[index])
    racer.showturtle()

    turtle_list.append(racer)

for racer in turtle_list:
    turtle.ontimer(lambda turtle_racer=racer: move_turtle(turtle_racer), 100)

turtle.mainloop()
