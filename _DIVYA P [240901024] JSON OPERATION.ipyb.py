#!/usr/bin/env python
# coding: utf-8

# In[2]:


f=open("D:/textfile.txt",'w')
f.write("first line\n")
f.write("second line\n")
f.write("third line\n")
f.close()
k=open("D://textfile.txt",'r')
print(k.readline())
print(k.readline())
print(k.readline())
k.close()


# In[7]:


m=open("D:/textfile.txt",'a')
m.write("fourth line\n")
m.write("fifth line\n")
m.close()
p=open("D:/textfile.txt",'r')
print(p.read())
p.close()


# In[8]:


with open("D:/textfile.txt",'r')as file:
 lines=file.readlines()
 print(lines)


# In[9]:


import json
x='{"name":"jhon","age":30,"city":"New york"}'
y=json.loads(x)
print(y["age"])


# In[10]:


data={
    "name":"jhon",
    "age":"30",
    "city":"New york"
}
json_data=json.dumps(data)
print(json_data)


# In[ ]:




