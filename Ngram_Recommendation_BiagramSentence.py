#!/usr/bin/env python
# coding: utf-8
# sandeep kumar jnu




wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()

print(wordlist[0:4])




def Ngram(s,n):
    s=s.split()
    return ([s[i:i+n] for i in range(len(s)-(n-1))])
    


print(Ngram(wordlist,3))



def getNGrams(wordlist, n):
    ngrams = []
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(tuple(wordlist[i:i+n]))
    return ngrams



x=getNGrams(wordlist, 4)
print(x)



#def frequency(getNGrams(wordlist, 4))



print(len(x))
gram2 = set(x)
print(len(gram2))

# Print 20 elements from gram2
for i in gram2:
    print(i)



diction=dict()
for i in gram2:
    diction[i]=0
print(diction)


for i in x:
    
    diction[i]+=1
    
print(diction)


for i in sorted (diction,key=diction.get,reverse=True):
    print((i,diction[i]),"\n")




def recommendation(word1,word2):
    for i in sorted (diction,key=diction.get,reverse=True):
            if(i[0]==word1 and i[1]==word2):
                print(i[2])
word1 = 'was'
word2='the'     
recommendation(word1,word2)



def get2GramSentence(word1,word2,n ):
    list1=list()
    list1.append(word1)
    list1.append(word2)
    for k in range(n):
        for i in sorted (diction,key=diction.get,reverse=True):
            if(i[0]==word1 and i[1]==word2):
                list1.append(i[2])
                word1=word2
                word2=i[2]
                break
    return list1
        

word1 = 'was'
word2='the'
word3='age'
print("Start word: ", word1,word2,word3)

print("2-gram sentence:")
print(get2GramSentence(word1,word2,7))
print(" ")
