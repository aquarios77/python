from point import Point
from rectangle import Rectangle


p2 = Point(100, 80)
box_2 = Rectangle(p2, 5, 10)
print(f'box_2: {box_2}')

p2.x = 110
print(f'box_2: {box_2}')
print(f'Dist from (0,0): {p2.distance_from_origin()}')
box_2.grow(100, 100)
print(f'box_2: {box_2}')
box_2.move(100, 100)
print(f'box_2: {box_2}')
print(f'Area: {box_2.area()}')
print(f'Perimeter: {box_2.perimeter()}')
box_2.flip()
print(f'box_2: {box_2}')

p3 = Point(200,180)
box_3 = Rectangle(p3, 5, 10)

p4 = Point(700,700)
box_4 = Rectangle(p4, 5, 10)
print(f'box4: {box_4}')

print("Box 2 contains P2: " , box_2.contains(p2))
print("Box 2 contains P3: " , box_2.contains(p3))
print("Box 2 overlaps with Box3: " , box_2.overlap(box_3))
print(box_2.overlap(box_4))