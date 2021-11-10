import sys
import udapi

def correctDet(file):

    doc = udapi.Document(file)
    for n in doc.nodes:
        if n.form.lower() == "a" and n.upos == "DET" and n.deprel == "det" and n.parent.upos in ["NOUN", "PROPN"] and not n.feats:
            n.feats["Definite"] = "Def";
            n.feats["Gender"] = "Fem";
            n.feats["Number"] = "Sing";
            n.feats["PronType"]= "Art"
        
        if n.form.lower() == "as" and n.upos == "DET" and n.deprel == "det" and n.parent.upos in ["NOUN", "PROPN"] and not n.feats:
            n.feats["Definite"] = "Def";
            n.feats["Gender"] = "Fem";
            n.feats["Number"] = "Plur";
            n.feats["PronType"]= "Art"

        if n.form.lower() == "o" and n.upos == "DET" and n.deprel == "det" and n.parent.upos in ["NOUN", "PROPN"] and not n.feats:
            n.feats["Definite"] = "Def";
            n.feats["Gender"] = "Masc";
            n.feats["Number"] = "Sing";
            n.feats["PronType"]= "Art"

        if n.form.lower() == "as" and n.upos == "DET" and n.deprel == "det" and n.parent.upos in ["NOUN", "PROPN"] and not n.feats:
            n.feats["Definite"] = "Def";
            n.feats["Gender"] = "Masc";
            n.feats["Number"] = "Plur";
            n.feats["PronType"]= "Art"
    doc.store_conllu(file)

for conll in sys.argv[1:]:
    correctDet(conll)