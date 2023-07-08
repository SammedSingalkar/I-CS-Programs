L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
plaintext=input("enter the msg : ")
key=int(input("enter the key : "))
ciphertext=''
for c in plaintext.upper():
    if c.isalpha():
        ciphertext += I2L[(L2I[c] + key) % 26]
    else:
        ciphertext += c
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha():
        plaintext2 += I2L[(L2I[c] - key) % 26]
    else:
        plaintext2 += c
print ("The plaintext is : ",plaintext)
print ("Encryption : ",ciphertext)
print ("Decryption : ",plaintext2)