import nltk
from nltk.wsd import lesk
nltk.download('wordnet')
from nltk.corpus import wordnet

sentence = input("Enter a sentence: ")
target_word = input("Enter ambiguous word: ")


tokens = sentence.replace('.', '').replace(',', '').split()

sense = lesk(tokens, target_word)

print("Sentence:", sentence)
print("Target Word:", target_word)

if sense:
    print("Sense:", sense.name())
    print("Definition:", sense.definition())
    print("Examples:", sense.examples())
else:
    print("No sense found")
