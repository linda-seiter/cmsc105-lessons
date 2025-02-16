from PIL import Image

#Open image using Image module
image = Image.open("images/python.png")

#Show original Image
image.show()

#print Image dimensions
print(image.size)

# Resize image to 200x300
new_size = (200, 300)  #(width, height)
resized_image = image.resize(new_size)
resized_image.show()

# Rotate resized image 90 degrees
rotated_image = resized_image.rotate(90)
rotated_image.show()