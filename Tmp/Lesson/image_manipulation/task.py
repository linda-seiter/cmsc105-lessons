from PIL import Image, ImageDraw, ImageFilter

#Open image using Image module
image = Image.open("images/penguin.png")

#Show actual Image
image.show()

(width, height) = image.size
print("Dimensions:", width, height)

#Show rotated Image
rotated_image = image.rotate(45)
rotated_image.show()

#Crop
(left, upper, right, lower) = (50, 25, 250, 150)
cropped_image = image.crop((left, upper, right, lower))
cropped_image.show()

#Draw lines over the image
image_copy = image.copy()
drawing = ImageDraw.Draw(image_copy)
drawing.circle((width/2, height/2-20), 20, fill="blue")
image_copy.show()


