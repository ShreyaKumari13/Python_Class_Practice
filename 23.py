'''
    23. Write a Python class named Circle constructed by a radius and two methods which
         will compute the area and the perimeter of a circle.
'''
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        print(2*3.14*self.radius)
    def area(self):
        print(3.14*(self.radius^2))
a = Circle(int(input("Enter the radius: ")))
a.perimeter()
a.area()