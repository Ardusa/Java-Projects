import math
from random import randint

def Q1():
    def Palindrome(string):
        palindromeStat = False
        for i in range(len(string)):
            if string[i]==string[-(i+1)]:
                palindromeStat=True
            else:
                palindromeStat=False
        return palindromeStat

    print('Tuple Examples: civic madam kayak hannah\n')
    pali = input('Enter Proposed Palindrome: ')
    print('Is', pali, 'a palindrome? ', Palindrome(pali))
    
def Q2():
    #Number 1 - Create a tuple that has 5 elements
    def TupleFive():
        tup=(randint(1,10),randint(1,10), randint(1,10),
        randint(1,10),randint(0,10))
        return tup

    print('New Tuple of five:',TupleFive(),'\n')
    def Exists(x, t):
        for i in t:
            if i==x:
                return True
        return False

    #Number 2 - Check whether an element exists within a tuple
    tuplestr = 'Hey','There',','
    print('Tuple:', tuplestr,'\n')
    str, str2 = 'There','Ankur'
    print('Does',str,'exist in tuple?',Exists(str,tuplestr))
    print('Does',str2,'exist in tuple?',Exists(str2,tuplestr), '\n')

    #Number Five, Three, and Four - Length, Splice, Indexes
    def Half(tup):
        half = len(tup)//2
        first=tup[:half]
        last=tup[half:]
        return first,last

    stuple = (1, 2, 3, 8, 5, 6, 7, 8, 9, 10)
    print('Tuple:', stuple, '\n')
    print('Length of tuple:', len(stuple))
    print('Tuple split:', Half(stuple))

    def indexOf(x,t):
        indexes=[]
        for i in range(len(t)):
            if t[i]==x:
                indexes.append(i)
        return indexes

    print("Index(es) of 8:",indexOf(8,stuple))

Qinput = int(input('What question? '))
if Qinput == 1:
    Q1()
elif Qinput == 2:
    Q2()
else:
    print('invalid input')