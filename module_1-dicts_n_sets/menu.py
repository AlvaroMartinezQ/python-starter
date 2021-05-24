MENU = {
        'sandwich': 0.99,
        'coffee': 0.87,
        'salad': 3.05
    }

def user_imput():
    print("-- Welcome to the restaurant --")

    total = 0
    option = None
    found = False

    while option != '':
        found = False
        option = input("Please enter your desired meal: ")
        if option != '':
            for name, number in MENU.items(): 
                if name == f'{option}':
                    found = True
                    total += number
                    print(f'{option} costs: {number:.2f}$. Total atm is {total:.2f}$.')

            if not found:
                print (f'Damn! We ran out of fresh {option} today!')

    print(f'Your total to pay is: {total}.')

if __name__ == "__main__":
    user_imput()