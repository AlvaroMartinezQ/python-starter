# script opens a passed file and reads its content
# py read_file.py ./tweetsSamples/N/757313951738761216.txt

fil = input("Please input your file path to read: ")
print(f'Reading data from file: {fil}')

file_object = open(f'{fil}', "r")
file_lines = file_object.readlines()

print(file_lines)
