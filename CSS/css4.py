#MD-5 and SHA-1 protocol analysis
import hashlib

str = input("Enter the string : ")

#MD5

result = hashlib.md5(str.encode())
print("The hexadecimal equivalent of MD5 is: ",result.hexdigest())

#SHA1

result1 = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ",result1.hexdigest())

"""
Output : 

Enter the string : GeeksforGeeks
The hexadecimal equivalent of MD5 is:  f1e069787ece74531d112559945c6871
The hexadecimal equivalent of SHA1 is :  4175a37afd561152fb60c305d4fa6026b7e79856

"""