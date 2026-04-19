import nltk
from nltk import CFG
from nltk.parse import ShiftReduceParser

g = CFG.fromstring("""
S  -> NP VP
NP -> DT NN
VP -> V NP
DT -> 'the'
NN -> 'boy' | 'ball'
V  -> 'hit'
""")

p = ShiftReduceParser(g, trace=2)

s = "the boy hit the ball".split()


for tree in p.parse(s):
    print("\nFinal Parse Tree:\n")
    tree.pretty_print()
