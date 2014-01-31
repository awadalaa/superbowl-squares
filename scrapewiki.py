#!/usr/bin/python
# Filename: scrapewiki.py
import urllib.request
from datetime import date
from roman import toRoman
import re

def startScraping():
    numeralarr = getAllBowlNumerals()
    for bowlnumeral in numeralarr:
        pullWikiSuperBowlDataForBowl(bowlnumeral)

def getAllBowlNumerals():
    numerals = []
    firstBowlYear = 1966
    currentYear = date.today().year
    for i in range(1,currentYear - firstBowlYear + 1):
        numerals.append(toRoman(i))
        # print(toRoman(i))
    return numerals
    

def pullWikiSuperBowlDataForBowl(n):
    numeralarr = getAllBowlNumerals()
    if n not in [numeralarr]:
        return
    wikiBowlPage = urllib.request.urlopen("http://en.wikipedia.org/wiki/Super_Bowl_" + numeralarr[0]).read().decode("utf-8")
    print (wikiBowlPage)
    # remove everything before Box Score on the wiki page
    wikiBowlPage = re.sub("(?s).*?(<span class=\"toctext\">Box score)", "\\1", wikiBowlPage, 1)
    
    # remove everything after Box Score on the wiki page
    
    print(wikiBowlPage)
    #urllib.request.urlopen("http://en.wikipedia.org/wiki/Super_Bowl_I").read()
