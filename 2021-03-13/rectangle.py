class Rectangle:
    
    def __init__(self, pos, w, h): # a reference to class point is given which is "pos"
        import copy
        my_pos = copy.deepcopy(pos)
        self.corner = my_pos # pos is meant as a reference to a object of class Point thus creating aggregation
        self.width = w
        self.height = h

    def __str__(self):
        return f'({self.corner}, {self.width}, {self.height})'
    
    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
        
    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def flip(self):
        self.width , self.height = self.height , self.width
    
    def contains(self, p):
        if (p.x >= self.corner.x and p.x <= self.corner.x + self.width) and (p.y >= self.corner.y and p.y <= self.corner.y + self.height):
            return "YES"
        else:
            return "NO"
        
    def overlap(self, other):
       r1xmi = self.corner.x
       r1xma = self.corner.x + self.width
       r1ymi = self.corner.y
       r1yma = self.corner.y + self.height
       
       r2xmi = other.corner.x
       r2xma = other.corner.x + other.width
       r2ymi = other.corner.y
       r2yma = other.corner.y + other.height
       
       if (r1xmi <= r2xma and r1xma >= r2xmi) and (r1ymi <= r2yma and r1yma >= r2ymi):
             return "YES"
       else:
            return "NO"

        