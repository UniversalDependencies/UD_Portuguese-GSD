# Summary

The Brazilian Portuguese UD is converted from the [Google Universal Dependency
Treebank v2.0 (legacy)](https://github.com/ryanmcd/uni-dep-tb).

# Changelog

* 2022-11-01 v2.11
 * added missing lemmas of NUM tokens
 * start to fix the enclitics tokenization

* 2021-05-01 v2.8
 * Fixed verbs that are not AUX in PT 
 * Fixed some cases of missing MWT (contractions)
 * Fixed some other erros in validation. 
 * added many more missing lemmas 
 * removed undocumented subtypes "xcomp:adj" and "acl:part".
 
  We still have many validation errors and incompatibilities with
  UD_Portuguese-Bosque.

* 2019-11-15 v2.5
  * Google gave permission to drop the "NC" restriction from the license.
    This applies to the UD annotations (not the underlying content, of which Google claims no ownership or copyright).

2018-04-27 v2.3
  * Added lemmas from MorphoBr project (https://github.com/LFG-PTBR/MorphoBr), see issue #8 for more details.

2018-03-30 v2.2
  * Automatically correct UPOS and XPOS of _cop_ verbs to AUX instead
    of VERB.

2018-04-15 v2.2
  * Repository renamed from UD_Portuguese to UD_Portuguese-GSD.

2017-03-01 v2.0
  * Converted to UD v2 guidelines.

2016-05-15 v1.3
  * First release. No lemmas, no features. Dependencies converted from
    the legacy UD treebank.


```
===================================
Universal Dependency Treebanks v2.0
(legacy information)
===================================

=========================
Licenses and terms-of-use
=========================

For the following languages

  German, Spanish, French, Indonesian, Italian, Japanese, Korean and Brazilian
  Portuguese

we will distinguish between two portions of the data.

1. The underlying text for sentences that were annotated. This data Google
   asserts no ownership over and no copyright over. Some or all of these
   sentences may be copyrighted in some jurisdictions.  Where copyrighted,
   Google collected these sentences under exceptions to copyright or implied
   license rights.  GOOGLE MAKES THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY
   WARRANTY OF ANY KIND, WHETHER EXPRESS OR IMPLIED.

2. The annotations -- part-of-speech tags and dependency annotations. These are
   made available under a CC BY-SA 4.0. GOOGLE MAKES
   THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY WARRANTY OF ANY KIND, WHETHER
   EXPRESS OR IMPLIED. See attached LICENSE file for the text of CC BY-NC-SA.

Portions of the German data were sampled from the CoNLL 2006 Tiger Treebank
data. Hans Uszkoreit graciously gave permission to use the underlying
sentences in this data as part of this release.

Any use of the data should reference the above plus:

  Universal Dependency Annotation for Multilingual Parsing
  Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg,
  Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang,
  Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee
  Proceedings of ACL 2013

=======
Contact
=======

ryanmcd@google.com
joakim.nivre@lingfil.uu.se
slav@google.com
See https://github.com/ryanmcd/uni-dep-tb for more details
```

(Original treebank contributors: LaMontagne, Adam; Souček, Milan;
Järvinen, Timo; Radici, Alessandra)


<pre>
=== Machine-readable metadata =================================================
Data available since: UD v1.3
License: CC BY-SA 4.0
Includes text: yes
Genre: blog news
Lemmas: automatic
UPOS: converted from manual
XPOS: manual native
Features: not available
Relations: converted from manual
Contributors: Rademaker, Alexandre; McDonald, Ryan; Nivre, Joakim; Zeman, Daniel; Chalub, Fabricio; Ramisch, Carlos; Belieni, Juan; Wille, Vanessa Berwanger; Pintucci, Rodrigo 
Contributing: here
Contact: arademaker@gmail.com
===============================================================================
</pre>
