
import turtle
import _tkinter as tk
import sys
sys.stdin = open("hexifier.txt", "r")
width, height = input().split()
hexl = []
hexl = list(input().split())

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(900, 1200)

# Create a Turtle object
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed (0 is the fastest)

# Set the initial position for drawing
x, y = -450, 600

# Set the size of each square
square_size = 1

# Loop through the list of hex color codes and draw dots
for hex_code in hexl:
    t.penup()
    t.goto(x, y)
    t.dot(square_size, hex_code)  # Draw a dot with the hex code as color

    # Move to the next position
    x += square_size
    if x == 450:
        x = -450
        y -= square_size

# Close the Turtle window on click
screen.exitonclick()
