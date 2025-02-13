def mono(plain,key):
	plain.lower()
	enc=""
	for ch in plain:
		if ch.isalpha():
			enc+=key[ord(ch)-97]
	return enc

def decrypt(enc,key):
	dec=""
	for ch in enc:
		for i,chs in enumerate(key):
			if ch==chs:
				dec+=chr(ord('a')+i)
	return dec

plain=input("plain : ")
y=input("keytext : ")
key=y.upper()

for i in range(26):
	ch=chr(ord('A')+i)
	if ch not in key:
		key+=ch
print("key : ",key)
enc=mono(plain,key)
dec=decrypt(enc,key)
print(enc)
print(dec)
