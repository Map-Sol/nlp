
morph_dict = {
    "children": "child",
    "mice": "mouse",
    "cars": "car"
}

word = input("Enter word: ")


if word in morph_dict:
    root = morph_dict[word]
    feature = "irregular (dictionary)"

elif word.endswith("ing"):
    root = word[:-3]
    feature = "continuous"
elif word.endswith("ed"):
    root = word[:-2]
    feature = "past tense"
elif word.endswith("s"):
    root = word[:-1]
    feature = "plural"

else:
    root = word
    feature = "base form"

print("Word   :", word)
print("Root   :", root)
print("Feature:", feature)
