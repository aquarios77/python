from point import Point
from rectangle import Rectangle


p2 = Point(100, 80)
box_1 = Rectangle(Point(0, 0), 100, 200)
box_2 = Rectangle(p2, 5, 10)
print(f'box_1: {box_1}')
print(f'box_2: {box_2}')
