import turtle

#Get the turtle object
foo = turtle.Turtle()

#Move the turtle object forward by 1 pixel
def move_right():
    foo.forward(1)

#Move the turtle object backward by 1 pixel
def move_left():
    foo.forward(-1)

#Turn the turtle counterclockwise by 1 degree
def turn_left():
    foo.left(1)
#Turn the turtle clockwise by 1 degree
def turn_right():
    foo.right(1)

#Make a copy of the turtle
def stamp_location():
    foo.stamp()

#Change the turtle's shape to a circle
def change_to_circle():
    foo.shape("circle")

#Change the turtle's shape to a turtle
def change_to_turtle():
    foo.shape("turtle")

#Set turtle's initial shape to a turtle
foo.shape("turtle")

#Get the screen object
screen = turtle.Screen()

#Set the onkey functions
screen.onkey(move_right, "Up")
screen.onkey(move_left, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(stamp_location, "space")
screen.onkey(change_to_circle, "s")
screen.onkey(change_to_turtle, "t")

#Add event listener to Screen
screen.listen()

#mainloop
turtle.mainloop()
