"""NAME: Shreyas Vithal Patil
ROLL_NO: 18CE7006
BATCH: C-2
AIM : Write a program to demonstrate Single and Multiple inheritance in python """

class Person:
    def __init__(self,n,i):
        self.name = n
        self.id = i
    def display(self):
        print("Name : ",self.name,"\nID : ",self.id)
class Student(Person):
    def __init__(self,n,i,s1,s2):
        self.sub1 = s1
        self.sub2 = s2
        super().__init__(n,i)
    def display(self):
        super().display()
        print("Subject 1 marks : ",self.sub1)
        print("Subject 2 marks : ",self.sub2)
class Sports:
    def __init__(self,sm):
        self.smarks = sm
    def printsport(self):
        print("Sports marks : ",self.smarks)
class Result(Student,Sports):
    def __init__(self,n,i,s1,s2,sm1,sman1):
        self.sman = sman1
        Student.__init__(self,n,i,s1,s2)
        Sports.__init__(self,sm1)
    def total(self,a = None, b = None,c = None):
        if a!=None and b!=None and c!=None:
            sum = a+b+c
        else:
            sum = a+b
        print("Total marks : ",sum)
id1 = int(input("Enter ID : "))
name1 = input("Enter name : ")
s1 = int(input("Enter marks of subject1 : "))
s2 = int(input("Enter marks of subject2 : "))
sm1 = int(input("Enter sports marks : "))
spname = input("Enter sport name : ")
r1 = Result(name1,id1,s1,s2,sm1,spname)
print("\nDetails\n")
r1.display()
r1.printsport()
r1.total(s1,s2,sm1)
"""
Enter ID : 34
Enter name : Shr 
Enter marks of subject1 : 78
Enter marks of subject2 : 87
Enter sports marks : 87
Enter sport name : cricket

Details

Name :  Shr 
ID :  34
Subject 1 marks :  78
Subject 2 marks :  87
Sports marks :  87
Total marks :  252
"""
