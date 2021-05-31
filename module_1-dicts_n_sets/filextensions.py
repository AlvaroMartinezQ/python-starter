# Script return a dict of all file extensions in a given directory
# It does not iterate though subdirectories

import os

def dictdir(path):
    print(f'Checking -> {path}')
    exts = dict()
    dirs = os.listdir(path)
    for val in dirs:
        if "." in val:
            extension = val.split(".")
            if not extension[1] in exts:
                aux = extension[1]
                exts[f'{aux}'] = '1'
            else:
                update = exts.get(extension[1])
                update = int(update) + 1
                up_dict = {f'{extension[1]}':update}
                exts.update(up_dict)

    print(f'File extensions are: {exts}')
    return exts

if __name__ == "__main__":
    dictdir("../")
    dictdir(".")
