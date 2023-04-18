#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Human:
    
    class_attribute_1_gender = "male"
    class_attribute_2_has_hair = True 
    class_attribute_3_two_hands = True 
    
    
    
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height 
        
A = Human(name="Asher", age = 20, height = 5.7)
A.name

B = Human(name="Dylan", age = 20, height = 6.2)
B.height


# In[12]:


class point:
    
    def __init__(self, x=0, y=0):
        self.move(x,y)
        
    def move(self,x,y):
        self.x=x
        self.y=y
        
    def reset(self):
        self.move(0,0)
        
    def CalcDist(self,M,N):
        print(math.sqrt((M.x-N.x)**2+(M.y-N.y)**2))


# In[ ]:




