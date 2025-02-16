from turtle import *

# TODO: Prompt for pen color and store in variable pen_color
pen_color = input('Pen color: ' )

# Set the pen size and pen color
pensize(5)
color(pen_color)

# TODO: Draw three lines with length 200 to form a triangle.
forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(120)

# Keep the window open so you can see the drawing until you close it manually.
done()
