# class Person:
#     def __init__(self,first_name,surname,age):
#         self.first_name = first_name
#         self.surname = surname
#         self.age = age

#     def __repr__(self):
#         return f'Person(first_name = {self.first_name},surname = {self.surname},age = {self.age})'
    
#     # def __lt__(self,other):
#     #     return self.age < other.age  ## babu bhaiya yeh samjh le
# data = [
#     {'first_name':"John", 'surname':'Smith', 'age':13},
#     {'first_name':"Anne", 'surname':'McNell', 'age':11},
#     {'first_name':'Mary', 'surname': 'Brown', 'age':14}
# ]

# for i in data:
#     a = Person(**i)
#     print(a)

for i in range(1,13):
    a = open(f"{i}.py","w")
    a.write("'''\n\n'''")
    a.close()