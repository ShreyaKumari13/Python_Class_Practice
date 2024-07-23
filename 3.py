'''
    3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
'''
class Student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks

student1 = Student(1,"shreya",400)
print(student1.__dict__)