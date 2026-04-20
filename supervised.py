from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

sentences = [
    "I deposited money in the bank",
    "She works at a bank",
    "He withdrew cash from the bank",
    "The bank gives loans",
    "The river bank is beautiful",
    "We sat on the bank of the river",
    "Children played near the river bank",
    "The bank of the river was muddy"
]

labels = ["finance","finance","finance","finance",
          "river","river","river","river"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X, labels)

test = ["He went to the bank to withdraw money"]
X_test = vectorizer.transform(test)

print("Predicted Sense:", model.predict(X_test)[0])
