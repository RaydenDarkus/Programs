'''
Name : Shreyas Vithal Patil
Roll No : 18CE7006
Batch : C-2
Aim : Write a menu driven python program to check if number and string palindrome
and find the factorial of the input number
'''
while(1):
    n=int(input('Enter the option \n1.Palindrome\n2.Factorial\n'))
    if(n==1):
        x=input('Enter the string : ')
        if(x==x[::-1]):
            print('Palindrome')
        else:
            print('Not Palindrome')
        break
    elif(n==2):
        x=int(input('Enter a number : '))
        s=1
        for i in range(1,x+1):
            s=s*i
        print(x,'! = ',s)
        break
''' Output 
Enter the option 
1.Palindrome
2.Factorial
2
Enter a number : 5
5 ! =  120

Enter the option 
1.Palindrome
2.Factorial
1
Enter the string : level
Palindrome ''' 
