"""NAME: Shreyas Vithal Patil
ROLL_NO: 18CE7006
BATCH: C-2
AIM: Write a menu driven program to demonstrate use of tuples in python. 
a. Add and show N student roll number , name and 3 subject marks in a list of tuples.
b. Display student roll number and marks whoose name is Python.
c. Demonstrate nested tuple and sort nested tuple by name."""

name,roll_no1,marks1 = [],[],[]
student,new,sorting = [],[],[]
n = int(input("Enter the number of students : "))
count = 0
for i in range(0,n):
    name = input("Enter the name : ")
    roll_no = input("Enter the roll no : ")
    for j in range (3):
        marks1.append(input("Enter the marks of the subject : "))
    student = (name,roll_no,marks1)
    new.append(student)
    marks1 = []
print(new)
for i in range(0,n):
    if(new[i][0] == "python"):
        print("name : ",new[i][0])
        print("roll no : ",new[i][1])
        print("marks : ",new[i][2])
        count = 1 
        break
if(count == 0):
    print("python not found")
    print("Before sorting: ",new)
    sorting = new
    sorting.sort()
    print("After sorting : ",sorting)

"""Enter the number of students :2
Enter the name : shr
Enter the roll no : 5
Enter the marks of the subject : 85
Enter the marks of the subject : 78
Enter the marks of the subject : 98
Enter the name : python
Enter the roll no : 6
Enter the marks of the subject : 67
Enter the marks of the subject : 83
Enter the marks of the subject : 64
[('shr', '5', ['85', '78', '98']), ('python', '6', ['67', '83', '64'])]
name :  python
roll no :  6
marks :  ['67', '83', '64']
"""
