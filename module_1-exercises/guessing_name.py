# Generate a random number
# User has to guess it
# If user gives x number and program has y:
#  -> x>y => system informs smaller number
#  -> x<y => system informs bigger number
#  -> x==y => system informs user has guessed it and ends

import random

def guess():
    print("Guess game!")
    x = random.randint(0,101) # 101 not included
    y = -1
    while x!=y:
        try:
            y = int(input("Enter your number:")) # Parsing from string to int
            if y>x:
                print("Number has to be smaller!")
            elif y<x:
                print("Number has to be bigger!")
            else:
                print("You guessed it, now go to study... :)")
        except ValueError:
            print('Please enter an integer') # Handle the exception

guess()
