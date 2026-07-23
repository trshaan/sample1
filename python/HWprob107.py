length=int(input("enter the length of the triangle: "))

breadth=int(input("enter the breadth of the traingle: "))
class rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        print("the perimter of the rectangle is", 2*(self.length+self.breadth))
    def area(self):
        print("the area of the rectangle is ",self.length*self.breadth)    
r1=rectangle(length, breadth)
r1.perimeter()
r1.area()        
