a = input("Enter Text : ")
s = int(input("Shift : "))
res= " "

for i in a:
    if(i.isupper()):
        res += chr((ord(i)+s-65)%26+65)
    elif(i.islower()):
        res += chr((ord(i)+s-97)%26+97)
print(f"Ciphertext : {res}")
