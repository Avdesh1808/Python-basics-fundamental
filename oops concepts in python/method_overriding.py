# This is the example of overriding function
class shape:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)# This key is used for overiding the functions from base class into derived class
    def area(self):
        return 3.14*super().area()
class square(shape):
    def __init__(self,side):
        self.side=side
        super().__init__(side,side)
    def area(self):
        return super().area()
        
a=square(2)
print(a.area())
b=circle(3)
print(b.area())