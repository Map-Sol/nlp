import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> D N | D N PP | 'ravi' | 'raju'
VP -> V NP | V NP PP
PP -> P NP
D -> 'the' | 'my'
P -> 'in' | 'with'
N -> 'raju' | 'ravi'
V -> 'playing'
""")

parser = ChartParser(grammar)

sentence = "ravi playing with the raju".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
