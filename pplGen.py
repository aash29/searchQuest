#! /usr/bin/python
import os
import random
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS ppl')

c.execute('''CREATE TABLE ppl
             (id integer, name text, surname text)''')

with open(os.getcwd()+os.sep+'male_names.txt',encoding="utf8") as maleNamesFile:
    maleNames = maleNamesFile.read().splitlines()

with open(os.getcwd()+os.sep+'male_surnames.txt',encoding="utf8") as maleSurnamesFile:
    maleSurnames = maleSurnamesFile.read().splitlines()

#print(maleNames)

globalMap=[]

for i in range(1,10):
    globalMap.append(dict({'name':random.choice(maleNames),'surname':random.choice(maleSurnames)}))
    c.execute('insert into ppl values (?,?,?)', [i, globalMap[-1]['name'], globalMap[-1]['surname']])



c.execute('SELECT * FROM ppl')
# 1 способ напечатать результат
meida = c.fetchall()
print(meida)
# 2 способ напечатать результат
for row in c.execute("select name, surname from ppl"):
    print(row)

conn.commit();


#print(globalMap);


conn.close();
