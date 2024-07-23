'''
    9. Write a Python class named Student with two attributes student_name, marks. 
    Modify the attribute values of the said class and print the original and modified values of the said attributes.
'''
class Student:
    student_name = "shreya"
    marks = 89
print(f"Student Name: {getattr(Student,'student_name')}")
print(f"marks : {getattr(Student,'marks')}")
setattr(Student,"student_name","shruti")
setattr(Student,"marks",95)
print(f"Student_name : {getattr(Student,'student_name')}")
print(f"marks : {getattr(Student,'marks')}")
