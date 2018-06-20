import random
import turtle
import time

STAMP_SIZE = 20
SQUARE_SIZE = 20
FINISH_LINE = 200
COLOR_LIST = ['maroon', 'blue', 'green', 'brown', 'yellow', 'purple']
STARTING_LINE_X = -350
STARTING_LINE_Y = 280
TURTLE_DISTANCE = 90

def draw_starting_line():
    '''Creates the starting line where the turtles start to race '''
    turtle.speed('fastest')
    turtle.penup()
    turtle.setpos(-350, 300)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(520)

def draw_finish_line():
    '''Draws the finish line; Makes it a checkered line '''
    turtle.shape('square')
    turtle.shapesize(SQUARE_SIZE / STAMP_SIZE)
    turtle.penup()

    for i in range(18):
        turtle.setpos(FINISH_LINE, (300 - (i * SQUARE_SIZE * 2)))
        turtle.stamp()

    for j in range(18):
        turtle.setpos(FINISH_LINE + SQUARE_SIZE, ((300 - SQUARE_SIZE) - (j * SQUARE_SIZE  * 2)))
        turtle.stamp()

    turtle.hideturtle()


def move_turtle(who):
    '''Randomly assigns a turtle a speed from 1 - 10 '''
    who.forward(random.randint(1, 10))
    if who.xcor() < FINISH_LINE:
        turtle.ontimer(lambda who=who: move_turtle(who), 50)

print('Welcome to Turtle Racing!')
number_of_turtles = int(raw_input('How many turtles (between 3 and 6): '))

draw_starting_line()
draw_finish_line()

turtle_list = []

for index in range(number_of_turtles):
    racer = turtle.Turtle('turtle', visible=False)
    racer.speed('fastest')  # affects drawing speed, not forward motion
    racer.penup()
    racer.setpos(STARTING_LINE_X - STAMP_SIZE, STARTING_LINE_Y - index * TURTLE_DISTANCE)
    racer.color(COLOR_LIST[index])
    racer.showturtle()

    turtle_list.append(racer)

for racer in turtle_list:
    #Moves each turtle to the starting line
    turtle.ontimer(lambda who=racer: move_turtle(who), 100)

#mainloop
turtle.mainloop()
