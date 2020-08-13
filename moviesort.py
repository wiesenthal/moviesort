from random import shuffle
from functools import cmp_to_key

def compare(m1, m2):
    x = input(m1 + " > " + m2 + "?")
    if x == "1":
        return 1
    elif x == "2":
        return -1
    else:
        return 0

def sort(mList):
    shuffle(mList);
    mList = sorted(mList, key=cmp_to_key(compare), reverse=True)
    return mList

def insert(m, sortedList): #returns index
    if len(sortedList) == 0:
        return 0
    i = int(len(sortedList)/2)
    x = compare(m, sortedList[i])
    if x == -1:
        return i+1 + insert(m, sortedList[i+1:])
    elif x == 1:
        return insert(m, sortedList[0:i])
    else:
        return i

def readIn():
    l = []
    f = open('in.txt', 'r')
    for line in f.readlines():
        l.append(line.strip())
    f.close()
    x = sort(l)
    f2 = open('out.txt', 'w')
    for i in x:
        f2.write(i + '\n')
    f2.close()

def addNew(newList):
    l = []
    f = open('out.txt', 'r')
    for line in f.readlines():
        l.append(line.strip())
    f.close()
    for m in newList:
        i = insert(m, l)
        l.insert(i, m)
    f = open('out.txt', 'w')
    for i in l:
        f.write(i + '\n')
    f.close()

def newFromFile(file):
    l = []
    f = open('new.txt', 'r')
    for line in f.readlines():
        l.append(line.strip())
    f.close()
    addNew(l)
newFromFile('new.txt')
