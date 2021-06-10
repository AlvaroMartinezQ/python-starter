# Simulates zip
def my_zip(*args):

    min_length = min(map (len, args)) # gets the tuple with least values

    result = []

    for i in range(min_length):
        elem = [sequence[i] for sequence in args]
        print(elem)
        result.append(tuple(elem))

    return result

if __name__ == "__main__":
    print(my_zip([10, 20,30], 'abcd'))

