from PIL import Image
import sys
import turtle
import _tkinter as tk

sys.stdout = open("hexifier.txt", "w")
# REPLACE IMGPATH WITH THE IMAGE'S PATH
img = Image.open('/Users/richardzheng/Documents/GitHub/turtlepyrecreate/hangingRockImage.jpg')

#RGB
rgb_img = img.convert('RGB')

# Get the width and height of the image
width, height = rgb_img.size



hexl = []
# LOOP THROUgH ALL PIXELS
for y in range(height):
     for x in range(width):
        #RGB of every pixel
        r, g, b = rgb_img.getpixel((x, y))

        #RGB to HEX
        hex_code = '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

        # Print the hex code
        hexl.append(hex_code)

sys.stdout = open("hexifier.txt", "w")
width, height = rgb_img.size


print(str(width)+" "+str(height))
for i in hexl:
  print(i+" ", end = '')


sys.stdin = open("hexifier.txt", "r")
width, height = input().split()
hexl = []
hexl = list(input().split())

# Set up the Turtle scree=
screen = turtle.Screen()
screen.setup(900, 1200)

# Create a Turtle object
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed (0 is the fastest)
turtle.tracer(100000,0)
# Set the initial position for drawing
x, y = -450, 500

# Set the size of each square
square_size = 1

# Loop through the list of hex color codes and draw dots
for hex_code in hexl:
    t.penup()
    t.goto(x, y)
    t.pencolor(hex_code)
    t.pendown()
    t.forward(1)
    # Move to the next position
    x += square_size
    if x == 450:
        x = -450
        y -= square_size
turtle.update
# Close the Turtle window on click
screen.exitonclick()