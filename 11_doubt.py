'''
    11. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. 
        Create a function to display the entire attribute and their values in Student class.
'''
class Student:
    student_id = 18
    student_name = "shreya"
    def display():
        print(f"student_id : {Student.student_id}\nstudent_name : {Student.student_name}")
Student.display()