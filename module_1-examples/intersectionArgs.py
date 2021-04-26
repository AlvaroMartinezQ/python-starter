# values from first sequence in all the others

def funct(*args, **kwargs):
    check = args
    res = []
    for kwarg in kwargs:
        print("Checking key in kwargs: " + kwarg)
        for key, val in kwargs.items():
            if not val in res and val in check:
                res.append(val)

    print(res)

funct(1, 2, 3, 4, x=1, y=2)