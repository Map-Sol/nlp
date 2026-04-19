from sklearn.linear_model import LogisticRegression

# Training data (slightly improved)
X_train = [
    [1], [1], [1],   # boundary cases
    [0], [0], [0]    # non-boundary
]
y_train = [1, 1, 1, 0, 0, 0]

model = LogisticRegression()
model.fit(X_train, y_train)

print("Model trained successfully\n")

text = input("Enter text: ")
words = text.split()

sentences = [words[0]]

for i in range(1, len(words)):
    prev_word = words[i-1]
    curr_word = words[i]

    # Feature extraction
    has_punct = prev_word[-1] in ".!?"
    is_capital = curr_word[0].isupper()

    feature = 1 if (has_punct and is_capital) else 0

    prediction = model.predict([[feature]])[0]

    if prediction == 1:
        sentences.append(curr_word)
    else:
        sentences[-1] += " " + curr_word

print("\nPredicted Sentences:")
for s in sentences:
    print(s)
