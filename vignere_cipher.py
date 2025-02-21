def key_cycle(msg,key):
    s=key
    while(len(s)<len(msg)):
        s=s+key
    return s[:len(msg)]

def encrypt(msg,key):
    c=[((ord(msg[i])-ord("A")) + (ord(key[i])-ord("A")))%26 for i in range(len(msg))]
    return "".join(chr(x+ord("A")) for x in c)

def decrypt(msg,key):
    c=[((ord(msg[i])-ord("A")) - (ord(key[i])-ord("A")))%26 for i in range(len(msg))]
    return "".join(chr(x+ord("A")) for x in c)

msg=input("Enter the msg: ").upper().replace(" ","")
key=input("Enter the key: ").upper()
key=key_cycle(msg,key)

cipher=encrypt(msg,key)
print("Ciphertext: ",cipher)

plaintext=decrypt(cipher,key)
print("Plaintext: ",plaintext)