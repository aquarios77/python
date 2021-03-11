from turtle import *

speed(0)
penup()
goto(-140 , 140)
# step vertibas no intervala [0;6]

for step in range(15):
    write(step , align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

exitonclick()