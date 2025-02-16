# https://medium.com/edureka/python-turtle-module-361816449390
import random
import turtle
import time

def move():
    if head.direction == "up":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x - 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


#set up the screen
win = turtle.Screen()
win.title("My snake game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "up"

# keyboard bindings
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.listen()

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# Main game loop
delay=0.5
while True:
    win.update()
    move()
    time.sleep(delay)
    if head.distance(food) < 15:
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
