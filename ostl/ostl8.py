'''Aim: Write menu driven program to implement stack, queue and linklist.'''

'''Stack'''
s=[]
length=int(input('Enter length of stack : '))
while(1):
	c=int(input('1.Push\n2.Pop\n3.Display\n'))
	if(c==1):
		if(len(s)<length):
			s.append(int(input('Enter value to push : ')))
		else:
			print('Stack Overflow')
	elif(c==2):
		if(len(s)==0):
			print('Stack Underflow')
		else:
			s.pop()
	elif(c==3):
		print(s)
	else:
		print('Done')
		break
'''Output
Enter length of stack : 4
1.Push
2.Pop
3.Display
1
Enter value to push : 4
1.Push
2.Pop
3.Display
1
Enter value to push : 8
1.Push
2.Pop
3.Display
1
Enter value to push : 5
1.Push
2.Pop
3.Display
3
[4, 8, 5]
1.Push
2.Pop
3.Display
2
1.Push
2.Pop
3.Display
3
[4, 8]
1.Push
2.Pop
3.Display
4                           
Done
'''
