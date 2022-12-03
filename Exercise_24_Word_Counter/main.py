import string

sentence=input("Write a sentence, and let us calculate how many times each word appears :D! ")

translator = str.maketrans('', '', string.punctuation)

sentence = sentence.translate(translator).lower()
cut = sentence.split()
which_word = {}
for element in cut:
    if element in which_word:
        which_word[element] +=1
    else:
        which_word[element]=1

print(which_word)