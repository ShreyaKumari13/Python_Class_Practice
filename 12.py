'''
    12. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. 
        Print all the attributes of student1, student2 instances with their values in the given format.
'''
# class Student:
#     pass

# student1 = Student()
# student2 = Student()
# student1.student_id = 25
# student2.student_id = 50
# student1.student_name = "Shreya"
# student2.student_name = "Shruti"
# students = [student1,student2]
# for studentinfo in students:
#     for attr in studentinfo.__dict__:
#         print(f'{attr} --> {getattr(studentinfo, attr)}')


class Student:
    def __init__(self,student_id,student_name):
        self.student_id = student_id
        self.student_name = student_name
    def display():
        print(f"student_id : {self.student_id}\nstudent_name : {self.student_name}")
student1 = Student(45,"shreya")
student2 = Student(5,"shruti")
Student.display()
# print(student1.student_id)
# print(student1.student_name)