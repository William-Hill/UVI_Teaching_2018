import turtle
import random
import math

#Turtle objec to draw circles
drawer = turtle.Turtle()
drawer.hideturtle()

#franklin!!!!
franklin = turtle.Turtle()

#A List of colors
COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'gold', 'violet', 'orange', 'magenta', 'cyan']

#A list that will hold the circle center point coordinates
point_list = []

#Sets the radius for all circles
CIRCLE_RADIUS = 8

#tuples to hold the range of x and y
range_x = (0.0,300.0)
range_y = (0.0, 300.0)

#Set turtle's initial shape to a turtle
franklin.shape("turtle")

#Variable for holding franklin's calculated coordinate
franklin_coordinate = None

#Get the screen object
screen = turtle.Screen()

#Move the turtle object forward by 1 pixel
def move_right():
    global franklin_coordinate
    global point_list
    franklin.forward(1)

    franklin_x = int(franklin.pos()[0])
    franklin_y = int(franklin.pos()[1])
    franklin_coordinate = (franklin_x, franklin_y)
    print "franklin_coordinate: ", franklin_coordinate
    is_in_circle(franklin_coordinate, point_list)

#Move the turtle object backward by 1 pixel
def move_left():
    global franklin_coordinate
    global point_list
    franklin.forward(-1)

    franklin_x = int(franklin.pos()[0])
    franklin_y = int(franklin.pos()[1])

    franklin_coordinate = (franklin_x, franklin_y)
    print "franklin_coordinate: ", franklin_coordinate

    is_in_circle(franklin_coordinate, point_list)

#Turn the turtle counterclockwise by 1 degree
def turn_left():
    franklin.left(3)

#Turn the turtle clockwise by 1 degree
def turn_right():
    franklin.right(3)

#Set the screen.onkey functions
screen.onkey(move_right, "Up")
screen.onkey(move_left, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

#Move turtle to coordinate
def move_turtle_to(position):
    drawer.up()
    drawer.goto(position[0], position[1])
    drawer.down()

#Fu
def draw_circle(radius=CIRCLE_RADIUS):
    drawer.circle(CIRCLE_RADIUS)

for _ in range(10):
    x_coor = random.randrange(*range_x)
    y_coor = random.randrange(*range_y)
    point_list.append((x_coor,y_coor))

print "point_list:", point_list
print "type in point_list: ", type(point_list[0])

def is_in_circle(position, point_list):
    for circle in point_list:
        location = math.sqrt((position[0] - circle[0]) ** 2 + (position[1] - circle[1]) ** 2)
        # print "location in is_in_circle: ", location
        if location < CIRCLE_RADIUS:
            print "found circle"
            franklin.fillcolor(random.choice(COLORS))

#for loop for creating circles
for point in point_list:
    move_turtle_to(point)
    draw_circle(point)

print "franklin's coordinates: ", franklin.pos()

#Add event listener to Screen
screen.listen()

#mainloop
turtle.mainloop()
