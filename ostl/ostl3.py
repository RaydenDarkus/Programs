'''
   NAME: Shreyas Vithal Patil
   ROLL_NO: 18CE7006
   BATCH: C-2
   AIM: Write a menu driven program to demonstrate use
	of list in python.
	a. Put even and odd elements into two different
	   lists.
	b. Merge and sort the two list.
	c. Update first element with X value and delete
	   the middle element of list.
	d. Find max and min element from the list.
	e. Add N names into the existing number list and
	   check if word python is present in list.
'''  
while(1):
	print("\nEnter a choice")
	print("1)Put odd and even elements in different lists")
	print("2)Merge and sort the two lists")
	print("3)Update first element with X value and delete middle element of list")
	print("4)Find min and max element from the list")
	print('5)Add N elements into list and check if word "PYTHON" is present in it')
	print("6)Exit")
	c=int(input())
	if(c==1):	
		n=int(input("Enter number of elements: "))
		odd=[]
		even=[]
		for i in range(0,n):
			e=int(input("Enter element: "))
			if(e%2==0):
				even.append(e)
			else:
				odd.append(e)
		print("\nODD: ",odd)
		print("EVEN: ",even)
	elif(c==2):
		l=odd+even
		print("MERGED LIST(before sorting): ",l)
		l.sort()
		print("MERGED LIST(after sorting): ",l)
	elif(c==3):
		n=int(input("Enter a value: "))
		l[0]=n
		l.pop(len(l)//2)
		print(l)
	elif(c==4):
		print("MAX element: ",max(l))
		print("MIN element: ",min(l))
	elif(c==5):
		n=int(input("Enter no.of names: "))
		for i in range(0,n):
			name=input("Enter name: ")
			l.append(name)
		print("\nLIST: ",l)
		for i in l:
			if(i=="PYTHON"):
				print("PYTHON found")
				break
		if(i!="PYTHON"):
			print("PYTHON not found")
	else:
		break
			
'''
OUTPUT
Enter a choice
1)Put odd and even elements in different lists
2)Merge and sort the two lists
3)Update first element with X value and delete middle element of list
4)Find min and max element from the list
5)Add N elements into list and check if word "PYTHON" is present in it
6)Exit
1
Enter number of elements: 5
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5

ODD:  [1, 3, 5]
EVEN:  [2, 4]

Enter a choice
1)Put odd and even elements in different lists
2)Merge and sort the two lists
3)Update first element with X value and delete middle element of list
4)Find min and max element from the list
5)Add N elements into list and check if word "PYTHON" is present in it
6)Exit
2
MERGED LIST(before sorting):  [1, 3, 5, 2, 4]
MERGED LIST(after sorting):  [1, 2, 3, 4, 5]

Enter a choice
1)Put odd and even elements in different lists
2)Merge and sort the two lists
3)Update first element with X value and delete middle element of list
4)Find min and max element from the list
5)Add N elements into list and check if word "PYTHON" is present in it
6)Exit
3
Enter a value: 0
[0, 2, 4, 5]

Enter a choice
1)Put odd and even elements in different lists
2)Merge and sort the two lists
3)Update first element with X value and delete middle element of list
4)Find min and max element from the list
5)Add N elements into list and check if word "PYTHON" is present in it
6)Exit
4
MAX element:  5
MIN element:  0

Enter a choice
1)Put odd and even elements in different lists
2)Merge and sort the two lists
3)Update first element with X value and delete middle element of list
4)Find min and max element from the list
5)Add N elements into list and check if word "PYTHON" is present in it
6)Exit
5
Enter no.of names: 3
Enter name: JAVA
Enter name: PYTHON
Enter name: C

LIST:  [0, 2, 4, 5, 'JAVA', 'PYTHON', 'C']
PYTHON found

Enter a choice
1)Put odd and even elements in different lists
2)Merge and sort the two lists
3)Update first element with X value and delete middle element of list
4)Find min and max element from the list
5)Add N elements into list and check if word "PYTHON" is present in it
6)Exit
6
'''			
