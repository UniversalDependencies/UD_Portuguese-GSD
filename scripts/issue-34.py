import os
import sys
from depedit import DepEdit

# script arguments

args = sys.argv[1:]

if len(args) != 2 or not os.path.isfile(args[0]):
    print("Usage: fix-num-lemma.py <conllu file> <output file>")
    sys.exit()

conllu_file = args[0]
output_file = args[1]

# conllu sentences

with open(conllu_file, "r") as file:
    sentences = file.read()

print("Conllu file loaded")

# Fix

d = DepEdit()
d.add_transformation('pos=/NUM/&lemma=/_/&form=/^([0-9\,]+)$/\tnone\t#1:lemma=$1')

result = d.run_depedit(sentences)
result += "\n\n"

print("Fixed")

# Output

with open(output_file, "w") as file:
    file.write(result)

print(f"Written to {output_file}")
