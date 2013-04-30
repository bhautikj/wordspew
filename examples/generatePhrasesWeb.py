#
# Run a tiny little web server to serve up json-wrapped wordspew. Usage:
# python generatePhrasesWeb.py
# then go to a web browser and visit:
# http://localhost:8080/spew?getspew&num=20
# Adjust the num parameter to change the number of phrases that are spewed
#
# requires: the fabulous webpy module - see: http://webpy.org/
#
# (c) Bhautik J Joshi 2013
# bjoshi@gmail.com
#

import wordspew

import web
from web import form

import json

urls = (
"/spew", "spew"
)

class spew:
  def GET(self):
    params = web.input()
    numParams = len(params.keys())
    if "getspew" in params.keys():
      numspew = 1
      if "num" in params.keys():
        numspew = int(params["num"])
      ret = []
      for i in range (0, numspew):
        ret.append (wordspew.getPhrase())
      return json.dumps(ret)


wordspewApp = web.application(urls, locals())
wordspewApp.internalerror = web.debugerror

if __name__ == "__main__":
  wordspewApp.run()
