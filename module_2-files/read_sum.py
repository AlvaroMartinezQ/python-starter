fil = open("./statics/read_sum.txt", "r")

add = 0

line = fil.readline()
while line:
    words = line.split(" ")
    words.remove
    for word in words:
        # Clean the string
        word = word.replace('.', ' ')
        word = word.replace(',', ' ')
        
        try:
            number = int(word)
            add += number
        except ValueError:
            pass

    line = fil.readline()

print(f'Sum of all numbers found in file is: {add}')

fil.close()
