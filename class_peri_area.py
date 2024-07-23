class Calculator:
    def __init__(self,radius,side,length,breadth):
        self.radius = radius
        self.side = side
        self.length = length
        self.breadth = breadth
    def peri_area(self):
        print(f"The perimeter of the circle is: {self.radius*2*3.14}\nThe area of the circle is: {self.radius*self.radius*3.14}")
    def square(self):
        print(f"The perimeter of the square is: {self.side*4}\nThe area of the square is:{self.side*2}")
    def rectangle(self):
        print(f"The perimeter of the rectangle is: {self.length*2+self.breadth*2}\nThe area of the rectangle is:{self.length*self.breadth}")
a = Calculator(2,3,5,4)
a.square()
a.rectangle()

# class Calculator:
#     def __init__(self,radius,side,length,breadth):
#         self.radius = radius
#         self.side = side
#         self.length = length
#         self.breadth = breadth
#     def peri_area(self):
#         print(f"The perimeter of the circle is: {self.radius*2*3.14}\nThe area of the circle is: {self.radius*self.radius*3.14}")
#         print(f"The perimeter of the square is: {self.side*4}\nThe area of the square is:{self.side*2}")
#         print(f"The perimeter of the rectangle is: {self.length*2+self.breadth*2}\nThe area of the rectangle is:{self.length*self.breadth}")
# a = Calculator(2,3,5,4)
# a.peri_area()