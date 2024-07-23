class Calculator:
    def circle(radius):
        print("The formula for perimeter of circle is = 2 * 3.14 * r \nr = radius of circle \nThe perimeter is : ",2 * 3.14 * radius)
        print("The formula for area of circle is = 3.14 * r * r \nr = radius of circle \nThe area is : ",3.14 * radius*radius)
    def square(side):
        print("The formula for perimeter of square is = side*4 \nside = side of a square \nThe perimeter is : ",side*4)
        print("The formula for area of square is = side*2 \nside = side of a square \nThe area is : ",side*2)
    def rectangle(length,breadth):
        print("The formula for perimeter of rectangle is = length*2 + breadth*2 \nlength = longest side of a rectangle\nbreadth = smallest side  of a rectangle\nThe perimeter is : ",length*2 + breadth*2)
        print("The formula for area of rectangle is = length*breadth \nlength = longest side of a rectangle\nbreadth = smallest side  of a rectangle \nThe area is : ",length*breadth)
print("     CIRCLE")
print("     -------")
Calculator.circle(int(input("Enter the radius of the circle: ")))
print("     SQUARE")
print("     -------")
Calculator.square(int(input("Enter the side of the square: ")))
print("     RECTANGLE")
print("     ---------")
Calculator.rectangle(int(input("Enter the length of the rectangle: ")),int(input("Enter the breadth of the rectangle: ")))


