from math1 import Math1
from math2 import Math2
# composition example - NOT inheritance
class MyMath:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m1 = Math1(x, y)
        self.m2 = Math2(x, y)

    def power(self):
         return self.x ** self.y
    
    def add(self):
        return self.m1.add()
    
    def subtract(self):
        return self.m1.subtract()
    
    def multiply(self):
        return self.m2.multiply()
    
    def divide(self):
        return self.m2.divide()
    
    def __str__(self):
        return f'<{self.x}, {self.y}>'