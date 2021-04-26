# User enters as many races as he/she wants
# Program returns the media of the times and the number of races

races = 0
timings = []
media = 0

print("Please enter your race timings (minutes) separated by spaces and then press enter.")

timings = input()

for time in timings:
    if time == ' ': 
        pass
    else:
        try:
            val = int(time) # Parsing
            media+=val
            races+=1
        except ValueError:
            print("A value entered in not an integer. Therefore it won't be used.") # Handle the exception

calculated_media = media / races

print(f"Your media is: {calculated_media}, in a total of {races} races.")
