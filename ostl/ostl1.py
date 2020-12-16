'''
Name : Shreyas Vithal Patil
Roll No : 18CE7006
Batch : C-2
Aim : Write a python program to swap two numbers and check if the first number is
positive or negative or zero.
'''
n1=int(input('Enter the number : '))
n2=int(input('Enter the 2nd number : '))
print('Before Swapping - \nn1 =',n1,' n2 =',n2)
temp=n1
n1=n2
n2=temp
print('After Swapping - \nn1 =',n1,' n2 =',n2)
if n2>0:
    print('The number is positive')
elif n2==0:
    print('The number is 0')
else:
    print('The number is negative')
'''Output : 
Enter the number : 3
Enter the 2nd number : 4
Before Swapping - 
n1 = 3  n2 = 4
After Swapping - 
n1 = 4  n2 = 3
The number is positive '''
