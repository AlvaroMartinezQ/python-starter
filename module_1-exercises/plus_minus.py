# Receives a list of numbers
# Iterates through the array like: [n1, n2, n3, n4] -> (((n1 - n2) + n3 ) - n4) and returns the result

numbers = input("Please input your numbers separated with spaces: ")

res = 0
count = 0

for num in numbers:
    try:
        if num == ' ':
            pass
        else:
            val = int(num) # Parsing
            if count % 2 != 0:
                res -= val
            else:
                res += val
            count += 1
    except ValueError:
        print("A value entered in not an integer. Therefore it won't be used.") # Handle the exception

print(f'Result is: {res}')
