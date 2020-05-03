#!/usr/bin/env python3
"""
Correct wrong contractions of conjunction "e" (and) with next tokens "a" (the.FEM/DET or to/ADP) and "o" (the.MASC/DET or him/PRON). This is an old known bug of Portuguese-GSD: https://github.com/UniversalDependencies/UD_Portuguese-GSD/issues/5
"""
import re
import conllu
import sys
import pdb

################################################################################

def error(message):
  print("ERROR:" + message,file=sys.stderr)
  sys.exit(-1)

################################################################################

def warn(message):
  print("WARNING:" + message,file=sys.stderr)

################################################################################

def shift_after_index(tokenseq, index):
  for token in tokenseq[index+1:]:
    tid = token["id"]
    if type(tid) == int : # simple token, numerical ID
      token["id"] += 1
    elif type(tid) == tuple and len(tid) == 3 and tid[1]=="-": 
      # range, represented as tuple (first,'-',last)
      token["id"] = (tid[0] + 1, "-", tid[2] + 1)      
    elif type(tid) == tuple and len(tid) == 3 and tid[1]==".": 
      # empty node, represented as tuple (id,'.',index)
      token["id"] = (tid[0] + 1, "-", tid[2])      
    else :
      error("Unknown ID field: {}".format(str(tid)))
  for token in tokenseq:
    if token["head"] and token["head"] > int(tokenseq[index]["id"]) :
      token["head"] = token["head"] + 1
      
################################################################################

#pdb.set_trace()
for infile in sys.argv[1:]:  
  treebankreader = open(infile, "r", encoding="utf-8")
  for tokenseq in conllu.parse_incr(treebankreader):
    sent_id = tokenseq.metadata["sent_id"]
    for (itoken,token) in enumerate(tokenseq) :
      if re.fullmatch("[eE][ao]",token["form"]):
        if token["upostag"] != "CCONJ" or \
           token["deprel"] != "cc" or \
           token["head"] < token["id"] :
          warntempl = "Sentence {}, token {} UPOS={}, DEPREL={}, HEAD={}"
          warn(warntempl.format(sent_id, token["id"], token["upostag"], 
                                token["deprel"], token["head"]))        
        # Correct the "text" metadata first
        if " " + token["form"] + " " in tokenseq.metadata["text"] :
          tokenseq.metadata["text"] = tokenseq.metadata["text"].replace(
              " " + token["form"] + " ", " e " + token["form"][1] + " ", 1)
        else: # Never occurred, but you never know...
          error("Metadata 'text' does not contain token")        
        etoken = token.copy()
        etoken["form"] = token["form"][0]
        etoken["lemma"] = "e"        
        
        # Now correct "o" or "a"
        token["form"] = token["form"][1] 
        nextok = tokenseq[itoken+1]
        if nextok["upostag"] in ["NOUN", "PROPN"] and (
          (token["form"] == "o") or \
          (token["form"] == "a" and nextok["upostag"] == "NOUN" \
             and nextok["form"].endswith("a"))) : # w[i+1] is FEM.SG
            token["lemma"] = "o"
            token["upostag"] = "DET"
            token["xpostag"] = "DET"
            token["deprel"] = "det"
            token["feats"] = "Definite=Def|Gender=Masc|Number=Sing|PronType=Art"           
        else : # Guess DET but mark for checking...
          token["lemma"] = "o"
          token["upostag"] = "DET"
          token["xpostag"] = "DET"
          token["deprel"] = "det"  
          token["misc"] = "XXXXX"
          warn("Check sentence {}, token {}: {} cannot be guessed".format(sent_id,itoken,token["form"]))        
          #print(tokenseq.serialize(),end="")
          #pdb.set_trace()
        tokenseq.insert(itoken,etoken)
        shift_after_index(tokenseq, itoken)
        #print(tokenseq.serialize(),end="")
        #pdb.set_trace()
    print(tokenseq.serialize(),end="")

        

