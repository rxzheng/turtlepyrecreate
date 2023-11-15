import turtle
import _tkinter as tk
import sys


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
turtle.tracer(10000,0)
# Set the initial position for drawing
x, y = -450, 500

#Create text
t.penup()
t.goto(0,-300)
t.setheading(45)
t.color("white")
t.write("HANGING ROCK", move = False, align = 'center', font=("Roboto", 40, "normal"))
t.goto(0,-300)
t.write("61=401776338", move = False, align = 'center', font=("Roboto", 40, "normal"))
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