import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser

grammar = DependencyGrammar.fromstring("""
'hit' -> 'boy' | 'ball' | 'with'
'boy' -> 'the'
'ball' -> 'the'
'with' -> 'bat'
'bat' -> 'the'
""")

parser = ProjectiveDependencyParser(grammar)

sentence = "the boy hit the ball with the bat".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
