'''Name : Shreyas Vithal Patil
Roll No : 18CE7006
Batch : C-2
Aim : Write a menu driven program to demonstrate use of dictionary in python
a.Create key/value pair dictionary
b.Update/Concatenate & Delete item of the existing dictionary
c.Find a key and print its value
d.Map 2 list onto dictionary'''
d={}
while(1):
	c=int(input('Enter option\n1.Create key/value pair\n2.Update and delete dictionary item\n3.Find key and print value\n4.Map 2 list onto dictionary & concatenate\n'))
	if(c==1):
		n=int(input('Enter number of elements : '))
		for i in range(n):
			key=input('Enter key : ')
			value=int(input('Enter value : '))
			d[key]=value
		print(d)
	elif(c==2):
		k=input('Enter key of element to update : ')
		val=int(input('Enter the new value : '))
		d[k]=val
		k=input('Enter key of element to delete : ')
		del d[k]
		print(d)
	elif(c==3):
		k=input('Enter key of element to search : ')
		print('The element is',d[k])
	elif(c==4):
		d1={}
		l1,l2=[],[]
		n1=int(input('Enter no : of keys & values : '))
		for x in range(n1):
			l1.append(input('\nEnter key : '))
			l2.append(int(input('Enter value : ')))
		d1=dict(zip(l1,l2))
		print(d1)
		d.update(d1)
		print(d)
	else:
		print('Done')
		break
'''
Output : 
Enter option
1.Create key/value pair
2.Update and delete dictionary item
3.Find key and print value
4.Map 2 list onto dictionary & concatenate
1
Enter number of elements : 4
Enter key : a
Enter value : 1
Enter key : b
Enter value : 2
Enter key : c
Enter value : 3
Enter key : d
Enter value : 4
{'d': 4, 'b': 2, 'c': 3, 'a': 1}
Enter option
1.Create key/value pair
2.Update and delete dictionary item
3.Find key and print value
4.Map 2 list onto dictionary & concatenate
2
Enter key of element to update : c
Enter the new value : 8
Enter key of element to delete : b
{'d': 4, 'c': 8, 'a': 1}
Enter option
1.Create key/value pair
2.Update and delete dictionary item
3.Find key and print value
4.Map 2 list onto dictionary & concatenate
3
Enter key of element to search : a
The element is 1
Enter option
1.Create key/value pair
2.Update and delete dictionary item
3.Find key and print value
4.Map 2 list onto dictionary & concatenate
4
Enter no : of keys & values : 2

Enter key : y
Enter value : 56

Enter key : z
Enter value : 34
{'y': 56, 'z': 34}
{'d': 4, 'a': 1, 'z': 34, 'y': 56, 'c': 8}
Enter option
1.Create key/value pair
2.Update and delete dictionary item
3.Find key and print value
4.Map 2 list onto dictionary & concatenate
5
Done
'''
