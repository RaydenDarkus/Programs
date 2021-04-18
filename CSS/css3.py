#Diffie-Hellman Exchange Key Algorithm
import random

n,g=[int(x) for x in input("Enter public keys of both Alice and Bob n,g: ").split(' ')]
print("Public key for Alice = ",n,"\nPublic key for Bob = ",g)
x = random.randint(0,9)
y = random.randint(0,9)
#print("Private keys of Alice = ",x,"\nPrivate key for Bob = ",y)
A = g**x % n
B = g**y % n
print("Alice receives public key = ",B,"\nBob receives public key = ",A)
k1 = B**x % n
k2 = A**y % n
print("Symmetric key for Alice = ",k1,"\nSymmetric key for Bob = ",k2)
if k1 == k2:
    print("The shared secret key is ",k1)

"""
Output
Enter public keys of both Alice and Bob n,g: 23 9
Public key for Alice =  23 
Public key for Bob =  9
Alice receives public key =  8 
Bob receives public key =  8
Symmetric key for Alice =  16 
Symmetric key for Bob =  16
The shared secret key is  16
"""