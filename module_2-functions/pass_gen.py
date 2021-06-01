import random

def create_password(characters):
    length = len(characters)
    out = ''

    for i in range(length):
        out = out + random.choice(characters)

    print(f'Genrated password is : {out}')

if __name__ == "__main__":
    create_password("ABCabc123")
    create_password("!@#$%")
