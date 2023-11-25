#!/usr/bin/env python
# coding: utf-8

# # To implement gradient descent for linear regression in python

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[2]:


df=pd.read_csv('C:\\Users\\LENOVO\\Desktop\\Mira_DS\\ML\\3.Gradient descent\\test_scores.csv')
df


# In[3]:


x=np.array(df.math)
y=np.array(df.cs)


# In[25]:


import math
m_curr=b_curr=0
iterations=1000000
cost_previous=0
learning_rate=0.0002
n=len(x)
for i in range(iterations):
    y_pred=m_curr*x+b_curr
    cost=1/n*sum([val**2 for val in (y-y_pred)])
    md=-2/n*sum(x*(y-y_pred))
    bd=-2/n*sum(y-y_pred)
    m_curr=m_curr-learning_rate*md
    b_curr=b_curr-learning_rate*bd
    if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
    cost_previous = cost
    print(m_curr,b_curr,cost,i)


# In[28]:


print('Using gradient function m,b is',m_curr,b_curr)


# In[36]:


reg=linear_model.LinearRegression()
reg.fit(df[['math']],df.cs)
print('Using sklearn: Coeff and intercept is ',reg.coef_,reg.intercept_)

