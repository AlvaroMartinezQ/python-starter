# util functions for the development of this project

def to_lower(str_in):
    str_out = str(str_in)
    return str_out.lower()

def rm_hashtags(str_in, hashes = False):
    str_inter = str(str_in)
    str_inter = str_inter.split(" ")
    str_out = ''
    for word in str_inter:
        if word[0] == '#':
            # Maybe store the hashtags for a future hashtag check
            pass
        else:
            str_out += word
            str_out += ' '

    # print(str_out)
    return str_out

def rm_mentions(str_in, names = False):
    str_inter = str(str_in)
    str_inter = str_inter.split(" ")
    str_out = ''
    for word in str_inter:
        if word[0] == '@':
            # Maybe store the names for a future user check
            pass
        else:
            str_out += word
            str_out += ' '

    print(str_out)
    return str_out

if __name__ == '__main__':
    pass
    # rm_hashtags("good morning how are yall #goodmorning")
    # rm_mentions("hey wasssup man @alvaro")
