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

    Examples:
        msh> py .\emotions.py -s ./tweetsSamples/N/ -l ./lex/lex_es.txt -r ./report.json
        msh> py .\emotions.py -s ./tweetsSamples/P/ -l ./lex/lex_es.txt -r ./report.json
        msh> py .\emotions.py -s ./tweetsSamples/NEU/ -l ./lex/lex_es.txt -r ./report.json
        msh> py .\emotions.py -s ./tweetsSamples/NONE/ -l ./lex/lex_es.txt -r ./report.json
"""

import argparse, os, re, json

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

    total_tweets = 0
    total_words = 0
    total_positive = 0
    total_negative = 0
    total_neutral = 0
    total_none = 0

    files = os.listdir(src_folder)
    for fil_path in files:
        data = utils.read_file(src_folder + fil_path)
        
        data = str(data)
        words = utils.tokenize_str(data)
        
        words = utils.rm_hashtags(data)
        
        words = utils.rm_mentions(words)

        words_arr = words.split(" ")

        score = 0
        in_lists = False
        for word in words_arr:
            total_words += 1
            if word in positive:
                score += 1
                in_lists = True
            elif word in negative:
                score -= 1
                in_lists = True
        
        if in_lists:
            if score < 0:
                total_negative += 1
            elif score > 0:
                total_positive += 1
            elif score == 0:
                total_neutral += 0
        else:
            total_none += 1

        total_tweets += 1

    print(f"Scanned a total of {total_words} words in {total_tweets} tweets.\n{total_positive} were positive, {total_negative} were negative, {total_neutral} were neutral and {total_none} couldn't be determined.")

    if report_file != None:
        result = dict()
        result['path'] = src_folder
        result['scanned_tweets'] = total_tweets
        result['scanned_words'] = total_words
        result['positive'] = total_positive
        result['negative'] = total_negative
        result['neutral'] = total_neutral
        result['undefined'] = total_none
        
        with open(report_file, 'w') as outfile:
            json.dump(result, outfile)

if __name__ == '__main__':
    emotions()
