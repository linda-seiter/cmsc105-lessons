# magic_sparkle.py
import random
import turtle
import time

BACKGROUND_COLOUR = "#1a6b72"

lead_dot_speed = 1

window = turtle.Screen()
window.tracer(0)
window.bgcolor(BACKGROUND_COLOUR)

lead_dot = turtle.Turtle()
lead_dot.shape("circle")
lead_dot.color("white")
lead_dot.penup()


def go_left():
    lead_dot.setheading(180)


def go_right():
    lead_dot.setheading(0)


window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.listen()

def make_new_dot():
    new_dot = turtle.Turtle()
    new_dot.shape("circle")
    r = random.random()
    g = random.random()
    b = random.random()
    new_dot.color((r, g, b))
    new_dot.penup()
    new_dot.goto(lead_dot.xcor(), lead_dot.ycor())
    new_dot.setheading(270)
    return new_dot

interval_start = 0
dots = []
while True:
    lead_dot.forward(lead_dot_speed)
    if time.time() - interval_start > 0.5:
        interval_start = time.time()
        dots.append(make_new_dot())
    for dot in dots:
       dot.forward(1)
       if dot.ycor() < -window.window_height() / 2 :
            dots.remove(dot)
            turtle.turtles().remove(dot)
    # print(f"\nNumber of dots in the 'dots' list: {len(dots)}")
    # print(f"Number of dots in the 'turtle.turtles()' list: {len(turtle.turtles())}")
    window.update()
