import random  # Importing the random module for generating random numbers

# Taking user input and converting each character to an 8-bit binary representation
s = input("Enter a string : ")
result = ''.join(format(ord(i), '08b') for i in s)
answer = ""

# Removing every 8th bit from the binary string to introduce randomness
for i in range(len(result)):
    if (i % 8 != 0):  # Skips every 8th bit
        answer += result[i]

# Splitting the modified binary string into two equal halves
l = int(len(answer) / 2)
left = answer[:l]
right = answer[l:]

# A predefined list of bit-shift values used for transformations
lt = [2, 3, 6, 7, 1, 6, 5, 9]
keys = []  # List to store generated encryption keys

# Loop to generate 8 different encryption keys
for i in range(0, 8):
    newKey = ""
    newAnswer = ""

    # Convert left and right halves from binary to integer and apply bitwise left shift
    nl = int(left, 2)
    nl = bin(nl << lt[i])  # Left shift operation on left half
    num = 2 + lt[i]  # Offset for slicing

    nr = int(right, 2)
    nr = bin(nr << lt[i])  # Left shift operation on right half
    num = 2 + lt[i]  # Offset for slicing

    # Concatenating transformed right and left halves to form an intermediate key
    newKey = nr[num:] + nl[num:]

    rm = []  # List to store random positions for removing bits
    while (len(rm) != 8):  # Ensuring exactly 8 bits are removed
        r = random.randint(0, len(newKey) - 1)  # Selecting a random index
        if (r not in rm):
            rm.append(r)  # Storing unique random positions

    # Creating the final key by excluding randomly selected bits
    for i in range(len(newKey)):
        if (i not in rm):
            newAnswer += newKey[i]

    keys.append(newAnswer)  # Storing the generated key

# Printing the generated encryption keys
for i in range(0, len(keys)):
    print("Key ", i + 1, " = ", keys[i])
