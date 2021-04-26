# *args and **kwargs

def printValues(a, *args, **kwargs):
    print(a)

    for(arg in args):
        print(arg)

    for(kwarg in kwargs):
        print(kwarg)

