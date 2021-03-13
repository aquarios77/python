class Rectangle:
    
    def __init__(self, pos, w, h): # a reference to class point is given which is "pos"
        self.corner = pos # pos is meant as a reference to a object of class Point thus creating aggregation
        self.width = w
        self.height = h

    def __str__(self):
        return f'({self.corner}, {self.width}, {self.height})'
