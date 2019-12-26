#!/usr/bin/env python
# coding: utf-8

# In[1]:


wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()

print(wordlist[0:4])


# In[4]:


def Ngram(s,n):
    s=s.split()
    return ([s[i:i+n] for i in range(len(s)-(n-1))])
    


# In[5]:


print(Ngram(wordlist,3))


# In[14]:


def getNGrams(wordlist, n):
    ngrams = []
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(tuple(wordlist[i:i+n]))
    return ngrams


# In[16]:


x=getNGrams(wordlist, 4)
print(x)


# In[ ]:


#def frequency(getNGrams(wordlist, 4))


# In[73]:


print(len(x))
gram2 = set(x)
print(len(gram2))

# Print 20 elements from gram2
for i in gram2:
    print(i)


# In[90]:


diction=dict()
for i in gram2:
    diction[i]=0
print(diction)


# In[91]:


for i in x:
    
    diction[i]+=1
    
    


# In[92]:


print(diction)


# In[98]:


for i in sorted (diction,key=diction.get,reverse=True):
    print((i,diction[i]),"\n")


# In[126]:


def recommendation(word1,word2):
    for i in sorted (diction,key=diction.get,reverse=True):
            if(i[0]==word1 and i[1]==word2):
                print(i[2])
word1 = 'was'
word2='the'     
recommendation(word1,word2)


# In[125]:


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


# In[ ]:




