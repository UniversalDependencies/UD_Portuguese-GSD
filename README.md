# Summary

The Brazilian Portuguese UD is converted from the [Google Universal Dependency
Treebank v2.0 (legacy)](https://github.com/ryanmcd/uni-dep-tb).

# Changelog

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


# Universal Dependency Treebanks v2.0

A description of how this treebank was generated can be found in:

  Universal Dependency Annotation for Multilingual Parsing
  Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg,
  Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang,
  Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee
  Proceedings of ACL 2013

#  License

we will distinguish between two portions of the data.

1. The underlying text for sentences that were annotated. This data Google
   asserts no ownership over and no copyright over. Some or all of these
   sentences may be copyrighted in some jurisdictions.  Where copyrighted,
   Google collected these sentences under exceptions to copyright or implied
   license rights.  GOOGLE MAKES THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY
   WARRANTY OF ANY KIND, WHETHER EXPRESS OR IMPLIED.

2. The annotations -- part-of-speech tags and dependency annotations. These are
   made available under a CC BY-NC-SA 3.0 non commercial license. GOOGLE MAKES
   THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY WARRANTY OF ANY KIND, WHETHER
   EXPRESS OR IMPLIED. See attached LICENSE file for the text of CC BY-NC-SA.

We are greatful to researchers at those institutes who provided us
data, in particular:

Maria Simi and company from the University of Pisa.
  Converting Italian Treebanks: Towards an Italian Stanford Dependency Treebank
  Bosco, Cristina and Montemagni, Simonetta and Simi, Maria
  Proceedings of LAW VII \& ID

Filip Ginter and company from the University of Turku.
  Building the essential resources for Finnish: the Turku Dependency Treebank
  Haverinen, Katri and Nyblom, Jenna and Viljanen, Timo and Laippala,
  Veronika and Kohonen, Samuel and Missil{\"a}, Anna and Ojala, Stina and
  Salakoski, Tapio and Ginter, Filip
  Language Resources and Evaluation, 2013

Joakim Nivre and company from Uppsala University.

And Chris Manning and Marie-Catherine de Marneffe from Stanford and Ohio.
  Generating typed dependency parses from phrase structure parses
  MC De Marneffe, B MacCartney, CD Manning,
  Proceedings of LREC, 2006

Any use of the data should reference the above plus:

  Universal Dependency Annotation for Multilingual Parsing
  Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg,
  Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang,
  Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee
  Proceedings of ACL 2013
  
(Original treebank contributors: LaMontagne, Adam; Souček, Milan;
Järvinen, Timo; Radici, Alessandra)


<pre>
=== Machine-readable metadata =================================================
Data available since: UD v1.3
License: CC BY-NC-SA 3.0 US
Includes text: yes
Genre: blog news
Lemmas: automatic
UPOS: converted from manual
XPOS: manual native
Features: not available
Relations: converted from manual
Contributors: McDonald, Ryan; Nivre, Joakim; Zeman, Daniel; Rademaker, Alexandre; Chalub, Fabricio; Ramisch, Carlos
Contributing: here
Contact: arademaker@gmail.com
===============================================================================
</pre>
