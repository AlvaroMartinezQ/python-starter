import os

PATH = "./statics/encrypt.txt"
ENCRYPT = "./statics/new_encrypt.txt"

# Delete the file if exists
if os.path.exists(ENCRYPT):
    os.remove(ENCRYPT)

fil = open(PATH)
new_fil = open(ENCRYPT, "a")

line = fil.readline()
while(line):
    new_line = ''
    for character in line:
        number = ord(character)
        number += 1
        new_line = new_line + str(number) + ':'
    
    new_line = new_line + '\n'
    new_fil.write(new_line)
    
    line = fil.readline()

fil.close()
new_fil.close()

# Open the encrypted file and print it
fil = open(ENCRYPT)

line = fil.readline()
while(line):
    new_line = ''
    arr = line.split(':')
    for char in arr:
        if char == '\n':
            pass
        else:
            new_line = new_line + chr(int(char) - 1)

    print(new_line)

    line = fil.readline()
