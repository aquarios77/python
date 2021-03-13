class Math2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

    def __str__(self):
        return f'<{self.x}, {self.y}>'