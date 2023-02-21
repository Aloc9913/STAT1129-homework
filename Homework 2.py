#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = 0 
print(n)
while True:
    n = n + 1
    
    if n == 5:
        break 
    print(n)


# In[9]:


n = 0 
print(n)
while True:
    n = n + 1
    
    if n == 5:
        break 
    print(n)
    
print("5 is not less than 5")


# In[10]:


favfruit = ["peach", "mango", "strawberry", "apple"]
for fruit in favfruit:
        if fruit == "peach":
            print("I like peach")
        if fruit == "mango":
            print("I like mango")
        if fruit == "strawberry":
            print("I like strawberry")
else:
        print("apple is really a fruit?")


# In[11]:


h = 0 
sum = 0
while h < 31:
    sum += h
    h += 1
print("sum:", sum)


# In[13]:


grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70: 
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# In[29]:


name_marks = {"Andy":88, "Amy":66, "James": 90, "Arthur": 77}
for name, marks in name_marks.items():
    print(f"{name} , {marks} ")


# In[23]:


len(name_marks)


# In[24]:


max(name_marks)


# In[31]:


min(name_marks)


# In[40]:


name_int_marks = {"Andy": 88, "Amy": 66, "James": 90, "Arthur": 77}


# In[37]:


max(name_int_marks.values())


# In[38]:


min(name_int_marks.values())


# In[47]:


88+66+90+77


# 321/4

# In[48]:


321 / 4


# In[58]:


name_marks = {"Andy":88, "Amy":66, "James": 90, "Arthur": 77}
for name, marks in name_marks.items():
    if name == "James":
        break
    print(f"{name} , {marks} ")


# In[ ]:




