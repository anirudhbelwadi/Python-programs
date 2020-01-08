class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calcarea(self):
        return self.length*self.width
a=float(input("Enter length = "))
b=float(input("Enter breadth = "))
rect1=Rectangle(a,b)
print("Area of rectangle:",rect1.calcarea())
