# i.
#Observatory:
- 42 contributors
- 33839 total total lines of code
# First Commit: 
- commit ac21a034bd4085bcf9b87fc44b43a558698e02cf
- Author: Aaron Gunderson <airgunde@gmail.com>
- Date:   Mon Dec 8 21:45:33 2014 -0500
# Initial commit
# Most Recent Commit:
- commit fb202da270f620caae609e0736770af7e42d379b
- Merge: 803c6c1 bf6bb93
- Author: Alexander Schwartzberg <aeksco@gmail.com>
- Date:   Sat Oct 6 12:06:18 2018 -0400
# Merged upstream
# Branches:
- master
- dev
- gh-pages
- vagrant-for-windows
- blogfolders
- urp-form
- feature/455

Gitstats does an excellent job of showing change over time, as
opposed to handwriting observations, which is tedious even only
taking specific moments (like first and most recent commit)




# ii.
MCO
- contributers 3
- LOC 103388
- First: Initial commit
- Latest: template init
- branches:
	- master
	- gh-pages
- git stats
	- the total LOC found is less that wc found probably because it doesnt incluse whitespace
	- they also say 4 authors instead of the 3 github said on the top bar there may be an author with only commits in another branch
[MCO gource](http://www.bierysbargainbarn.com/gource.mp4)
it seems like jeremiah has the most input altho 99k lines in 15 commits is kinda weird...




# iii.
https://github.com/musicexmachina/mxm
5 contributors
39059 lines of code

The initial commit was on 9/1/2016 by Patrick Celentano
The latest commit was on 2/2/2018 by jpatsenker
There are 7 branches currently (As of 1/29/2019)




# iv.
RCOS-MicrofossilSorter Number of contributors: 3 Number of lines of code: 109076 Initial commit: "Initial Commit", Fri Jan 26 16:59:32 2018 -0500 Latest Commit: "half approach.py function documented", Fri Dec 7 17:33:59 2018 -0500 Current Branches: master, WebsiteUpdate, documentation Compared to the above, GitStats returned less total lines of code, with 2874 lines. The number of contributors on GitHUb is half as many authors returned by GitStats. Gource Video: https://www.youtube.com/watch?v=UhHALqy0crA












Part 2.
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







test code

'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('this line has no special handling'), 
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')
                
    def test_hash(self):
    '''
    Lines with one or more(up to three) hashtags
    '''
        self.assertEqual(
                run_markdown('#testOne'),
                '<h1>testOne</h1>')
        self.assertEqual(
                run_markdown('#testTwo'),
                '<h2>testOne</h2>')
        self.assertEqual(
                run_markdown('#testThree'),
                '<h3>testOne</h3>')
         
    def test_block
    '''
    Lines with blockquotes
    '''
        self.assertEqual(
            run_markdown('>this is a
                          >blockquote'),
            '<blockquote>this is a blockquote</blockquote>')
    

if __name__ == '__main__':
unittest.main()

