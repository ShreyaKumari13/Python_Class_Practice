class Person:
    ''' person details'''

    def __init__(self,first_name,age,caste):
        self.first_name = first_name
        self.age = age
        self.caste = caste
z,t,g = [],[],[]
for i in range(int(input("enter the no of names you want to enter :"))):
    a,b,c = input("ENter the details name,age,caste ('shruti',14,'rajaput'): ").split()
    y = Person(a,int(b),c)
    z.append(y.first_name)
    t.append(y.age)
    g.append(y.caste)
for i,j,k in zip(z,t,g):
    print("Name =",i,", age =",j,", caste =",k)
