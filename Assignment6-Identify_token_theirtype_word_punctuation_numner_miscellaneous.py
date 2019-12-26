#!/usr/bin/env python
# coding: utf-8

# In[72]:


p=[ "." ,",","?","!",";",":"," "" ","'","-","()"]


# In[73]:


def IsPunctuation(string):
    for i in string:
        flag=0
        for j in p:
            if(i==j):
                flag=1
        if(flag==0):
            return False
    return True    


# In[74]:


string="!"
print(IsPunctuation(string))


# In[75]:


Lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# In[76]:


Upper=[]
for i in range(len(Lower)):
    Upper.append(Lower[i].upper())
print(Upper)    


# In[77]:


letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# In[107]:


Digit=['0','1','2','3','4','5','6','7','8','9','10','.']


# In[79]:


def Isdigit(string):
    for s in string:
        flag=0
        for i in Digit:
            if(i==s):
                flag=1
        if(flag==0):
            return False
    return True
    


# In[108]:


string="1238374298439.93748943732"
def IsNumber(string):
    if(Isdigit(string)):
        print(string,"is number")


# In[109]:


IsNumber(string)


# In[110]:


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


# In[111]:


def Isalphanumberic(string):
    if( Isdigit(string)==False and  IsAlpha(string)==False):
        print(string,"is alphanumeric")
    else:
        print(string,"is not alphanumeric")
        
        


# In[112]:


string="sandeep@123"
Isalphanumberic(string)


# In[113]:


string="sandeep"
print(IsAlpha(string))


# In[114]:


from nltk.corpus import words


# In[117]:


print("now" in words.words())


# In[118]:


print("fast" in words.words())


# In[119]:


filename1 ='textdata.txt'
file = open(filename1, 'rt')
text1 = file.read()
file.close()


# In[120]:


print(text1)


# In[121]:


print(text1.split())


# In[122]:


text1=text1.split()
for i in text1:
    if(i==',' or i==';' or i==':' or i=='?' or i=='!' or i=='.'):
        text1.remove(i)


# In[123]:


print(text1)


# In[129]:


def wordpresent_in_ntlk(list_of_word):
    
    for i in list_of_word:
            if(i.lower() in words.words()): 
                print(i,"is a word")
            else:
                print(i," is not a word")


# In[130]:


list_of_word=['i','am','a','student','was','punch','miscellaneous','match','matched','gaurav','sandeep@123']
wordpresent_in_ntlk(list_of_word)


# In[131]:


def Isword(string):
    if(IsAlpha(string)):
        wordpresent_in_ntlk([string])
    else:
        print(string," is not a word")
        


# In[137]:


Isword("deep")


# In[ ]:




