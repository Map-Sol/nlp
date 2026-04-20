!python -m spacy download en_core_web_sm
import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

sentence = "Ram gave Sita a book"

doc = nlp(sentence)

for token in doc:
    if token.pos_ == "VERB":
        print("Predicate:", token.text)
        for child in token.children:
            if child.dep_ in ("nsubj", "dobj", "iobj"):
                print(child.dep_, ":", child.text)
