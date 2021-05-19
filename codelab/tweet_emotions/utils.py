# util functions for the development of this project

import re

def read_file(path):
    # print(path)
    file_object = open(f'{path}', "r")
    file_line = file_object.readline()

    return file_line


def to_lower(str_in):
    str_out = str(str_in)
    
    return str_out.lower()


def rm_hashtags(str_in, hashes = False):
    str_inter = str(str_in)
    str_inter = str_inter.split(" ")
    str_out = ''
    for word in str_inter:
        if '#' in word:
            # Maybe store the hashtags for a future hashtag check
            pass
        else:
            str_out += word
            str_out += ' '

    return str_out


def rm_mentions(str_in, names = False):
    str_inter = str(str_in)
    str_inter = str_inter.split(" ")
    str_out = ''
    for word in str_inter:
        if '@' in word:
            # Maybe store the names for a future user check
            pass
        else:
            str_out += word
            str_out += ' '

    return str_out


def rm_points_digits(str_in):
    str_inter = str(str_in)
    str_inter = str_inter.split(" ")
    pattern = r'[0-9,.]'
    str_out = ''
    for word in str_inter:
        mod_word = re.sub(pattern, '', word)
        str_out += mod_word
        str_out += ' '
    
    # print(str_out)
    return str_out


def tokenize_str(str_in):
    arr_out = str_in.split(" ")
    # print(arr_out)
    return arr_out


if __name__ == '__main__':
    # pass
    # rm_hashtags("good morning how are yall #goodmorning")
    rm_mentions("hey wasssup man @alvaro")
    # rm_points_digits("this is a test string ok 1234 wow 1233 2323 yes 2..")
    # tokenize_str("Let's deploy on friday LOL!!")
