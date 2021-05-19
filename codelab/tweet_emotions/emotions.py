"""
    Script determines if a tweet is positive or not
    It uses a simple algorithm for this:
        +1 if a word is positive
        -1 if a word is negative
        If the final score is:
            > 0 then tweet is positive
            < 0 then tweet is negative
            == 0 then tweet is neutral
    This checks are made consuming the file lex_es.txt
    Note that these expressions are measured in spanish
"""

import argparse, os, re

# Local
import utils

def emotions():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--source", required=True, help="Folder where script should begin")
    ap.add_argument("-l", "--lex", required=True, help="Lexic to use")
    ap.add_argument("-r", "--report", help="Store report operations in JSON file format. Use as: [name_of_your_file].json")
    args = ap.parse_args()
    src_folder = args.source
    lex_file = args.lex
    report_file = args.report

    positive = []
    negative = []

    pattern = r'[\n\t]' # regex

    file_object = open(f'{lex_file}', "r")
    for line in file_object:
        w = str(line)
        if 'positive' in w:
            w = w.replace('positive', '')
            w = re.sub(pattern, '', w)
            positive.append(w)
        elif 'negative' in w:
            w = w.replace('negative', '')
            w = re.sub(pattern, '', w)
            negative.append(w)
        else:
            pass

    total_words = 0
    total_positive = 0
    total_negative = 0

    files = os.listdir(src_folder)
    for fil_path in files:
        data = utils.read_file(src_folder + fil_path)
        
        data = str(data)
        words = utils.tokenize_str(data)
        
        words = utils.rm_hashtags(data)
        
        words = utils.rm_mentions(words)

        words_arr = words.split(" ")
        for word in words_arr:
            if word in positive:
                total_positive += 1
            elif word in negative:
                total_negative += 1
            total_words += 1

    print(f'Scanned a total of {total_words}. {total_positive} were positive, {total_negative} were negative.')

if __name__ == '__main__':
    emotions()
