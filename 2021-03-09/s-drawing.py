import turtle
window = turtle.Screen()
window.setup( 600, 400 )
window.title('Drawing W' )

felix = turtle.getturtle()
felix.hideturtle()

felix.color( 'red', 'DarkTurquoise' ) # fona kraasa, aizpildijuma krasa



felix.penup()
felix.setposition(0,-90)
felix.pendown()
felix.right(40)


for i in range(210):
    turtle.left(1)
    felix.forward(1) 

for i in range(210):
    turtle.right(1)
    felix.forward(1) 



turtle.exitonclick()
