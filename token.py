import re

text=input("enter the text for tokenisation")
word=re.findall(r'\b\w+\b',text)
sentence=re.split(r'[.!?]+',text)
sentence=[s.strip() for s in sentence if s.strip()]
print(sentence)
print("\n")
print(word)
