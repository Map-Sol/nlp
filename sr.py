import nltk
from nltk import CFG
from nltk.parse import ShiftReduceParser

g = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> V NP
DT -> 'the'
NN -> 'boy' | 'ball'
V -> 'hit'
""")

p = ShiftReduceParser(g)
s = "the boy hit the ball".split()

print("{:<5} {:<30} {:<30} {:<10}".format("steps","Stack", "Input", "Action"))
print("-"*80)

stk = []
inp = s[:]
steps=1

for w in s:
    stk.append(w)
    inp.pop(0)
    print("{:<5} {:<30} {:<30} {:<10}".format(steps," ".join(stk), " ".join(inp), "SHIFT"))
    steps+=1
    
print("{:<5} {:<30} {:<30} {:<10}".format(steps," ".join(stk), " ".join(inp), "reduce"))

for t in p.parse(s):
    t.pretty_print()
