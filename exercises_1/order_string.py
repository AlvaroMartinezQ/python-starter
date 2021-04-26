# Receives a sentence
# Returns all words ordered and the longest word

sentence = input("Please input your sentence: ")
sentence = sentence.lower()
sentence = sentence.split()

longest_word = ""

sentence.sort()

for word in sentence:
    if len(word) > len(longest_word):
        longest_word = word

ordered_sentence = ' '.join(sentence)

print(f'Oredred sentence is: [{ordered_sentence}], with the longest word as: {longest_word}' )