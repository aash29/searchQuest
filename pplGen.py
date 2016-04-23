#! /usr/bin/python
import os
import random
import sqlite3

with open(os.getcwd()+os.sep+'male_names.txt',encoding="utf8") as maleNamesFile:
    maleNames = maleNamesFile.read().splitlines()

with open(os.getcwd()+os.sep+'male_surnames.txt',encoding="utf8") as maleSurnamesFile:
    maleSurnames = maleSurnamesFile.read().splitlines()

#print(maleNames)

globalMap=[]

for i in range(1,10):
    globalMap.append(dict({'name':random.choice(maleNames),'surname':random.choice(maleSurnames)}))

print(globalMap);
