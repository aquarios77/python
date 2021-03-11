import turtle
import random

# create grpphic window, get a reference to this window
window = turtle.Screen()
# set window dimensions
window.setup(600 , 400)
# set window title
window.title("Turtle race")

trase = turtle.getturtle()
trase.speed(0)

trase.penup()
trase.goto(-140, 140)

for step in range(15):
    trase.write(step , align="center")
    trase.right(90)
    trase.forward(10)
    for i in range(15):
        trase.pendown()
        trase.forward(6)
        trase.penup()
        trase.forward(4)
    trase.backward(160)
    trase.left(90)
    trase.forward(20)


# create new turtle 
colors = ["red" , "blue" , "green" , "orange" , "violet"]
turtles = []

n = 5
x = -140
y = 100

for i in range(n):
    ada = turtle.Turtle()
    ada.color(colors[i])
    ada.shape("turtle")
    ada.penup()
    ada.goto(x,y - i * 30)
    ada.pendown()
    turtles.append(ada)

# turtles rotate before race
for i in range(n):
    for turn in range(10):
        turtles[i].right(36)


# ada and bob get running
for turn in range(100):
    for i in range(n):
        turtles[i].forward(random.randint(1,5))

turtle.exitonclick()