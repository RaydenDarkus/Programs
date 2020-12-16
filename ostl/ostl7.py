'''Name : Shreyas Vithal Patil
Roll No : 18CE7006
Batch : C/C-2
Aim : Exploring files and directories.
a. Python program to read the content of file and write it in another file.
b. Python program to append data to existing file and then display the entire file.
c. Python program to count number of lines, words and characters in a file.
d. Python program to display file available in current directory.'''
import os
while(1):
	c=int(input('1.Read content of 1 file and copy into another file\n2.Append file and display\n3.Count words/characters/lines in file\n4.Display files in current directory\n5.Exit\n'))
	if(c==1):
		f=open('f1.txt','r')
		print(f.read())
		f.close()
		nf=open('f2.txt','w')
		with open('f1.txt','r') as f:
			nf.write(f.read())
		nf.close()
	elif(c==2):
		s=input('Enter data to append : ')
		f=open('f1.txt','a+')
		f.write(s)
		print(f.read())
		f.close()
	elif(c==3):
		line,char,word=0,0,0
		f=open('f1.txt','r')
		for i in f:
			line+=1
			char+=len(i)
			word+=len(i.split(' '))
		print('The number of lines is :',line)
		print('The number of words is :',word)
		print('The number of characters is :',char)
		f.close()
	elif(c==4):
		files = [f for f in os.listdir('.') if os.path.isfile(f)]
		for f in files:
			print(f)
	else:
		print('Done')
		break
'''
Output : 
student-HP-280-G2-MT% python3 Exp7.py
1.Read content of 1 file and copy into another file
2.Append file and display
3.Count words/characters/lines in file
4.Display files in current directory
5.Exit
1
run faster than the wind

1.Read content of 1 file and copy into another file
2.Append file and display
3.Count words/characters/lines in file
4.Display files in current directory
5.Exit
2
Enter data to append : cathay pacific
run faster than the wind 
cathay pacific 

1.Read content of 1 file and copy into another file
2.Append file and display
3.Count words/characters/lines in file
4.Display files in current directory
5.Exit
3 
The number of lines is : 2
The number of words is : 7
The number of characters is : 39
1.Read content of 1 file and copy into another file
2.Append file and display
3.Count words/characters/lines in file
4.Display files in current directory
5.Exit
4
Exp7.py
Exp2.py
Tup.py
Exp5_2.py
Palindrome.py
Dict.py
Swap.py
Exp6.py
Exp4.py
Exp5.py
f2.txt
Fact.py
Number.py
Exp3.py
f1.txt
1.Read content of 1 file and copy into another file
2.Append file and display
3.Count words/characters/lines in file
4.Display files in current directory
5.Exit
5
Done'''
