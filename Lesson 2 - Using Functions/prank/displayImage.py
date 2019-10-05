import Image

file = raw_input("What is the name of the image file? ")

image = Image.open(file)
image.show()

