import turtle
window = turtle.Screen()
window.setup( 600, 400 )
window.title('Drawing W' )

felixA = turtle.getturtle()
felixA.hideturtle()

felixA.color( 'red', 'DarkTurquoise' ) # fona kraasa, aizpildijuma krasa

l = 150

felixA.penup()
felixA.setposition(-l/2,-l/2)
felixA.pendown()

turtle.left(60)
felixA.forward(l) 

turtle.right(120)
felixA.forward(l) 

felixA.penup()
turtle.left(180)
felixA.forward(l/2) 
felixA.pendown()

turtle.left(60)
felixA.forward(l/2)


turtle.exitonclick()
