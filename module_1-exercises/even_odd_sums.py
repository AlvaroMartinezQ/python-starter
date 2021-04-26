# Receives a list of numbers
# Returns the addition of odds + odds and evens + evens

numbers = input("Please input your numbers separated with spaces: ")

odds = 0
evens = 0

for num in numbers:
    try:
        if num == ' ':
            pass
        else:
            val = int(num) # Parsing
            if val % 2 == 0:
                evens += val
            else:
                odds += val
    except ValueError:
        print("A value entered in not an integer. Therefore it won't be used.") # Handle the exception

print(f'Odds sum: {odds}, evens sum: {evens}')
