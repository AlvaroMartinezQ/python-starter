# Read the last 5 lines from a given file

fil = open("./statics/tail.txt", "r")
lines = fil.readlines()
last = lines[-5:]
for item in last:
    print(item)
fil.close()
