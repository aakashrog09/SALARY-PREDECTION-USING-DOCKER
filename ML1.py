#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy


# In[3]:


ds=pd.read_csv('salarydata.csv')


# In[4]:


x=ds['YearsExperience']


# In[5]:


y=ds['Salary']


# In[6]:


x=x.values.reshape(30,1)


# In[7]:


from sklearn.linear_model import LinearRegression


# In[8]:


model=LinearRegeression()


# In[9]:


model=LinearRegression()


# In[10]:


model.fit(x,y)


# In[11]:


years=int(input("Years of experience"))


# In[12]:


result=model.predict([[years]])


# In[13]:


print('estimated salary is ', result )


# In[ ]:




