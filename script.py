import turtle
import _tkinter as tk
import sys
sys.stdin = open("hexifier.txt", "r")
width, height = input().split()
hexl = []
hexl = list(input().split())
# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(326811,240948) 
#326,811 x 240,948

# Create a Turtle object
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed (0 is the fastest)

# Set the initial position for drawing
x, y = -600, 500

# Set the size of each square
square_size = 1

ptr = 0
# Loop through the list of hex color codes and draw squares
for hex_code in hexl:
    t.penup()
    t.goto(x, y)
    t.fillcolor(hex_code)  # Set the fill color to the hex code
    t.begin_fill()  # Start filling
    for _ in range(4):  # Draw a square
        t.forward(square_size)
        t.right(90)
    t.end_fill()  # End filling

    # Move to the next position
    x += square_size
    ptr+=1
    if ptr == width:
        ptr = 0
        y -= square_size
        x = 100

# Close the Turtle window on click
screen.exitonclick()