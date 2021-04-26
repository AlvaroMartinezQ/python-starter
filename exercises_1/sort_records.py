# Receives a list and formats it

def format_sort_records(records):
    for val in records:
        print(val[1], val[0], val[2])

PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]

format_sort_records(PEOPLE)
