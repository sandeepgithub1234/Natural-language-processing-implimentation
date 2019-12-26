#!/usr/bin/env python
# coding: utf-8

# sandeep kumar jnu


p=[ "." ,",","?","!",";",":"," "" ","'","-","()"]


def IsPunctuation(string):
    for i in string:
        flag=0
        for j in p:
            if(i==j):
                flag=1
        if(flag==0):
            return False
    return True    


string="!"
print(IsPunctuation(string))


Lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


Upper=[]
for i in range(len(Lower)):
    Upper.append(Lower[i].upper())
print(Upper)    


letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Digit=['0','1','2','3','4','5','6','7','8','9','10','.']


def Isdigit(string):
    for s in string:
        flag=0
        for i in Digit:
            if(i==s):
                flag=1
        if(flag==0):
            return False
    return True
    


string="1238374298439.93748943732"
def IsNumber(string):
    if(Isdigit(string)):
        print(string,"is number")


IsNumber(string)


def IsAlpha(string):
    if(Isdigit(string[0])):
        return False
    for i in string:
        flag=0
        for j in letter:
            if(j==i):
                flag=1
        if(flag==0):
            return False
    return True 

def Isalphanumberic(string):
    if( Isdigit(string)==False and  IsAlpha(string)==False):
        print(string,"is alphanumeric")
    else:
        print(string,"is not alphanumeric")
        


string="sandeep@123"
Isalphanumberic(string)

string="sandeep"
print(IsAlpha(string))


from nltk.corpus import words


print("now" in words.words())

print("fast" in words.words())


filename1 ='textdata.txt'
file = open(filename1, 'rt')
text1 = file.read()
file.close()


print(text1)


print(text1.split())


text1=text1.split()
for i in text1:
    if(i==',' or i==';' or i==':' or i=='?' or i=='!' or i=='.'):
        text1.remove(i)


print(text1)


def wordpresent_in_ntlk(list_of_word):
    
    for i in list_of_word:
            if(i.lower() in words.words()): 
                print(i,"is a word")
            else:
                print(i," is not a word")


list_of_word=['i','am','a','student','was','punch','miscellaneous','match','matched','gaurav','sandeep@123']
wordpresent_in_ntlk(list_of_word)


def Isword(string):
    if(IsAlpha(string)):
        wordpresent_in_ntlk([string])
    else:
        print(string," is not a word")
        


Isword("deep")



