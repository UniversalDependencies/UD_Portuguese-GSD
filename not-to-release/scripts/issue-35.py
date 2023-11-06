import os
import sys
from conllu import Token, parse

# Script arguments

args = sys.argv[1:]

if len(args) != 2 or not os.path.isfile(args[0]):
    print("Usage: fix-enclisis.py <conllu file> <output file>")
    sys.exit()

conllu_file = args[0]
output_file = args[1]

# Conllu sentences

with open(conllu_file, "r") as file:
    sentences = parse(file.read())

print("Conllu file loaded")

# Fix

for sentence in sentences:
    for i in range(len(list(sentence)) - 2):
        first_is_verb = sentence[i]["upostag"] == "VERB"
        second_is_hyphen = (
            sentence[i + 1]["form"] == "-" and sentence[i + 1]["upos"] == "PUNCT"
        )
        third_is_pron = sentence[i + 2]["upos"] == "PRON"
        first_is_head = sentence[i + 2]["head"] == sentence[i]["id"]

        if first_is_verb and second_is_hyphen and third_is_pron and first_is_head:
            sentence[i + 2]["id"] = sentence[i + 1]["id"]
            sentence[i + 1] = sentence[i].copy()

            misc = dict()
            if (
                sentence[i + 2]["misc"] is not None
                and "SpaceAfter" in sentence[i + 2]["misc"]
            ):
                misc["SpaceAfter"] = sentence[i + 2]["misc"]["SpaceAfter"]
                del sentence[i + 2]["misc"]["SpaceAfter"]

            sentence[i] = Token(
                id=(sentence[i]["id"], "-", sentence[i + 2]["id"]),
                form=sentence[i]["form"] + "-" + sentence[i + 2]["form"],
                lemma=None,
                upos=None,
                xpos=None,
                feats=None,
                head=None,
                deprel=None,
                deps=None,
                misc=misc,
            )

            last_id = sentence[i + 2]["id"]

            for j in range(0, len(list(sentence))):
                ids = [sentence[j]["id"], sentence[j]["head"]]

                for k in range(2):
                    id = ids[k]
                    if type(id) is tuple:
                        if id[0] > last_id:
                            ids[k] = (id[0] - 1, id[1], id[2])
                        if ids[k][2] > last_id:
                            ids[k] = (ids[k][0], ids[k][1], ids[k][2] - 1)
                    elif type(id) is int and id > last_id:
                        ids[k] -= 1

                sentence[j]["id"] = ids[0]
                sentence[j]["head"] = ids[1]


print("Fixed")

# Output

with open(output_file, "w") as file:
    file.writelines(sentence.serialize() for sentence in sentences)

print(f"Written to {output_file}")
