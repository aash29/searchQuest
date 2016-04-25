#! /usr/bin/python
import os
import sqlite3
import random
import string

conn = sqlite3.connect('example.db')
#conn.row_factory = sqlite3.Row
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

services = ['email','messenger','forum']

ppl=[]


for i in range(0,10):

    rec = dict({})
    rec['id']=i
    rec['name']=random.choice(maleNames)
    rec['surname']=random.choice(maleSurnames)
    em = ''.join(random.choice(string.ascii_lowercase) for _ in range(9))+ ''.join(random.choice(string.digits) for _ in range(2)) +'@'+''.join(random.choice(string.ascii_lowercase) for _ in range(9))+'.com'
    rec['email']=em
    rec['messenger']=''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,8)))
    rec['forum']=''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,8)))


    ppl.append(rec)
    c.execute('insert into ppl values (?,?,?,?)', [i, ppl[-1]['name'], ppl[-1]['surname'], ppl[-1]['email']])


#c.executemany("insert into ppl(id , name, surname) values (?, ?, ?)", globalMap)
'''

c.execute('SELECT * FROM ppl')
# 1 способ напечатать результат
meida = c.fetchall()
print(meida)
# 2 способ напечатать результат
for row in c.execute("select name, surname from ppl"):
    print(row)

'''
#print(len(ppl));


from random import randrange
from datetime import datetime
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2008 21:30', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('1/1/2009 14:50', '%d/%m/%Y %H:%M')

print(random_date(d1, d2))

#сгенерим траффик

msgs = [];

c.execute('DROP TABLE IF EXISTS msgs')
c.execute('''CREATE TABLE msgs
             (id integer, timestamp integer,service text, fromuser text, touser text)''')

for i in range(0,100):
    cid = random.choice([x['id'] for x in ppl])
    did = random.choice([x['id'] for x in ppl])
    #print(cid)
    rec = dict({})
    rec['id']=i
    rec['timestamp']=random.randint(0,10000)
    rec['fromid']=cid
    rec['toid']=did
    s1 = random.choice(list(set(services).intersection(ppl[cid].keys())))   #выбирать из тех сервисов, которые есть у человека
    rec['service']=s1
    fromname = ppl[cid][s1]
    rec['fromuser']=fromname
    toname = ppl[did][s1]
    rec['touser']=toname

    msgs.append(rec)

    c.execute('insert into msgs values (?,?,?,?,?)', [i, msgs[-1]['timestamp'], msgs[-1]['service'], msgs[-1]['fromuser'], msgs[-1]['touser']])

print(msgs)



conn.commit()

#запускаем командную строку

import cmd, sys, readline

class searchShell(cmd.Cmd):
    intro = 'Type help or ? to list commands.\n'
    prompt = '(echelon) '

    def __init__(self):
        super(searchShell, self).__init__()
        self.histfile = os.getcwd()+os.sep+ ".history"
        try:
            readline.read_history_file(self.histfile)
            # default history len is -1 (infinite), which may grow unruly
            readline.set_history_length(1000)
        except FileNotFoundError:
            pass

    # ----- basic turtle commands -----
    def do_select(self, arg):
        'search for entries with standart SQL syntax'
        #c.execute('SELECT ' + arg + ' FROM ppl')

        try:
            for row in c.execute('SELECT ' + arg):
                print(row)
        except sqlite3.OperationalError:
            print ('Error: unknown syntax')
        #c.execute('SELECT ' + arg)
        #print (c.fetchall())
        readline.write_history_file(self.histfile);

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    shell=searchShell()
    shell.cmdloop()



conn.close();
