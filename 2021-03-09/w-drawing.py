import turtle
window = turtle.Screen()
window.setup( 600, 400 )
window.title('Drawing W' )

felix = turtle.getturtle()
felix.hideturtle()

felix.color( 'black', 'DarkTurquoise' ) # fona kraasa, aizpildijuma krasa

l = 50

felix.penup()
felix.setposition(-l,0)
felix.pendown()

turtle.right(60)
felix.forward(l) 

turtle.left(120)
felix.forward(l) 

turtle.right(120)
felix.forward(l) 

turtle.left(120)
felix.forward(l)

turtle.exitonclick()
