import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser

grammar = DependencyGrammar.fromstring("""
'hit' -> 'boy' | 'ball'
'boy' -> 'the'
'ball' -> 'the'
""")

parser = ProjectiveDependencyParser(grammar)

sentence = "the boy hit the ball".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
