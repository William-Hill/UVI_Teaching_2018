import turtle
# import turtlebounce

#Get the turtle object
franklin = turtle.Turtle()

#Move the turtle object forward by 1 pixel
def move_right():
    franklin.forward(1)

#Move the turtle object backward by 1 pixel
def move_left():
    franklin.forward(-1)

#Turn the turtle counterclockwise by 1 degree
def turn_left():
    franklin.left(1)
#Turn the turtle clockwise by 1 degree
def turn_right():
    franklin.right(1)

#Make a copy of the turtle
def stamp_location():
    print "stamped"
    franklin.stamp()

#Change the turtle's shape to a circle
def change_to_circle():
    franklin.shape("circle")

#Change the turtle's shape to a turtle
def change_to_turtle():
    franklin.shape("turtle")


# def turn_up():
#     move()

#Set turtle's initial shape to a turtle
franklin.shape("turtle")

# defines boundary variables for where the turtle can go
x, y = 0, 0
xdir, ydir = 3, 3
xlimit, ylimit = franklin.window_width() / 2, franklin.window_height() / 2

#Get the screen object
screen = turtle.Screen()

def turn_up():
    print 'entered turn_up'
    global x, y, xdir, ydir

    x = x + xdir
    y = y + ydir

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir

    franklin.goto(x, y)

    screen.ontimer(turn_up, 3)


# screen.ontimer(turn_up, 3)



#Set the onkey functions
screen.onkey(move_right, "Up")
screen.onkey(move_left, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(stamp_location, "space")
screen.onkey(change_to_circle, "s")
screen.onkey(change_to_turtle, "t")
screen.onkey(turn_up, "u")

#Add event listener to Screen
screen.listen()

#mainloop
turtle.mainloop()
