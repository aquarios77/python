import random
import math
import turtle
random.seed(100)

# create grpphic window, get a reference to this window
window = turtle.Screen()
# set window dimensions
window.setup(600 , 400)
# set window title
window.title("Rinkis")

# 1. izveidot sarakstus ar x un y koordinatem

n = 10
x = []
y = []

#[0;9]
for i in range(n):
    x.append(random.randint(-100, 100))
    y.append(random.randint(-100, 100))

# 2. izvadit punktu koordinates
for i in range(n):
    print(f'({x[i]}, {y[i]})', end= ' ')
print()



# create turtle
felix = turtle.Turtle()
felix.hideturtle()

# draw axis
felix.setposition(0,0)
felix.goto(-150,0)
felix.goto(150,0)
felix.write("X", align="center")
felix.goto(0,0)
felix.goto(0,-150)
felix.goto(0,150)
felix.write("Y" , align="center")

felix.setposition(0,0)

for i in range(n):
    felix.penup()
    felix.setposition(x[i], y[i])
    felix.pendown()
    felix.dot("red")



# 3. atrast taisnstura stura koordinates
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

# draw min rectanle to include all points
felix.penup()
felix.setposition(x_min, y_min)
felix.pendown()
felix.goto(x_max, y_min)
felix.goto(x_max, y_max)
felix.goto(x_min, y_max)
felix.goto(x_min, y_min)


aug_k_sturis = (x_min, y_max)
aug_l_sturis = (x_max, y_max)
ap_k_sturis = (x_min, y_min)
ap_l_sturis = (x_max, y_min)
print(f'Tainstura sturi: {aug_k_sturis}, {aug_l_sturis}, {ap_k_sturis}, {ap_l_sturis}')

# 4. atrast taistura laukumu
laukums = (x_max - x_min) * (y_max - y_min)
print(f'Taisnstura laukums: {laukums}')

# 5. atrast rinka radiusu un laukumu
punktu_attalumi = []
for i in range(n):
    attalums = math.sqrt(x[i] ** 2 + y[i] ** 2)
    punktu_attalumi.append(round(attalums,2))
print(punktu_attalumi)

radiuss = max(punktu_attalumi)

# draw min circle to include all points
felix.penup()
felix.goto(0,-radiuss)
felix.pendown()
felix.circle(radiuss)

#laukums = round(math.pi * radiuss ** 2,2)
laukums = math.pi * radiuss ** 2
print(f'Rinka radiuss: {radiuss}')
print(f'Rinka laukums: {laukums:.2f}')

turtle.exitonclick()


