'''
    2. Write a Python program to create a class and display the namespace of the said class.
'''
class Employee:
    pass
    # def __init__(self,business):
    #     self.business = business
for i in Employee.__dict__:
    print(i)