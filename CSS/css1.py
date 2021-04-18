#Additive Cipher + Transposition Cipher
import math

plaintext = input("Enter the plaintext : ")
ac = ""
key1 = int(input("Enter the key for additve cipher : "))
for i in range(len(plaintext)):
    if(plaintext[i].isupper()):
        ac += chr((ord(plaintext[i]) + key1 - 65) % 26 + 65)
    if(plaintext[i].islower()):
        ac += chr((ord(plaintext[i]) + key1 - 97) % 26 + 97)
    elif(plaintext[i]==" " or plaintext[i]=="."):
        ac += chr(ord(plaintext[i]))
print("Addictive Cipher Encryption : " + ac)
tc = ""
keyword = input("Enter the key word for transposition cipher : ")
keyword = keyword.upper()
msg = list(ac)
msglen = float(len(ac))
k2 = sorted(list(keyword))
col = len(keyword)
row = int(math.ceil(msglen/col))
fill_null = int((row * col) - msglen) 
msg.extend(" " * fill_null) 
k = 0
matrix = [msg[i:i+col] for i in range(0,len(msg),col)]
""""for i in range(row):
    for j in range(col):
        print(matrix[i][j],end= " ")
    print("\n")"""
for i in range(col):
    cid = keyword.index(k2[k])
    tc += "".join(row[cid] for row in matrix)
    k += 1
print("Columnar Transposition Cipher Encryption : " + tc)
dtc = ""
k = 0
msg = list(tc)
msglen = float(len(tc))
msdidx = 0
row = int(math.ceil(msglen/col))
dec_c = []
for i in range(row):
    dec_c += [[None] * col]
for i in range(col):
    cid = keyword.index(k2[k])
    for j in range(row):
        dec_c[j][cid] = msg[msdidx]
        msdidx += 1
    k += 1
dtc = "".join(sum(dec_c,[]))
print("Columnar Transposition Cipher Decryption : " + dtc)
dac = ""
for i in range(len(dtc)):
    if(dtc[i].isupper()):
        dac += chr((ord(dtc[i]) - key1 - 65) % 26 + 65)
    if(dtc[i].islower()):
        dac += chr((ord(dtc[i]) - key1 - 97) % 26 + 97)
    elif(dtc[i]==" " or dtc[i]=="."):
        dac += chr(ord(dtc[i]))
print("Addictive Cipher Decryption : " + dac)
