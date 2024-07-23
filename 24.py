'''
    24. Write a Python program to get the class name of an instance in Python.
'''

import itertools
x = itertools.cycle('ABCD')
print(type(x).__name__)




# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def displayEmployee(self):
#         print(f"name : {self.name}\nsalary : {self.salary}")
# emp1 = Employee("Shreya",98000)
# emp2 = Employee("megha",95000)
# emp1.displayEmployee()
# emp2.displayEmployee()
