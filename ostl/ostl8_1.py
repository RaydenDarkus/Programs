'''Queue'''
q=[]
length=int(input('Enter length of queue : '))
while(1):
	c=int(input('Enter the option\n1.Insert\n2.Delete\n3.Display\n'))
	if(c==1):
		if(len(q)<length):
			q.append(int(input('Enter value to append :')))
		else:
			print('Queue Overflow')
	elif(c==2):
		if(len(q)==0):
			print('Queue Underflow')
		else:
			q.pop(0)
	elif(c==3):
		print(q)
	else:
		print('Done')
		break
'''Output
Enter length of queue : 4
Enter the option
1.Insert
2.Delete
3.Display
1
Enter value to append :6
Enter the option
1.Insert
2.Delete
3.Display
1
Enter value to append :3
Enter the option
1.Insert
2.Delete
3.Display
1
Enter value to append :9
Enter the option
1.Insert
2.Delete
3.Display
3
[6, 3, 9]
Enter the option
1.Insert
2.Delete
3.Display
2
Enter the option
1.Insert
2.Delete
3.Display
2
Enter the option
1.Insert
2.Delete
3.Display
3
[9]
Enter the option
1.Insert
2.Delete
3.Display
4
Done
'''
