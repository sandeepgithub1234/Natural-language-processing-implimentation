#!/usr/bin/env python
# coding: utf-8

# In[1]:


paragraph=''' 
  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

 

'''
plist=paragraph.split()

print(plist)


# In[ ]:


Definitions. "This License" refers to version 3 of the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. 
 You can apply it to your programs, too. 
 When we speak of free software, we are referring to freedom, not price. 
 Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things. 
 To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. 
 Therefore, you have certain responsibilities if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. 


# In[2]:


def Ngram(s,n):
    s=s.split()
    return ([s[i:i+n] for i in range(len(s)-(n-1))])
    


# In[3]:


print(Ngram(paragraph,3))


# In[4]:


def getNGrams(plist, n):
    ngrams = []
    for i in range(len(plist)-(n-1)):
        ngrams.append(tuple(plist[i:i+n]))
    return ngrams


# In[5]:


x=getNGrams(plist, 5)
print(x)


# In[6]:


#def frequency(getNGrams(wordlist, 4))


# In[7]:


print(len(x))
gram2 = set(x)
print(len(gram2))

# Print 20 elements from gram2
for i in gram2:
    print(i)


# In[8]:


diction=dict()
for i in gram2:
    diction[i]=0
print(diction)


# In[9]:


for i in x:
    
    diction[i]+=1
    
    


# In[10]:


print(diction)


# In[11]:


for i in sorted (diction,key=diction.get,reverse=True):
    print((i,diction[i]),"\n")


# In[13]:


def recommendation(word1,word2,word3):
    for i in sorted (diction,key=diction.get,reverse=True):
            if(i[0]==word1 and i[1]==word2 and i[2]==word3):
                print(i[3])
word1 = 'I'
word2='am'   
word3='a'
print(recommendation(word1,word2,word3))


# In[32]:


def get2GramSentence(word1,word2,word3,word4,n ):
    list1=list()
    list1.append(word1)
    list1.append(word2)
    list1.append(word3)
    list1.append(word4)
    for k in range(n):
        for i in sorted (diction,key=diction.get,reverse=True):
            if(i[0]==word1 and i[1]==word2 and i[2]==word3 and i[3]==word4):
                if(i[4][0].isupper() and( i[3][len(i[3])-1]=="."  or  i[3][len(i[3])-1]==',')):
                    list1.append('\n')
                list1.append(i[4])
                word1=word2
                word2=word3
                word3=word4
                word4=i[4]
                break
    return list1
        

word1 = 'The'
word2='licenses'
word3='for'
word4='most'
print("Start word: ", word1,word2,word3,word4)

print("4-gram sentence:")
str=" "
print(str.join(get2GramSentence(word1,word2,word3,word4,512)))


# In[14]:


The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

