from PIL import Image, ImageDraw

image = Image.new("RGB", (500, 300), "white")
drawing = ImageDraw.Draw(image)

# Draw a line
drawing.line((50, 50, 450, 50), fill="black", width=5)

# Draw a rectangle
drawing.rectangle((100, 100, 400, 200), outline="red", fill="green", width=20)

# Draw a circle (ellipse)
drawing.ellipse((150, 75, 350, 225), outline="blue", fill="yellow", width=10)

# Draw text
drawing.text((250, 250), "Hello There!", fill="purple")

# Display image with drawing overlay
image.show()