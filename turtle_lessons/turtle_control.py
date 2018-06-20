import turtle
import random
import math

drawer = turtle.Turtle()
drawer.hideturtle()

colors = ["pink", "aqua", "blue", "violet", "cyan"]

point_list = []

CIRCLE_RADIUS = 8

range_x = (0.0, 300.0)
range_y = (0.0, 300.0)

#Get the turtle object
franklin = turtle.Turtle()

franklin_coordinate = None

#Set turtle's initial shape to a turtle
franklin.shape("turtle")

#Get the screen object
screen = turtle.Screen()

#Move the turtle object forward by 1 pixel
def move_right():
    global franklin_coordinate
    global point_list

    franklin.forward(4)

    franklin_x = int(franklin.xcor())
    franklin_y = int(franklin.ycor())

    franklin_coordinate = (franklin_x, franklin_y)
    is_in_circle(franklin_coordinate, point_list)
#Move the turtle object backward by 1 pixel
def move_left():
    global franklin_coordinate
    global point_list

    franklin.forward(-1)

    franklin_x = int(franklin.xcor())
    franklin_y = int(franklin.ycor())

    franklin_coordinate = (franklin_x, franklin_y)
    is_in_circle(franklin_coordinate, point_list)

#Turn the turtle counterclockwise by 1 degree
def turn_left():
    franklin.left(4)

#Turn the turtle clockwise by 1 degree
def turn_right():
    franklin.right(4)

#Make a copy of the turtle
def stamp_location():
    franklin.stamp()

#Change the turtle's shape to a circle
def change_to_circle():
    franklin.shape("circle")

#Change the turtle's shape to a turtle
def change_to_turtle():
    franklin.shape("turtle")

def pen_up():
    franklin.penup()

def pen_down():
    franklin.pendown()

def move_turtle_to_point(position):
    drawer.penup()
    drawer.goto(position[0],position[1])
    drawer.pendown()

def draw_circle(radius):
    drawer.circle(radius)

def is_in_circle(position, point_list):
    for point in point_list:
        location = math.sqrt((position[0] - point[0]) ** 2 + (position[1] - point[1]) ** 2)
        if location < CIRCLE_RADIUS:
            print "franklin is inside a circle"
            franklin.fillcolor(random.choice(colors))

def teleport_franklin(position):
    ''' when franklin enters a circle, teleport him to a random circle'''
    pass

def racer_turtle(point_list):
    '''Create a second turtle to race against Franklin '''
    pass

for value in range(15):
    x = random.randrange(*range_x)
    y = random.randrange(*range_y)
    point_list.append((x,y))

for point in point_list:
    move_turtle_to_point(point)
    draw_circle(CIRCLE_RADIUS)


#Set the screen.onkey functions
screen.onkey(move_right, "Up")
screen.onkey(move_left, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(stamp_location, "k")
screen.onkey(change_to_circle, "c")
screen.onkey(change_to_turtle, "t")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")

#Add event listener to Screen
screen.listen()

#mainloop
turtle.mainloop()
