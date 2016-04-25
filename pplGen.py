#! /usr/bin/python
import os
import random
import sqlite3
import random
import string

conn = sqlite3.connect('example.db')
c = conn.cursor()

#сгенерим личностей
c.execute('DROP TABLE IF EXISTS ppl')

c.execute('''CREATE TABLE ppl
             (id integer, name text, surname text, email text)''')

with open(os.getcwd()+os.sep+'male_names.txt',encoding="utf8") as maleNamesFile:
    maleNames = maleNamesFile.read().splitlines()

with open(os.getcwd()+os.sep+'male_surnames.txt',encoding="utf8") as maleSurnamesFile:
    maleSurnames = maleSurnamesFile.read().splitlines()

#print(maleNames)

ppl=[]

for i in range(0,10):
    em = ''.join(random.choice(string.ascii_lowercase) for _ in range(9))+ ''.join(random.choice(string.digits) for _ in range(2)) +'@'+''.join(random.choice(string.ascii_lowercase) for _ in range(9))+'.com'
    ppl.append(dict({'id':i,'name':random.choice(maleNames),'surname':random.choice(maleSurnames),'email':em}))
    c.execute('insert into ppl values (?,?,?,?)', [i, ppl[-1]['name'], ppl[-1]['surname'], ppl[-1]['email']])


#c.executemany("insert into ppl(id , name, surname) values (?, ?, ?)", globalMap)


c.execute('SELECT * FROM ppl')
# 1 способ напечатать результат
meida = c.fetchall()
print(meida)
# 2 способ напечатать результат
for row in c.execute("select name, surname from ppl"):
    print(row)


#print(len(ppl));

#сгенерим траффик

msgs = [];

for i in range(0,10):
    cid = random.choice([x['id'] for x in ppl])
    did = random.choice([x['id'] for x in ppl])
    #print(cid)
    msgs.append(dict({'id':i, 'fromid': cid, 'toid': did, 'fromname':ppl[cid]['name'] }));

print(msgs);



conn.commit();


import cmd, sys

class searchShell(cmd.Cmd):
    intro = 'Type help or ? to list commands.\n'
    prompt = '(echelon) '
    file = None

    # ----- basic turtle commands -----
    def do_select(self, arg):
        'search for entries with standart SQL syntax'
        #c.execute('SELECT ' + arg + ' FROM ppl')
        c.execute('SELECT ' + arg)
        print (c.fetchall())

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    searchShell().cmdloop()



conn.close();
