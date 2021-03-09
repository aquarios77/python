import turtle
window = turtle.Screen()
window.setup( 600, 400 )
window.title('My First Turtle Graphics Program' )

felix = turtle.getturtle()
felix.color( 'black', 'DarkTurquoise' ) # fona kraasa, aizpildijuma krasa
felix.begin_fill()


# taking input for the no of the sides of the polygon 
n = int(input("Enter the no of the sides of the polygon : ")) 
l = 50

for _ in range(n): 
    felix.forward(l) 
    turtle.right(360 / n) 

felix.end_fill()
turtle.exitonclick()
