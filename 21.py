'''
    21. Write a Python class which has two methods get_String and print_String. 
        get_String accept a string from the user and print_String print
        the string in upper case
'''
class Upper_case:
    def __init__(self):
        self.s = ""
    def get_String(self):
        self.s = input("Enter the string: ")
    def print_String(self):
        print(self.s.upper())
shame = Upper_case()
shame.get_String()
shame.print_String()
    
# class Upper_case:
#     def __init__(self,s):
#         self.s = s
#     def print_String(self):
#         print(self.s.upper())
# s = Upper_case("shreya")
# s.print_String()
    