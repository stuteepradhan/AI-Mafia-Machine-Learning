#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


my_arr=numpy.array([[1,2,3],[4,5,6]])


# In[4]:


print(my_arr)


# In[5]:


print(my_arr.shape)


# In[6]:


print(my_arr.ndim)


# In[7]:


a=numpy.array([[1,2,3],[4,5,6]],float)
print(a)


# In[8]:


get_ipython().run_line_magic('pinfo', 'np.arrange')


# In[9]:


get_ipython().run_line_magic('pinfo', 'np.arange')


# In[10]:


np.arange(3)


# In[11]:


np.arange(0,30,5)


# In[12]:


np.linspace(0,5,10)


# In[16]:


my_arr.reshape(3,2)


# In[17]:


my_arr.flatten()


# In[20]:


arr=numpy.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
print(arr)


# In[19]:


print(arr[1:][:3])#from first index all three columns


# In[21]:


print(arr[1:][:3:2])


# In[22]:


arr+1


# In[23]:


arr.T


# In[26]:


arr.sort(axis=1)


# In[27]:


arr


# In[31]:


print(np.vsplit(arr,2))


# In[33]:


print(np.mean(arr))


# In[34]:


print(np.median(arr))


# In[ ]:





# In[ ]:




