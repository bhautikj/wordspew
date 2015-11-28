#
#  Copyright (c) 2013 Bhautik J Joshi (bjoshi@gmail.com)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#


# wordspew: a small library to generate random English snippets of phrases. The 
# results are often complete nonsene, but that's the point.
#
# Word  dictionaries for adjectives, adverbs, nouns and verbs were obtained from 
# http://www.ashley-bovan.co.uk/words/partsofspeech.html.
#
# Usage:
#  
# >>> import wordspew
# >>> wordspew.getPhrase()
# 'symbolically sloping anarchic rockery'
# >>> wordspew.getPhrase()
# 'absorbingly scrags run-of-the-mill ubiquitarians'
# >>> wordspew.getPhrase()
# 'three-phase underbidders'
# >>> wordspew.getPhrase()
# 'finest blepharitis'
# >>> wordspew.getPhrase()
# 'the institutionalization was meaningful'
  
import random, os

# simple dict to wrap the available word lists - type: (file, num lines)
worddb = {'adjective':('words/adjectives.txt',28479),
          'adverb':('words/adverbs.txt',6276),
          'noun':('words/nouns.txt',90963),
          'verb':('words/verbs.txt',30802) }

# a few simple phrase patterns
phrasePatterns = [ "adverb verb adjective noun",
                   "verb noun",
                   "adverb verb noun",
                   "the noun was adjective",
                   "noun adverb verb",
                   "adjective noun" ]

relpath = "."

TITLE = 'title'
UPPER = 'upper'

class CaseError(Exception):
  pass

# __init__.py will set the library path so we can access the word lists
def setRelpath(path):
  global relpath
  relpath = path

# Get a random work from a word list. The word lists have one word per line.
def getWord(wordType):
  global relpath
  
  # small error check to validate that we are accessing a known word list
  if wordType not in worddb.keys():
    raise
  
  result = ""
  filepath = os.path.join(relpath, worddb[wordType][0])
  fp = open(filepath,"r")
  
  # select a random entry
  nlines = worddb[wordType][1]
  index = int(random.random()*nlines)
  
  # we don't want to actually go through the entire file until we get to 
  # the line we are looking for. This emulates random-access by line number.
  for i, line in enumerate(fp):
    if i == index:
      # strip off \r\n from the end of the line
      result = line[:-2]
  fp.close()
  
  return result

def getPhrase(case=None):
  # pick a random phrase pattern
  nPhrases = len(phrasePatterns)
  phrase = phrasePatterns[int(random.random()*nPhrases)]
  pat = phrase.split(" ")
  
  # replace known phrase elements with random words from the word lists
  retList = []
  for word in pat:
    sub = word
    if word in worddb.keys():
      sub = getWord(word)
    if case is None:
      pass
    elif case == TITLE:
      sub = sub.title()
    elif case == UPPER:
      sub = sub.upper()
    else:
      raise CaseError("Unsupported character case '%s'" % case)
    retList.append(sub)
    
  # join and return
  return " ".join(retList)
