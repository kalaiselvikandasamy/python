print("Print Alphabets and Letters pattern in python ")
lastNumber = 5
asciiNumber = 65
for i in range(0, lastNumber):
    for j in range(0, i+1):
        character  = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber+=1
    print(" ")
