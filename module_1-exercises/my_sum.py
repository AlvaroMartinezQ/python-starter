# Take n number of numbers to add
# Print the result value

def sumFunct(*args):
    res = 0
    for n in args:
        res+=n
    print(f'Final value: {res}')

sumFunct(1,1,2,2)