"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line
 

def oneHash(line):
 line = re.sub(r'#(.*)', r'<h1>\1</h1>', line)
 return line
def twoHash(line):
 line = re.sub(r'##(.*)', r'<h2>\1</h2>', line)
 return line
def threeHash(line):
 line = re.sub(r'###(.*)', r'<h3>\1</h3>', line)
 return line
def blockQuote(line):
 line = re.sub(r'>(.*)', r'<blockquote>\1</blockquote>',line)
 return line

for line in fileinput.input():
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  line = oneHash(line)
  line = twoHash(line)
  line = threeHash(line)
  line = blockQuote(line)
print '<p>' + line + '</p>',
