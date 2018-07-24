
# coding: utf-8

# In[1]:


import os, random


# In[11]:


def randPassGen():
    key_L = 12
    key_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%*'
    print(''.join(random.choice(key_chars)for password in range(key_L)))

