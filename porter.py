def simple_porter_stem(word):
    word = word.lower()
    if word.startswith("re"):
        word = word[2:]
    elif word.startswith("un"):
        word = word[2:]
    if word.endswith("sses"):
        word = word[:-2]
    elif word.endswith("ies"):
        word = word[:-2]
    elif word.endswith("s") and not word.endswith("ss"):
        word = word[:-1]
    elif word.endswith("ing"):
        word = word[:-3]
    elif word.endswith("ed"):
        word = word[:-2]
    return word

words = ["redoing", "unwanted", "caresses", "running", "cats"]
for w in words:
    print(w, "->", simple_porter_stem(w))
