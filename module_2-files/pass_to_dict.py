# Return name and user ID from /etc/passwd file
# name -> field[0]
# UID -> field[2]

PATH = "../statics/etc_passwd.txt"

fil = open(PATH)

users = dict()

line = fil.readline()
while(line):
    words = line.split(":")
    if "#" in words[0]:
        # Section is a comment
        pass
    else:
        name = words[0]
        uid = words[2]
        users[name] = [uid]
    line = fil.readline()

print(users)

fil.close()
