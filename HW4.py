#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


numbers = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(numbers)


# In[4]:


for row in numbers:
    for column in row:
        print(column, end=' ')
        
    print()


# In[5]:


for i in numbers.flat:
    print(i, end='')


# In[ ]:


#begin question 2 


# In[6]:


import matplotlib 


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


xpoints = np.array([1,6])
ypoints = np.array([5,10])

plt.plot(xpoints, ypoints)
plt.show()


# In[10]:


xpoints = (3, 6, 9, 12)
ypoints = (2, 8, 1, 10)

plt.plot(xpoints, ypoints, marker = 'o')
plt.show()


# In[14]:


xpoints = (0, 1, 2, 3, 4, 5)
ypoints = (2, 4, 6, 14, 10, 12)

plt.plot(xpoints, ypoints, 'D:r', ms = 10, mec = 'g',mfc = 'g')
plt.show()


# In[16]:


#question 4

y1 = np.array([4, 5, 6, 7, 8])
y2 = np.array([7, 8, 9, 10, 11])
y3 = np.array([9, 10, 11, 12, 13])

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)

plt.show()


# In[19]:


#question 5 

marks = {'Andy':88,'Amy':66,'James':55,'Arthur':77}

x = ('Andy', 'Amy', 'James', 'Arthur')
y = (88, 66, 55, 77)

plt.title("Marks")

plt.bar(x,y)
plt.show()


# In[21]:


y = np.array([88, 66, 55, 77])
mylabels = ["Andy", "Amy", "James", "Arthur"]

plt.pie(y, labels = mylabels)
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.show()


# In[22]:


#Question 6 
points = np.array([[1,2,3], [5,6,7]])


# In[34]:


x = np.array([1, 2, 3])
y = np.array([5, 6, 7])

plt.subplot(2, 3, 1)
plt.bar(x,y)

x = np.array([1, 2, 3])
y = np.array([5, 6, 7])

plt.subplot(2, 3, 2)
plt.scatter(x,y)

x = np.array([1, 2, 3, 5, 6, 7])

plt.subplot(2, 3, 3)
plt.pie(x)

y1 = np.array([4, 5, 6, 7, 8])
y2 = np.array([7, 8, 9, 10, 11])
y3 = np.array([9, 10, 11, 12, 13])

plt.subplot(2, 3, 4)

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.grid()
plt.show()

x = [1, 1, 2, 3, 5, 6, 7, 8, 9, 4, 5, 6]

plt.subplot(2, 3, 5)
plt.hist(x)


# In[ ]:




