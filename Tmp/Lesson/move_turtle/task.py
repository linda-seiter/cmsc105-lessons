import turtle

def move_right():
    turtle.setheading(0)
    turtle.forward(50)

def move_up():
    turtle.setheading(90)
    turtle.forward(50)

def move_left():
    turtle.setheading(180)
    turtle.forward(50)

def move_down():
    turtle.setheading(270)
    turtle.forward(50)


screen = turtle.Screen()
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_left, "Left")
screen.onkey(move_down, "Down")


screen.listen()
turtle.mainloop()