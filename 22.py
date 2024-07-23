'''
    22. Write a Python class named Rectangle constructed by a length and width 
        and a method which will compute the area of a rectangle.
'''
class Rectangle:
    def __init__(self,leng,brea):
        self.leng = leng
        self.brea = brea
    def area(self):
        print(self.leng*self.brea)    
a = Rectangle(5,3)
a.area()