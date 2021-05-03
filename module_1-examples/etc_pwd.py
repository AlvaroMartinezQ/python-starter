BASH_POS = 6
shells = {}

with open("../statics/etc_passwd.txt") as file:
    for line in file:
        shell = line.strip().split(':')[BASH_POS]
        if shell:
            shells[shell] = shells.get(shell, 0)+1

print(shells)