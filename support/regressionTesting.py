# -*- coding: utf-8 -*-
#

import os

class Tester(object):
    def loadBooks(self, path):
        books = {}
        dirList=os.listdir(path)
        print '     Checking ' + path
        #print '     Loading all Usfm files from ' + path
        for fname in dirList:
          try:
              f = open(path + '/' + fname,'U') # U handles line endings
              usfm = f.read().decode('utf-8-sig')
              books[fname] = usfm
              #print '     Loaded ' + fname
              f.close()
          except:
              if not fname == '.DS_Store':
                  print '     - Couldn\'t open ' + fname
        #print '     Finished loading'
        return books
    
    def test(self, dir):
        books = self.loadBooks(dir)
        for b in books:
            self.testMalformedCodes(b)
            self.testDuplicates(b)

    def testMalformedCodes(self, b):
        w = b.split(u' \n\t.,:?;\'\"')
        self.checkForCode('sea', w)
        
    def checkForCode(self, c, w):
        if c in w:  print '     - Malformed code? \'' + c + '\' in ' + b[:50]
    
    def testDuplicates(self, b):
        for i, c in enumerate(b):
            if c in '.,\'"‘’“”' and b[i+1] == c:
                print 'Duplicate "' + c + '" in ' + b