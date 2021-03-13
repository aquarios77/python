class Math1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def add(self):
        return self.x + self.y
 
    def subtract(self):
        return self.x - self.y

    def __str__(self):
        return f'<{self.x}, {self.y}>'