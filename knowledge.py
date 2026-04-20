from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

sentence = "I went to the bank to deposit money"

words = word_tokenize(sentence)
target_word = "bank"

sense = lesk(words, target_word)

print("Word:", target_word)
print("Sense:", sense)
print("Definition:", sense.definition())
print("Examples:", sense.examples())
