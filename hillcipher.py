def generate_key_matrix(key):
    key = key.replace("j", "i").lower()  
    key_matrix = ""
    alphabet = "abcdefghiklmnopqrstuvwxyz"  
    for char in key:
        if char not in key_matrix and char in alphabet:
            key_matrix += char
    for char in alphabet:
        if char not in key_matrix:
            key_matrix += char
    return [list(key_matrix[i:i+5]) for i in range(0, 25, 5)]

def process_plaintext(plaintext):
    plaintext = plaintext.replace("j", "i").lower().replace(" ", "")
    digraphs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else "x"
        if a == b:  
            digraphs.append(a + "x")
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    if len(digraphs[-1]) == 1:  
        digraphs[-1] += "x"
    return digraphs
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None
def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    digraphs = process_plaintext(plaintext)
    ciphertext = ""
    for pair in digraphs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:  
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
ciphertext = playfair_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
