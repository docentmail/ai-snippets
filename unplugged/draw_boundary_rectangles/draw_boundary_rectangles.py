from PIL import Image, ImageDraw

# read 001_rectangles.json
import json
with open("001_rectangles.json", "r") as file:
    rectangles = json.load(file)

# read 001_image.jpg
image = Image.open("001_image.jpg")

# iterate over the rectangles   
for rectangle in rectangles["results"]:
    x1= rectangle["coordinates"]["x1"]
    y1= rectangle["coordinates"]["y1"]
    x2= rectangle["coordinates"]["x2"]
    y2= rectangle["coordinates"]["y2"]
    
    draw = ImageDraw.Draw(image)
    draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
    draw.text((x1, y1), rectangle["label"], fill="blue")




image.show()

image.save("001_image_with_rectangles.jpg")


"""

# Create a blank white image
image = Image.new("RGB", (200, 200), "white")

# Create a draw object
draw = ImageDraw.Draw(image)

# Draw a line
draw.line((10, 10, 190, 10), fill="black", width=2)

# Draw a rectangle
draw.rectangle((50, 50, 150, 150), outline="blue", width=2)

# Draw a circle (ellipse)
draw.ellipse((70, 70, 130, 130), outline="red", width=2)

# Draw text
draw.text((10, 170), "Hello, PIL!", fill="green")

# Save or show the image
image.show()
# image.save("example.png")


from PIL import Image, ImageDraw, ImageFont

# Open or create an image
image = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.truetype("arial.ttf", 20)  # Make sure arial.ttf is available

# Draw text with the font
draw.text((50, 100), "Hello, World!", font=font, fill="blue")

image.show()

"""