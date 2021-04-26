# Receives a sentence
# -> If it starts with a vocal, add 'way' on its end: air = airway
# -> If it starts with other letter: python = ythonpay

sentence = input("Please input your sentence:")
sentence = sentence.lower()
sentence = sentence.split()

new_sentence = ""

for word in sentence:
    word_aux = word
    if word_aux[0] == 'a' or word_aux[0] == 'e' or word_aux[0] == 'i' or word_aux[0] == 'o' or word_aux[0] == 'u':
        new_sentence += word + "way "
    else:
        first_char = word_aux[0]
        word = word[1:] # remove the fisrt character
        word += first_char
        new_sentence += word + "ay "

print(new_sentence) 
