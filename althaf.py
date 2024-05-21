#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello world')


# # list

# In[2]:


fruits=['mango','apple','orange','pineapple','pappaya']


# In[3]:


fruits


# In[4]:


fruits.append('strawberry')


# In[5]:


fruits


# In[6]:


fruits.pop(4)


# In[7]:


fruits.insert(3,'banana')


# In[8]:


fruits


# In[9]:


fruits.sort(reverse=True)


# In[10]:


fruits


# In[11]:


fruits[2]='grape'


# # tuple

# In[12]:


students=('alan','shaheen','althaf','vigneesh')


# In[13]:


type(students)


# In[14]:


s1=list(students)


# In[15]:


s1


# In[16]:


s1.append('afsal')


# In[17]:


s1


# # Dictianory

# In[18]:


cities={'kochi':'ernakulam','pala':'kottayam','kattapana':'idukki','ambalavayal':'wayanad'}


# In[19]:


cities


# In[20]:


names={'althaf':'ernakulam','shaheen':'kottayam','alan':'idukki','vigneesh':'wayanad'}


# In[21]:


names


# In[22]:


names['shaheen']


# In[23]:


names['afsal']='karupadanna'


# In[24]:


names


# In[25]:


cities['chalakudy']='thrissur'


# In[26]:


cities


# In[27]:


cities.pop('chalakudy')


# In[28]:


cities


# In[29]:


cities.popitem()


# In[30]:


states={'kl':{'capital':'tvm','rank':1},'TN':{'capital':'cni','rank':2},'KA':{'capital':'blr','rank':3},'TS':{'capital':'hyd','rank':4}}


# In[31]:


states


# In[32]:


states['TS']


# In[33]:


states['KA']['rank']


# In[34]:


states['TS']['capital']


# In[35]:


set_1={'apple','orange','mango','grapes','pineapple','strawbery','grapes','mango','watermelon'}


# In[36]:


type(set_1)


# In[37]:


set_1


# In[38]:


set_1.add('kiwi')


# In[39]:


set_1


# In[40]:


set_1.pop()


# In[41]:


set_1.remove('mango')


# In[42]:


set_1


# In[43]:


def addition(x,y):
    c=x+y
    return c


# In[44]:


a=int(input('Enter no 01:'))
b=int(input('Enter no 02:'))
addition(a,b)


# # DAY 3

# In[45]:


def addition(a,b):
    c=a+b
    return (c)


# In[46]:


a=int(input('Enter no 01:'))
b=int(input('Enter no 02:'))
addition(a,b)


# In[47]:


addition(5,6)


# In[48]:


def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    


# In[49]:


largest(433,455,687)


# # Questions

# In[50]:


scorelist={'1':{'diljith':'Titans','score':455},'2':{'biju':'wolves','score':400},'3':{'shaji':'stunners','score':350},'4':{'sabu':'assasins','score':330}}


# In[51]:


scorelist


# In[52]:


scorelist['2']


# In[54]:


score = [5,3,7,8,9,9]
sc_set=set(score
top=max(sc_set)
sc_set.remove(top)
print(max(sc_set))


# In[ ]:


top


# In[ ]:


set_1={2,5,7,88,99,33,67}
set_2={55,5,88,44,64,89,3}
if set_1.intersection(set_2):
    print(set_1&set_2)
else:
    print(set_1.union(set_2))


# In[56]:


D={'john' :[25,32,43],'peter':[87,55,96],'ram':[58,55,43],'meena':[63,79,85]}
n =input('Enter the name to be updated')
if n in D:
   D[n]=[88,77,99]
   print(D)
else:    
    print('Name not Found')


# In[ ]:





# In[ ]:




