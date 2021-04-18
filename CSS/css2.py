#RSA Encryption/Decryption + RSA Digital Signature
import sympy
import math
from sympy.core.numbers import mod_inverse

while(1):
    choice = int(input("Enter the choice : 1.RSA Encryption/Decryption 2.RSA Digital Signature 3.Exit - "))
    if choice == 1:
        p = sympy.randprime(0,100)
        q = sympy.randprime(0,100)
        n = p * q
        phi_n = (p-1) * (q-1)
        e = 2
        while(e<phi_n):
            if(math.gcd(e,phi_n)==1):
                break
            else:
                e += 1
        print( "p = ",p," q = ",q," n = ",n," phi_n =  ",phi_n," e = ",e)
        i = 1
        while(i<100):
            d = ((phi_n * i) + 1)/e
            k = phi_n * i
            if ((k + 1)% e == 0):
                print("i = ",i)
                break
            else:
                i += 1
        print("d = ",int(d),"\nPublic Key = ",e,",",n,"\nPrivate Key = ",int(d),",",n)
        PT = int(input("Enter the plaintext message : "))
        CT = (PT**e)%n
        print("CT = ",CT)
        print("PT = ",PT)
    elif choice == 2:
        p,q=[int(x) for x in input("Enter values of p,q: ").split(' ')]
        if(sympy.isprime(p) and sympy.isprime(q)):
            print("p: ",p,"q : ",q)
            n=p*q
            phi_n=(p-1)*(q-1)
            e=int(input("\nEnter Value of e: "))
            if(e>phi_n or e<1):
                print("Value must be 1<e<",phi_n)
            elif(math.gcd(e,phi_n)!=1):
                print("GCD({},{})!=1".format(e,phi_n))
                print("e and (p-1)(q-1) must be coprime")
            else:
                d=mod_inverse(e,phi_n)
                print("Public Key:({},{})".format(e,n))
                print("Private Key:({},{})".format(d,n))
                M=int(input("\nEnter Plaintext: "))
                Y=(M**d)%n
                print("Signed Message (M,Y): ({},{}) ".format(M,Y))
                Z=(Y**e)%n
                print("M:{} Z:{}".format(M,Z))
                if(M==Z):
                    print("Signature Valid")
                else:
                    print("Signature Invalid")
    else:
        break
"""
OUTPUT
Enter the choice : 1.RSA Encryption/Decryption 2.RSA Digital Signature 3.Exit - 1
p =  61  q =  13  n =  793  phi_n =   720  e =  7
i =  1
d =  103 
Public Key =  7 , 793 
Private Key =  103 , 793
Enter the plaintext message : 12
CT =  103
PT =  12
Enter the choice : 1.RSA Encryption/Decryption 2.RSA Digital Signature 3.Exit - 2
Enter the choice : 1.RSA Encryption/Decryption 2.RSA Digital Signature 3.Exit - 2
Enter values of p,q: 7 13
p:  7 q :  13

Enter Value of e: 5
Public Key:(5,91)
Private Key:(29,91)

Enter Plaintext: 10
Signed Message (M,Y): (10,82) 
M:10 Z:10
Signature Valid
"""