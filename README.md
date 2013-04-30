wordspew: a small library to generate random English snippets of phrases. The 
results are often complete nonsene, but that's the point.

Examples:
  generatePhrases.py:    simple way of retreiving spew from the python console
  generatePhrasesWeb.py: simple web server for dishing up wordspew

Word  dictionaries for adjectives, adverbs, nouns and verbs were obtained from 
[Ashley Bovan's word lists][1].

Usage:
        >>> import wordspew
        >>> wordspew.getPhrase()
        'symbolically sloping anarchic rockery'
        >>> wordspew.getPhrase()
        'absorbingly scrags run-of-the-mill ubiquitarians'
        >>> wordspew.getPhrase()
        'three-phase underbidders'
        >>> wordspew.getPhrase()
        'finest blepharitis'
        >>> wordspew.getPhrase()
        'the institutionalization was meaningful'

[1]: http://www.ashley-bovan.co.uk/words/partsofspeech.html